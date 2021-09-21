﻿from lib.game.ui.general import UIElement, Rect, load_ui_image

ENERGY_COST = UIElement(name='ENERGY_COST')
ENERGY_COST.description = "Energy cost of staging the mission."
ENERGY_COST.text_rect = Rect(0.9138564920273349, 0.9109311740890689, 0.9396355353075171, 0.951417004048583)
ENERGY_COST.text_threshold = 145
ENERGY_COST.available_characters = "-0123456789"

BOOST_COST = UIElement(name='BOOST_COST')
BOOST_COST.description = "Boost cost of staging the mission."
BOOST_COST.text_rect = Rect(0.783876993166287, 0.8704453441295547, 0.8086560364464692, 0.9101311740890689)
BOOST_COST.text_threshold = 225
BOOST_COST.available_characters = "0123456789-"

START_BUTTON = UIElement(name='START_BUTTON')
START_BUTTON.description = "The mission start button."
START_BUTTON.text_rect = Rect(0.8339690693028394, 0.8991369253779693, 0.9304245585423615, 0.9602835576607327)
START_BUTTON.button_rect = Rect(0.8339690693028394, 0.8991369253779693, 0.9304245585423615, 0.9602835576607327)
START_BUTTON.text = "START"
START_BUTTON.text_threshold = 150

REPEAT_BUTTON = UIElement(name='REPEAT_BUTTON')
REPEAT_BUTTON.description = "The mission repeat button."
REPEAT_BUTTON.button_rect = Rect(0.8942708333333333, 0.8944444444444445, 0.9354166666666667, 0.9601851851851851)

HOME_BUTTON = UIElement(name='HOME_BUTTON')
HOME_BUTTON.description = "The mission home button (middle position)."
HOME_BUTTON.image_rect = Rect(0.7515625, 0.8953703703703704, 0.8015625, 0.9648148148148148)
HOME_BUTTON.button_rect = Rect(0.7515625, 0.8953703703703704, 0.8015625, 0.9648148148148148)
HOME_BUTTON.image_threshold = 0.7
HOME_BUTTON.image = load_ui_image("home_button.png")

HOME_BUTTON_POSITION_2 = UIElement(name='HOME_BUTTON_POSITION_2')
HOME_BUTTON_POSITION_2.description = "The mission home button. (left position)."
HOME_BUTTON_POSITION_2.image_rect = Rect(0.6109375, 0.8944444444444445, 0.6604166666666667, 0.9638888888888889)
HOME_BUTTON_POSITION_2.button_rect = Rect(0.6109375, 0.8944444444444445, 0.6604166666666667, 0.9638888888888889)
HOME_BUTTON_POSITION_2.image_threshold = 0.7
HOME_BUTTON_POSITION_2.image = load_ui_image("home_button.png")

HOME_BUTTON_POSITION_3 = UIElement(name='HOME_BUTTON_POSITION_3')
HOME_BUTTON_POSITION_3.description = "The mission home button. (right position)."
HOME_BUTTON_POSITION_3.image_rect = Rect(0.8927083333333333, 0.8944444444444445, 0.9427083333333334, 0.9638888888888889)
HOME_BUTTON_POSITION_3.button_rect = Rect(0.8927083333333333, 0.8944444444444445, 0.9427083333333334, 0.9638888888888889)
HOME_BUTTON_POSITION_3.image_threshold = 0.7
HOME_BUTTON_POSITION_3.image = load_ui_image("home_button.png")

LVL_UP_NOTIFICATION = UIElement(name='LVL_UP_NOTIFICATION')
LVL_UP_NOTIFICATION.description = "LVL up notification after end of the mission."
LVL_UP_NOTIFICATION.text_rect = Rect(0.47955122512041004, 0.8978076507631267, 0.5214233754879544, 0.950978635356834)
LVL_UP_NOTIFICATION.button_rect = Rect(0.47955122512041004, 0.8978076507631267, 0.5214233754879544, 0.950978635356834)
LVL_UP_NOTIFICATION.text = "OK"
LVL_UP_NOTIFICATION.text_threshold = 150
LVL_UP_NOTIFICATION.available_characters = "OK"

STAGES_DONE_NOTIFICATION = UIElement(name='STAGES_DONE_NOTIFICATION')
STAGES_DONE_NOTIFICATION.description = "All stages done notification."
STAGES_DONE_NOTIFICATION.text_rect = Rect(0.484624145785877, 0.7327935222672065, 0.5199316628701595, 0.7773279352226721)
STAGES_DONE_NOTIFICATION.button_rect = Rect(0.44248291571753984, 0.7277327935222672, 0.5615034168564921, 0.7844129554655871)
STAGES_DONE_NOTIFICATION.text = "OK"
STAGES_DONE_NOTIFICATION.text_threshold = 150
STAGES_DONE_NOTIFICATION.available_characters = "OK"

RANK_UP_NOTIFICATION_1 = UIElement(name='RANK_UP_NOTIFICATION_1')
RANK_UP_NOTIFICATION_1.description = "Rank up notification."
RANK_UP_NOTIFICATION_1.text_rect = Rect(0.3080714725816389, 0.8629385964912281, 0.381392483056069, 0.9067982456140351)
RANK_UP_NOTIFICATION_1.button_rect = Rect(0.2932840418977203, 0.8574561403508771, 0.3961799137399877, 0.9122807017543859)
RANK_UP_NOTIFICATION_1.text = "CANCEL"
RANK_UP_NOTIFICATION_1.text_threshold = 150

RANK_UP_NOTIFICATION_2 = UIElement(name='RANK_UP_NOTIFICATION_2')
RANK_UP_NOTIFICATION_2.description = "Rank up notification with rank's count bar."
RANK_UP_NOTIFICATION_2.text_rect = Rect(0.30572916666666666, 0.8981481481481481, 0.3854166666666667, 0.9555555555555556)
RANK_UP_NOTIFICATION_2.button_rect = Rect(0.30572916666666666, 0.8981481481481481, 0.3854166666666667, 0.9555555555555556)
RANK_UP_NOTIFICATION_2.text = "CANCEL"
RANK_UP_NOTIFICATION_2.text_threshold = 150

TAP_TO_CONTINUE = UIElement(name='TAP_TO_CONTINUE')
TAP_TO_CONTINUE.description = "Tap to continue notification when you see new item description."
TAP_TO_CONTINUE.text_rect = Rect(0.8755208333333333, 0.95, 0.9927083333333333, 0.9907407407407407)
TAP_TO_CONTINUE.button_rect = Rect(0.8755208333333333, 0.95, 0.9927083333333333, 0.9907407407407407)
TAP_TO_CONTINUE.text = "Tap to continue."
TAP_TO_CONTINUE.text_threshold = 150

SHIELD_LVL_UP_NOTIFICATION = UIElement(name='SHIELD_LVL_UP_NOTIFICATION')
SHIELD_LVL_UP_NOTIFICATION.description = "SHIELD LVL up notification."
SHIELD_LVL_UP_NOTIFICATION.text_rect = Rect(0.47656035723701395, 0.7196848523742075, 0.5266573942838976, 0.7808314846569708)
SHIELD_LVL_UP_NOTIFICATION.button_rect = Rect(0.47656035723701395, 0.7196848523742075, 0.5266573942838976, 0.7808314846569708)
SHIELD_LVL_UP_NOTIFICATION.text = "OK"
SHIELD_LVL_UP_NOTIFICATION.text_threshold = 150
SHIELD_LVL_UP_NOTIFICATION.available_characters = "OK"

RECRUIT_CHARACTER_NOTIFICATION = UIElement(name='RECRUIT_CHARACTER_NOTIFICATION')
RECRUIT_CHARACTER_NOTIFICATION.description = "Recruit character notification."
RECRUIT_CHARACTER_NOTIFICATION.text_rect = Rect(0.36666666666666664, 0.7444444444444445, 0.4817708333333333, 0.8)
RECRUIT_CHARACTER_NOTIFICATION.button_rect = Rect(0.36666666666666664, 0.7444444444444445, 0.4817708333333333, 0.8)
RECRUIT_CHARACTER_NOTIFICATION.text = "CANCEL"
RECRUIT_CHARACTER_NOTIFICATION.text_threshold = 150

ALLY_APPEARED = UIElement(name='ALLY_APPEARED')
ALLY_APPEARED.description = "When ally from another dimension appears you can see this message."
ALLY_APPEARED.text_rect = Rect(0.2796875, 0.2898148148148148, 0.7177083333333333, 0.3712962962962963)
ALLY_APPEARED.text = "An Ally Shifter Appeared!"
ALLY_APPEARED.text_threshold = 120

ENEMY_APPEARED = UIElement(name='ENEMY_APPEARED')
ENEMY_APPEARED.description = "When enemy from another dimension appears you can see this message."
ENEMY_APPEARED.text_rect = Rect(0.2796875, 0.2898148148148148, 0.7177083333333333, 0.3712962962962963)
ENEMY_APPEARED.text = "An Enemy Shifter Appeared!"
ENEMY_APPEARED.text_threshold = 80

ALLY_AND_ENEMY_APPEARED = UIElement(name='ALLY_AND_ENEMY_APPEARED')
ALLY_AND_ENEMY_APPEARED.description = "When enemy and ally from another dimension appears you can see this message (ally on top)."
ALLY_AND_ENEMY_APPEARED.text_rect = Rect(0.3, 0.06574074074074074, 0.6994791666666667, 0.14629629629629629)
ALLY_AND_ENEMY_APPEARED.text = "An Ally Shifter Appeared!"
ALLY_AND_ENEMY_APPEARED.text_threshold = 120

ENEMY_AND_ALLY_APPEARED = UIElement(name='ENEMY_AND_ALLY_APPEARED')
ENEMY_AND_ALLY_APPEARED.description = "When enemy and ally from another dimension appears you can see this message (enemy on bottom)."
ENEMY_AND_ALLY_APPEARED.text_rect = Rect(0.278125, 0.5194444444444445, 0.7192708333333333, 0.6037037037037037)
ENEMY_AND_ALLY_APPEARED.text = "An Enemy Shifter Appeared!"
ENEMY_AND_ALLY_APPEARED.text_threshold = 80

REPEAT_BUTTON_IMAGE_POSITION_1 = UIElement(name='REPEAT_BUTTON_IMAGE_POSITION_1')
REPEAT_BUTTON_IMAGE_POSITION_1.description = "An image of Repeat Mission button (position 1)."
REPEAT_BUTTON_IMAGE_POSITION_1.image_rect = Rect(0.7536458333333333, 0.8944444444444445, 0.7953125, 0.9601851851851851)
REPEAT_BUTTON_IMAGE_POSITION_1.button_rect = Rect(0.7536458333333333, 0.8944444444444445, 0.7953125, 0.9601851851851851)
REPEAT_BUTTON_IMAGE_POSITION_1.image_threshold = 0.7
REPEAT_BUTTON_IMAGE_POSITION_1.image = load_ui_image("repeat_button.png")

REPEAT_BUTTON_IMAGE_POSITION_2 = UIElement(name='REPEAT_BUTTON_IMAGE_POSITION_2')
REPEAT_BUTTON_IMAGE_POSITION_2.description = "An image of Repeat Mission button (position 2)."
REPEAT_BUTTON_IMAGE_POSITION_2.image_rect = Rect(0.8942708333333333, 0.8944444444444445, 0.9354166666666667, 0.9601851851851851)
REPEAT_BUTTON_IMAGE_POSITION_2.button_rect = Rect(0.8942708333333333, 0.8944444444444445, 0.9354166666666667, 0.9601851851851851)
REPEAT_BUTTON_IMAGE_POSITION_2.image_threshold = 0.7
REPEAT_BUTTON_IMAGE_POSITION_2.image = load_ui_image("repeat_button.png")

SELECT_TEAM_1 = UIElement(name='SELECT_TEAM_1')
SELECT_TEAM_1.description = "Team selector is first team."
SELECT_TEAM_1.button_rect = Rect(0.5247323245827398, 0.14940560768948358, 0.5457618643878682, 0.180761480660571)

SELECT_TEAM_2 = UIElement(name='SELECT_TEAM_2')
SELECT_TEAM_2.description = "Team selector is second team."
SELECT_TEAM_2.button_rect = Rect(0.6017275751595806, 0.14819961257521103, 0.6214003704611524, 0.1813644782177073)

SELECT_TEAM_3 = UIElement(name='SELECT_TEAM_3')
SELECT_TEAM_3.description = "Team selector is third team."
SELECT_TEAM_3.button_rect = Rect(0.6790620118623107, 0.14819961257521103, 0.6966996904085474, 0.1795554855462984)

SELECT_TEAM_4 = UIElement(name='SELECT_TEAM_4')
SELECT_TEAM_4.description = "Team selector is fourth team."
SELECT_TEAM_4.button_rect = Rect(0.7547005179355949, 0.14819961257521103, 0.775051685488945, 0.1789524879891621)

SELECT_TEAM_5 = UIElement(name='SELECT_TEAM_5')
SELECT_TEAM_5.description = "Team selector is fifth team."
SELECT_TEAM_5.button_rect = Rect(0.830339024008879, 0.14880261013234727, 0.8506901915622291, 0.1813644782177073)

DIFFICULTY_STAGE_1 = UIElement(name='DIFFICULTY_STAGE_1')
DIFFICULTY_STAGE_1.description = "Difficulty of the mission: #1."
DIFFICULTY_STAGE_1.text_rect = Rect(0.7053617503168103, 0.27703640563159493, 0.775647145576617, 0.3341952140698302)
DIFFICULTY_STAGE_1.button_rect = Rect(0.7053617503168103, 0.27703640563159493, 0.775647145576617, 0.3341952140698302)
DIFFICULTY_STAGE_1.text = "ENTER"
DIFFICULTY_STAGE_1.text_threshold = 150

DIFFICULTY_STAGE_2 = UIElement(name='DIFFICULTY_STAGE_2')
DIFFICULTY_STAGE_2.description = "Difficulty of the mission: #2."
DIFFICULTY_STAGE_2.text_rect = Rect(0.7053617503168103, 0.41661024019007636, 0.774899428605768, 0.4750983232431543)
DIFFICULTY_STAGE_2.button_rect = Rect(0.7053617503168103, 0.41661024019007636, 0.774899428605768, 0.4750983232431543)
DIFFICULTY_STAGE_2.text = "ENTER"
DIFFICULTY_STAGE_2.text_threshold = 150

DIFFICULTY_STAGE_3 = UIElement(name='DIFFICULTY_STAGE_3')
DIFFICULTY_STAGE_3.description = "Difficulty of the mission: #3."
DIFFICULTY_STAGE_3.text_rect = Rect(0.7046140333459613, 0.5615011732079285, 0.774151711634919, 0.6133428831867931)
DIFFICULTY_STAGE_3.button_rect = Rect(0.7046140333459613, 0.5615011732079285, 0.774151711634919, 0.6133428831867931)
DIFFICULTY_STAGE_3.text = "ENTER"
DIFFICULTY_STAGE_3.text_threshold = 150

DIFFICULTY_STAGE_4 = UIElement(name='DIFFICULTY_STAGE_4')
DIFFICULTY_STAGE_4.description = "Difficulty of the mission: #4."
DIFFICULTY_STAGE_4.text_rect = Rect(0.7038663163751122, 0.6239770801055345, 0.7748994286057678, 0.6705016916250284)
DIFFICULTY_STAGE_4.button_rect = Rect(0.7038663163751122, 0.6239770801055345, 0.7748994286057678, 0.6705016916250284)
DIFFICULTY_STAGE_4.text = "ENTER"
DIFFICULTY_STAGE_4.text_threshold = 150

DIFFICULTY_STAGE_2_4 = UIElement(name='DIFFICULTY_STAGE_2_4')
DIFFICULTY_STAGE_2_4.description = "Difficulty of the mission: #4 from the bottom of the screen."
DIFFICULTY_STAGE_2_4.text_rect = Rect(0.6956414296957731, 0.34350013637372895, 0.7793857304308621, 0.3966711209674362)
DIFFICULTY_STAGE_2_4.button_rect = Rect(0.6956414296957731, 0.34350013637372895, 0.7793857304308621, 0.3966711209674362)
DIFFICULTY_STAGE_2_4.text = "ENTER"
DIFFICULTY_STAGE_2_4.text_threshold = 150

DIFFICULTY_STAGE_2_5 = UIElement(name='DIFFICULTY_STAGE_2_5')
DIFFICULTY_STAGE_2_5.description = "Difficulty of the mission: #5 from the bottom of the screen."
DIFFICULTY_STAGE_2_5.text_rect = Rect(0.6986322975791691, 0.48706179477673844, 0.7786380134600129, 0.534915680911075)
DIFFICULTY_STAGE_2_5.button_rect = Rect(0.6986322975791691, 0.48706179477673844, 0.7786380134600129, 0.534915680911075)
DIFFICULTY_STAGE_2_5.text = "ENTER"
DIFFICULTY_STAGE_2_5.text_threshold = 150

DIFFICULTY_STAGE_2_6 = UIElement(name='DIFFICULTY_STAGE_2_6')
DIFFICULTY_STAGE_2_6.description = "Difficulty of the mission: #6 from the bottom of the screen."
DIFFICULTY_STAGE_2_6.text_rect = Rect(0.6978845806083203, 0.6239770801055345, 0.7793857304308619, 0.6771480646992417)
DIFFICULTY_STAGE_2_6.button_rect = Rect(0.6978845806083203, 0.6239770801055345, 0.7793857304308619, 0.6771480646992417)
DIFFICULTY_STAGE_2_6.text = "ENTER"
DIFFICULTY_STAGE_2_6.text_threshold = 150

DIFFICULTY_DRAG_FROM = UIElement(name='DIFFICULTY_DRAG_FROM')
DIFFICULTY_DRAG_FROM.description = "Difficulty of the mission: drag position (bottom) to scroll the list."
DIFFICULTY_DRAG_FROM.button_rect = Rect(0.4645968857034299, 0.6319527277945906, 0.6694713357160579, 0.7063921062257806)

DIFFICULTY_DRAG_TO = UIElement(name='DIFFICULTY_DRAG_TO')
DIFFICULTY_DRAG_TO.description = "Difficulty of the mission: drag position (top) to scroll the list."
DIFFICULTY_DRAG_TO.button_rect = Rect(0.4578674329657889, 0.24779236410505603, 0.666480467832662, 0.31824391869171803)

SKIP_CUTSCENE = UIElement(name='SKIP_CUTSCENE')
SKIP_CUTSCENE.description = "SKIP button when you see cutscene."
SKIP_CUTSCENE.text_rect = Rect(0.8735980687578369, 0.040425524189597835, 0.9341631433966064, 0.09758433262783313)
SKIP_CUTSCENE.button_rect = Rect(0.8735980687578369, 0.040425524189597835, 0.9341631433966064, 0.09758433262783313)
SKIP_CUTSCENE.text = "SKIP"
SKIP_CUTSCENE.text_threshold = 130

SKIP_TAP_THE_SCREEN = UIElement(name='SKIP_TAP_THE_SCREEN')
SKIP_TAP_THE_SCREEN.description = "TAP THE SCREEN button when you see cutscene of fighting the enemy."
SKIP_TAP_THE_SCREEN.text_rect = Rect(0.7895833333333333, 0.9111111111111111, 0.9296875, 0.9518518518518518)
SKIP_TAP_THE_SCREEN.button_rect = Rect(0.7895833333333333, 0.9111111111111111, 0.9296875, 0.9518518518518518)
SKIP_TAP_THE_SCREEN.text = "TAP THE SCREEN"
SKIP_TAP_THE_SCREEN.text_threshold = 130

ITEM_MAX_LIMIT_NOTIFICATION = UIElement(name='ITEM_MAX_LIMIT_NOTIFICATION')
ITEM_MAX_LIMIT_NOTIFICATION.description = "Notification when one of your items has reached its max limit."
ITEM_MAX_LIMIT_NOTIFICATION.text_rect = Rect(0.33374641580485354, 0.40464676865649224, 0.6649850338909639, 0.4578177532501994)
ITEM_MAX_LIMIT_NOTIFICATION.button_rect = Rect(0.5565660731178578, 0.7117092046851513, 0.6014290913687982, 0.7728558369679147)
ITEM_MAX_LIMIT_NOTIFICATION.text = "One of your items has reached its max limit."
ITEM_MAX_LIMIT_NOTIFICATION.text_threshold = 120

WAITING_FOR_OTHER_PLAYERS = UIElement(name='WAITING_FOR_OTHER_PLAYERS')
WAITING_FOR_OTHER_PLAYERS.description = "Waiting for players before boss fight."
WAITING_FOR_OTHER_PLAYERS.text_rect = Rect(0.378125, 0.3, 0.6244791666666667, 0.35555555555555557)
WAITING_FOR_OTHER_PLAYERS.button_rect = Rect(0.46041666666666664, 0.7027777777777777, 0.5390625, 0.7537037037037037)
WAITING_FOR_OTHER_PLAYERS.text = "Waiting for other players."
WAITING_FOR_OTHER_PLAYERS.text_threshold = 120

NOT_ENOUGH_ENERGY = UIElement(name='NOT_ENOUGH_ENERGY')
NOT_ENOUGH_ENERGY.description = "Not enough energy notification, refers to CANCEL button."
NOT_ENOUGH_ENERGY.text_rect = Rect(0.4204815844233385, 0.4471835563314581, 0.580493016185026, 0.5043423647696933)
NOT_ENOUGH_ENERGY.button_rect = Rect(0.3793571510266431, 0.7130384792999941, 0.4638491687325808, 0.7755143861976)
NOT_ENOUGH_ENERGY.text = "Not enough Energy."
NOT_ENOUGH_ENERGY.text_threshold = 140

INVENTORY_FULL = UIElement(name='INVENTORY_FULL')
INVENTORY_FULL.description = "Inventory full notification, refers to CANCEL button."
INVENTORY_FULL.text_rect = Rect(0.3060808878834403, 0.46978122478378354, 0.6911551278706791, 0.5242814839923333)
INVENTORY_FULL.button_rect = Rect(0.38234801891003906, 0.7130384792999941, 0.4601105838783358, 0.7755143861976)
INVENTORY_FULL.text = "Your inventory is full. Go to Inventory and expand?"
INVENTORY_FULL.text_threshold = 140