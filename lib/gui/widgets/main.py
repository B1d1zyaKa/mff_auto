import json
from os.path import exists
from PyQt5.QtWidgets import QMainWindow
import lib.gui.designes.main_window as design

from lib.gui.single_task_manager import AutoPlayTask, DailyTriviaTask, WorldBossInvasionTask, SquadBattleAllTask
from lib.gui.queue_manager import QueueList
from lib.gui.logger import QTextEditFileLogger
from lib.gui.widgets.game_image import ScreenImageLabel
from lib.gui.threading import ThreadPool
from lib.gui.helper import TwoStateButton, set_default_icon

from lib.game.game import Game
from lib.players.nox_player import NoxWindow
import lib.logger as logging

logger = logging.get_logger(__name__)


def load_game_settings(path="settings/gui/game.json"):
    """Load game settings for GUI."""
    if exists(path):
        with open(path, encoding='utf-8') as json_data:
            return json.load(json_data)


def save_game_settings(json_data, path="settings/gui/game.json"):
    """Store game settings."""
    with open(path, mode='w', encoding='utf-8') as file:
        json.dump(json_data, file)


class MainWindow(QMainWindow, design.Ui_MainWindow):
    """Class for working with main GUI window."""

    def __init__(self):
        """Class initialization."""
        super().__init__()
        self.setupUi(self)
        set_default_icon(window=self)
        self.player = NoxWindow("NoxPlayer")
        self.game = Game(self.player)
        self.logger = QTextEditFileLogger(logger_widget=self.logger_text)
        run_and_stop_button = self.create_blockable_button(button=self.run_queue_button)
        autoplay_button = self.create_blockable_button(button=self.autoplay_button)
        daily_trivia_button = self.create_blockable_button(button=self.daily_trivia_button)
        world_boss_invasion_button = self.create_blockable_button(button=self.world_boss_invasion_button)
        squad_battle_button = self.create_blockable_button(button=self.squad_battle_button)
        self.queue_list = QueueList(list_widget=self.queue_list_widget, run_and_stop_button=run_and_stop_button,
                                    add_button=self.add_queue_button, edit_button=self.edit_queue_button,
                                    remove_button=self.remove_queue_button,
                                    select_all_button=self.list_select_all_button,
                                    deselect_all_button=self.list_deselect_all_button, game=self.game)
        self.autoplay = AutoPlayTask(game=self.game, button=autoplay_button)
        self.daily_trivia = DailyTriviaTask(game=self.game, button=daily_trivia_button)
        self.world_boss_invasion = WorldBossInvasionTask(game=self.game, button=world_boss_invasion_button)
        self.squad_battle = SquadBattleAllTask(game=self.game, button=squad_battle_button)
        self.screen_image = ScreenImageLabel(player=self.player, widget=self.screen_label)
        self.load_settings_from_file()
        self.acquire_heroic_quest_rewards_state_changed()
        self.acquire_heroic_quest_rewards_checkbox.stateChanged.connect(self.acquire_heroic_quest_rewards_state_changed)
        self.mission_team_spin_box.valueChanged.connect(self.mission_team_changed)
        self.timeline_team_spin_box.valueChanged.connect(self.timeline_team_changed)
        self.threads = ThreadPool()
        self.update_labels()
        self.blockable_buttons = [self.run_queue_button, self.add_queue_button, self.edit_queue_button,
                                  self.remove_queue_button, self.squad_battle_button, self.world_boss_invasion_button,
                                  self.daily_trivia_button, self.autoplay_button]
        self.tasks = [self.autoplay, self.daily_trivia, self.world_boss_invasion, self.squad_battle]

    def update_labels(self):
        """Update game's labels in thread to prevent GUI freezing."""
        self.threads.run_thread(target=self._update_labels)

    def _update_labels(self):
        """Update game's labels such as: username, energy, gold and boost points."""
        self.label_username.setText(self.game.user_name)
        self.label_energy.setText(f"Energy: {self.game.energy} / {self.game.energy_max}")
        self.label_gold.setText(f"Gold: {self.game.gold}")
        self.label_boosts.setText(f"Boosts: {self.game.boost} / {100}")

    def mission_team_changed(self):
        """'Mission team' spinbox event when value is changed."""
        team = self.mission_team_spin_box.value()
        self.game.set_mission_team(team)
        logger.info(f"Team number for missions : {self.game.mission_team}")

    def timeline_team_changed(self):
        """'Timeline team' spinbox event when value is changed."""
        team = self.timeline_team_spin_box.value()
        self.game.set_timeline_team(team)
        logger.info(f"Team number for TimeLine battles : {self.game.timeline_team}")

    def acquire_heroic_quest_rewards_state_changed(self):
        """'Acquire heroic quest rewards' checkbox even when value is changed."""
        if self.acquire_heroic_quest_rewards_checkbox.isChecked():
            self.game.ACQUIRE_HEROIC_QUEST_REWARDS = True
        else:
            self.game.ACQUIRE_HEROIC_QUEST_REWARDS = False
        logger.info(f"Acquire Heroic Quest rewards: {self.game.ACQUIRE_HEROIC_QUEST_REWARDS}")

    def load_settings_from_file(self):
        """Load settings and apply them to game."""
        game_settings = load_game_settings()
        if not game_settings:
            return
        self.timeline_team_spin_box.setValue(game_settings.get("timeline_team"))
        self.mission_team_spin_box.setValue(game_settings.get("mission_team"))
        self.acquire_heroic_quest_rewards_checkbox.setChecked(game_settings.get("acquire_heroic_quest_rewards"))
        self.timeline_team_changed()
        self.mission_team_changed()
        self.acquire_heroic_quest_rewards_state_changed()

    def save_settings_to_file(self):
        """Store GUI settings to file."""
        game_settings = {
            "timeline_team": self.game.timeline_team,
            "mission_team": self.game.mission_team,
            "acquire_heroic_quest_rewards": self.game.ACQUIRE_HEROIC_QUEST_REWARDS
        }
        save_game_settings(game_settings)
        logger.debug("Game settings saved.")

    def closeEvent(self, event):
        """Main window close event."""
        self.queue_list.stop_queue()
        for task in self.tasks:
            task.abort()
        self.save_settings_to_file()
        self.queue_list.save_queue_to_file()

    def create_blockable_button(self, button):
        """Create button that blocks others."""
        two_state_button = TwoStateButton(button=button)
        two_state_button.connect_first_state(self.block_buttons, caller_button=button)
        two_state_button.connect_second_state(self.unblock_buttons)
        two_state_button.signals.first_state.connect(self.unblock_buttons)
        return two_state_button

    def block_buttons(self, caller_button):
        """Block buttons except caller one."""
        buttons_to_block = [button for button in self.blockable_buttons if button != caller_button]
        for button in buttons_to_block:
            button.setEnabled(False)

    def unblock_buttons(self):
        """Unblock all buttons."""
        for button in self.blockable_buttons:
            button.setEnabled(True)