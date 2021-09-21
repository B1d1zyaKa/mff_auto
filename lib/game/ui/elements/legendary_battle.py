﻿from lib.game.ui.general import UIElement, Rect, load_ui_image

LB_LABEL = UIElement(name='LB_LABEL')
LB_LABEL.description = "Legendary battle label in mission selection."
LB_LABEL.text_rect = Rect(0.0455580865603645, 0.2935222672064777, 0.2164009111617312, 0.3390688259109312)
LB_LABEL.text = "LEGENDARY BATTLE"
LB_LABEL.text_threshold = 150

LB_STAGES = UIElement(name='LB_STAGES')
LB_STAGES.description = "DEPRECATED: Legendary battle stages text."
LB_STAGES.text_rect = Rect(0.0654897494305239, 0.7338056680161943, 0.193621867881549, 0.7591093117408907)
LB_STAGES.button_rect = Rect(0.02562642369020501, 0.3643724696356275, 0.219248291571754, 0.708502024291498)
LB_STAGES.text = "Remaining Rewards "
LB_STAGES.text_threshold = 95
LB_STAGES.available_characters = "Remaingwrds0123456789"

LB_MENU_LABEL = UIElement(name='LB_MENU_LABEL')
LB_MENU_LABEL.description = "Legendary battle label at the top left corner of LB menu."
LB_MENU_LABEL.text_rect = Rect(0.05125284738041, 0.0102429149797571, 0.2562642369020501, 0.0859109311740891)
LB_MENU_LABEL.text = "LEGENDARY BATTLE"
LB_MENU_LABEL.text_threshold = 120

LB_DIFFICULTY_NORMAL = UIElement(name='LB_DIFFICULTY_NORMAL')
LB_DIFFICULTY_NORMAL.description = "Legendary battle normal difficulty button."
LB_DIFFICULTY_NORMAL.text_rect = Rect(0.828125, 0.9027777777777778, 0.9364583333333333, 0.9685185185185186)
LB_DIFFICULTY_NORMAL.button_rect = Rect(0.828125, 0.9027777777777778, 0.9364583333333333, 0.9685185185185186)
LB_DIFFICULTY_NORMAL.text = "NORMAL"
LB_DIFFICULTY_NORMAL.text_threshold = 140

LB_DIFFICULTY_EXTREME = UIElement(name='LB_DIFFICULTY_EXTREME')
LB_DIFFICULTY_EXTREME.description = "Legendary battle extreme difficulty button."
LB_DIFFICULTY_EXTREME.text_rect = Rect(0.8317708333333333, 0.8074074074074075, 0.9244791666666666, 0.862037037037037)
LB_DIFFICULTY_EXTREME.button_rect = Rect(0.8317708333333333, 0.8074074074074075, 0.9244791666666666, 0.862037037037037)
LB_DIFFICULTY_EXTREME.text = "EXTREME"
LB_DIFFICULTY_EXTREME.text_threshold = 100

LB_BATTLE_STAGE_1 = UIElement(name='LB_BATTLE_STAGE_1')
LB_BATTLE_STAGE_1.description = "LB stage #1."
LB_BATTLE_STAGE_1.text_rect = Rect(0.1195899772209567, 0.7591093117408907, 0.1879271070615034, 0.7995951417004049)
LB_BATTLE_STAGE_1.button_rect = Rect(0.05808656036446469, 0.7439271255060729, 0.24658314350797267, 0.8097165991902834)
LB_BATTLE_STAGE_1.text = "ENTER"
LB_BATTLE_STAGE_1.text_threshold = 120

LB_BATTLE_STAGE_2 = UIElement(name='LB_BATTLE_STAGE_2')
LB_BATTLE_STAGE_2.description = "LB stage #2."
LB_BATTLE_STAGE_2.text_rect = Rect(0.40989583333333335, 0.7472222222222222, 0.48333333333333334, 0.8055555555555556)
LB_BATTLE_STAGE_2.button_rect = Rect(0.40989583333333335, 0.7472222222222222, 0.48333333333333334, 0.8055555555555556)
LB_BATTLE_STAGE_2.text = "ENTER"
LB_BATTLE_STAGE_2.text_threshold = 120

LB_BATTLE_STAGE_3 = UIElement(name='LB_BATTLE_STAGE_3')
LB_BATTLE_STAGE_3.description = "LB stage #3."
LB_BATTLE_STAGE_3.text_rect = Rect(0.7015625, 0.7472222222222222, 0.7802083333333333, 0.8055555555555556)
LB_BATTLE_STAGE_3.button_rect = Rect(0.7015625, 0.7472222222222222, 0.7802083333333333, 0.8055555555555556)
LB_BATTLE_STAGE_3.text = "ENTER"
LB_BATTLE_STAGE_3.text_threshold = 120

LB_START_BUTTON = UIElement(name='LB_START_BUTTON')
LB_START_BUTTON.description = "LB start button."
LB_START_BUTTON.text_rect = Rect(0.7972665148063781, 0.8906882591093117, 0.8826879271070615, 0.9412955465587045)
LB_START_BUTTON.button_rect = Rect(0.729498861047836, 0.881578947368421, 0.9567198177676538, 0.951417004048583)
LB_START_BUTTON.text = "START"
LB_START_BUTTON.text_threshold = 150

LB_IGNORE_NOTICE = UIElement(name='LB_IGNORE_NOTICE')
LB_IGNORE_NOTICE.description = "Ignore notification if you don't have character or costume."
LB_IGNORE_NOTICE.text_rect = Rect(0.5723234624145785, 0.7753036437246964, 0.6520501138952164, 0.8289473684210527)
LB_IGNORE_NOTICE.button_rect = Rect(0.5489749430523918, 0.7672064777327935, 0.6890660592255126, 0.8370445344129555)
LB_IGNORE_NOTICE.text = "IGNORE"
LB_IGNORE_NOTICE.text_threshold = 175

LB_REPEAT_BUTTON = UIElement(name='LB_REPEAT_BUTTON')
LB_REPEAT_BUTTON.description = "LB repeat button."
LB_REPEAT_BUTTON.button_rect = Rect(0.6896355353075171, 0.8987854251012146, 0.8052391799544419, 0.9615384615384616)

LB_HOME_BUTTON = UIElement(name='LB_HOME_BUTTON')
LB_HOME_BUTTON.description = "LB home button."
LB_HOME_BUTTON.button_rect = Rect(0.5535307517084282, 0.8997975708502024, 0.6594533029612756, 0.9615384615384616)

LB_DRAG_FROM = UIElement(name='LB_DRAG_FROM')
LB_DRAG_FROM.description = "LB: drag position (bottom) to scroll the list."
LB_DRAG_FROM.button_rect = Rect(0.1, 0.950925925925926, 0.12239583333333333, 0.9842592592592593)

LB_DRAG_TO = UIElement(name='LB_DRAG_TO')
LB_DRAG_TO.description = "LB: drag position (top) to scroll the list."
LB_DRAG_TO.button_rect = Rect(0.1, 0.10555555555555556, 0.12239583333333333, 0.14166666666666666)

LB_RAGNAROK_BATTLE = UIElement(name='LB_RAGNAROK_BATTLE')
LB_RAGNAROK_BATTLE.description = "Legendary battle : Ragnarok."
LB_RAGNAROK_BATTLE.text_rect = Rect(0.009984967427233352, 0.950978635356834, 0.20738224773137132, 0.9881983245724288)
LB_RAGNAROK_BATTLE.button_rect = Rect(0.036155061406948616, 0.8153926246428804, 0.1834553046642031, 0.9323687907490363)
LB_RAGNAROK_BATTLE.text = "MARVEL STUDIOS' THOR:RAGNAROK"
LB_RAGNAROK_BATTLE.text_threshold = 90

LB_RAGNAROK_BATTLE_TITLE = UIElement(name='LB_RAGNAROK_BATTLE_TITLE')
LB_RAGNAROK_BATTLE_TITLE.description = "Legendary battle : Ragnarok (title on top)."
LB_RAGNAROK_BATTLE_TITLE.text_rect = Rect(0.23385416666666667, 0.1259259259259259, 0.38177083333333334, 0.18518518518518517)
LB_RAGNAROK_BATTLE_TITLE.text = "RAGNAROK"
LB_RAGNAROK_BATTLE_TITLE.text_threshold = 130
LB_RAGNAROK_BATTLE_TITLE.available_characters = "RAGNAROK"

LB_NO_REWARD_NOTICE = UIElement(name='LB_NO_REWARD_NOTICE')
LB_NO_REWARD_NOTICE.description = "Legendary battle : no rewards notification before entering the battle."
LB_NO_REWARD_NOTICE.text_rect = Rect(0.5557291666666667, 0.7277777777777777, 0.6010416666666667, 0.7842592592592592)
LB_NO_REWARD_NOTICE.button_rect = Rect(0.5557291666666667, 0.7277777777777777, 0.6010416666666667, 0.7842592592592592)
LB_NO_REWARD_NOTICE.text = "OK"
LB_NO_REWARD_NOTICE.text_threshold = 150
LB_NO_REWARD_NOTICE.available_characters = "OK"

LB_CAPTAIN_MARVEL_BATTLE = UIElement(name='LB_CAPTAIN_MARVEL_BATTLE')
LB_CAPTAIN_MARVEL_BATTLE.description = "Legendary battle : Captain Marvel."
LB_CAPTAIN_MARVEL_BATTLE.text_rect = Rect(0.01222811833978037, 0.10821852954657461, 0.20663453076052232, 0.14410894414732692)
LB_CAPTAIN_MARVEL_BATTLE.button_rect = Rect(0.01222811833978037, 0.10821852954657461, 0.20663453076052232, 0.14410894414732692)
LB_CAPTAIN_MARVEL_BATTLE.text = "MARVEL STUDIOS' CAPTAIN MARVEL"
LB_CAPTAIN_MARVEL_BATTLE.text_threshold = 90

LB_CAPTAIN_MARVEL_BATTLE_TITLE = UIElement(name='LB_CAPTAIN_MARVEL_BATTLE_TITLE')
LB_CAPTAIN_MARVEL_BATTLE_TITLE.description = "Legendary battle : Captain Marvel 'New Hope' (title on top)."
LB_CAPTAIN_MARVEL_BATTLE_TITLE.text_rect = Rect(0.22916666666666666, 0.12037037037037036, 0.37395833333333334, 0.18888888888888888)
LB_CAPTAIN_MARVEL_BATTLE_TITLE.text = "NEW HOPE"
LB_CAPTAIN_MARVEL_BATTLE_TITLE.text_threshold = 130
LB_CAPTAIN_MARVEL_BATTLE_TITLE.available_characters = "NEW HOPE"

LB_EXTREME_UPGRADE = UIElement(name='LB_EXTREME_UPGRADE')
LB_EXTREME_UPGRADE.description = "Legendary battle : UPGRADE notification when EXTREME battle wasn't purchased. Leads to X close."
LB_EXTREME_UPGRADE.text_rect = Rect(0.6447966756780406, 0.7954535054202402, 0.7935923528769931, 0.8659050600069023)
LB_EXTREME_UPGRADE.button_rect = Rect(0.8474279747781217, 0.10821852954657461, 0.878084370582931, 0.16936516182933778)
LB_EXTREME_UPGRADE.text = "UPGRADE"
LB_EXTREME_UPGRADE.text_threshold = 150

LB_BLACK_PANTHER_BATTLE = UIElement(name='LB_BLACK_PANTHER_BATTLE')
LB_BLACK_PANTHER_BATTLE.description = "Legendary battle : Black Panther."
LB_BLACK_PANTHER_BATTLE.text_rect = Rect(0.03166875958185458, 0.7396239715968477, 0.1834553046642031, 0.7808314846569708)
LB_BLACK_PANTHER_BATTLE.button_rect = Rect(0.04961396688223072, 0.6027086862680516, 0.17074411615976992, 0.7343068731374771)
LB_BLACK_PANTHER_BATTLE.text = "MARVEL'S BLACK PANTHER"
LB_BLACK_PANTHER_BATTLE.text_threshold = 90

LB_BLACK_PANTHER_BATTLE_TITLE = UIElement(name='LB_BLACK_PANTHER_BATTLE_TITLE')
LB_BLACK_PANTHER_BATTLE_TITLE.description = "Legendary battle : Black Panther 'Wakanda Forever' (title on top)."
LB_BLACK_PANTHER_BATTLE_TITLE.text_rect = Rect(0.23125, 0.1175925925925926, 0.4864583333333333, 0.18611111111111112)
LB_BLACK_PANTHER_BATTLE_TITLE.text = "WAKANDA FOREVER"
LB_BLACK_PANTHER_BATTLE_TITLE.text_threshold = 130
LB_BLACK_PANTHER_BATTLE_TITLE.available_characters = "WAKANDA FOREVER"

LB_INFINITY_WAR_BATTLE = UIElement(name='LB_INFINITY_WAR_BATTLE')
LB_INFINITY_WAR_BATTLE.description = "Legendary battle : Infinity War."
LB_INFINITY_WAR_BATTLE.text_rect = Rect(0.01222811833978037, 0.5309278570665469, 0.20513909681882428, 0.5654889970524566)
LB_INFINITY_WAR_BATTLE.button_rect = Rect(0.04587538202798568, 0.3953418463525935, 0.17298726707231699, 0.5043423647696932)
LB_INFINITY_WAR_BATTLE.text = "MARVEL STUDIOS' AVENGERS: INFINITY WAR"
LB_INFINITY_WAR_BATTLE.text_threshold = 90

LB_INFINITY_WAR_BATTLE_TITLE = UIElement(name='LB_INFINITY_WAR_BATTLE_TITLE')
LB_INFINITY_WAR_BATTLE_TITLE.description = "Legendary battle : Infinity War 'Pending Danger' (title on top)."
LB_INFINITY_WAR_BATTLE_TITLE.text_rect = Rect(0.2296875, 0.12314814814814815, 0.4578125, 0.18703703703703703)
LB_INFINITY_WAR_BATTLE_TITLE.text = "PENDING DANGER"
LB_INFINITY_WAR_BATTLE_TITLE.text_threshold = 130
LB_INFINITY_WAR_BATTLE_TITLE.available_characters = "PENDING DANGER"

LB_ANT_MAN_BATTLE = UIElement(name='LB_ANT_MAN_BATTLE')
LB_ANT_MAN_BATTLE.description = "Legendary battle : Ant-Man And The Wasp."
LB_ANT_MAN_BATTLE.text_rect = Rect(0.012975835310629366, 0.32356101715108876, 0.20364366287712626, 0.35413433329247046)
LB_ANT_MAN_BATTLE.button_rect = Rect(0.04587538202798568, 0.1879750064371354, 0.16850096524722294, 0.3022926233136059)
LB_ANT_MAN_BATTLE.text = "MARVEL STUDIOS' ANT-MAN AND THE WASP"
LB_ANT_MAN_BATTLE.text_threshold = 90

LB_ANT_MAN_BATTLE_TITLE = UIElement(name='LB_ANT_MAN_BATTLE_TITLE')
LB_ANT_MAN_BATTLE_TITLE.description = "Legendary battle : Ant-Man And The Wasp 'Invisible Ghost' (title on top)."
LB_ANT_MAN_BATTLE_TITLE.text_rect = Rect(0.23020833333333332, 0.1259259259259259, 0.44635416666666666, 0.18333333333333332)
LB_ANT_MAN_BATTLE_TITLE.text = "INVISIBLE GHOST"
LB_ANT_MAN_BATTLE_TITLE.text_threshold = 130
LB_ANT_MAN_BATTLE_TITLE.available_characters = "INVISIBLE GHOST"