from __future__ import print_function

import argparse
import json
import os
import sys

import nox
import DragonRaid_Deprecated
import Conquest
import Campaign
import Inventory
import NPC
import UpperDungeon
import DoAllDailies
import Settings
import Manager

print('Nox Macro Generator v2.1')
#print('By: cpp (Reddit: u/cpp_is_king, Discord: @cpp#0120)')
#print('Paypal: cppisking@gmail.com')
print()

if sys.version_info < (3,5):
    print('Error: This script requires Python 3.5 or higher.  Please visit '
          'www.python.org and install a newer version.')
    print('Press any key to exit...')
    input()
    sys.exit(1)

parser = argparse.ArgumentParser('Nox Macro Generator')
parser.add_argument('--enable-developer-commands', action='store_true', default=False)
args = parser.parse_args()

macro_name = None
file_path = None
desc = None

# These coordinate initial values are relative to a 1280x720 resolution, regardless of what
# your actual resolution is.
points = {
    'forge_first_item': (615, 283),
    'buy': (965, 652),
    'exit': (152, 32),
    'inventory' : (178, 644),
    'grind' : (938,629),
    'sell' : (1080,629),
    'grind_all' : (730,629),
    'grind_2' : (732,589),
    'grind_confirm' : (738,531),
    'dismiss_results' : (738,531),
    'enter_node' : (1190,629),
    'use_shop' : (636,561),
    'abandon_raid' : (848, 590),
    'start_raid' : (1183, 624),

    # x coordinate here is very precise so as to click the one unused pixel between
    # the hero's S1 and S2 abilities.
    'start_adventure' : (1055, 660),
    'stam_potion_select' : (641,379),
    'stam_potion_confirm' : (635,546),
    'confirm_insufficient_members' : (635,546),
    
    # Dailies
    # Story - Chap 8
    'ch8_conquest_naviTo_story_8_20' : (1038, 430),
    'ch8_conquest_naviTo_story_8_25' : (1268, 145),
    'ch8_conquest_naviTo_story_8_24' : (900, 395),
    'ch8_conquest_naviTo_story_8_23' : (774, 588),
    'ch8_conquest_naviTo_story_8_23_2' : (997, 150),
    # Story - Chap 7
    'ch7_conquest_naviTo_story_7_8' : (540, 460),
    # Story - Chap 6
    'ch6_conquest_naviTo_story_6_10' : (888, 499),

    # Conquests
    #Deprecated 'portal' : (703, 656),
    'conquests' : (938, 648),
    'ch2_conquest' : (439, 275),
    'ch3_conquest' : (853, 276),
    'ch4_conquest' : (441, 355),
    'ch5_conquest' : (845, 358),
    'ch6_conquest' : (449, 436),
    'ch7_conquest' : (840, 435),
    'ch8_conquest' : (449, 515),
    'move_to_conquest' : (395, 532), # precise to avoid ruby reset
    'prepare_battle' : (1189, 649),
    'get_ready_for_battle' : (955, 654),
    'auto_repeat' : (850, 664),
    'repeat_ok' : (395, 532), # precise to avoid ruby reset
    'insufficient_keys' : (395, 532), # precise to avoid ruby reset
    'x_out' : (946, 170), # precise click to avoid unselecting heroes
    'exit_conquest' : (1200, 628),
    
    # Upper Dungeon
    'upper_dungeon' : (1048, 652),
    'ch1_upper_dungeon' : (439, 275),
    'ch2_upper_dungeon' : (853, 276),
    'ch3_upper_dungeon' : (441, 355),
    'ch4_upper_dungeon' : (845, 358),
    'ch5_upper_dungeon' : (449, 436),
    'ch6_upper_dungeon' : (840, 435),
    'ch7_upper_dungeon' : (445, 520),
    'ch8_upper_dungeon' : (840, 520),
    
    # Nox background
    'nox_launchgame' : (640, 350),  # Center of screen

    # Main game screen. (i.e. not in the chapters menu)
    'main_advertisement_close' : (1268, 708),
    'main_clicknowhere' : (1268, 708),
    'main_attendance_ok' : (640, 669),
    'main_heroes' : (68, 668),
    'main_mailbox' : (1068, 30),
    'main_inventory' : (168, 668),
    'main_mission' : (278, 668),
    'main_achievements' : (378, 668),
    'main_friend' : (598, 668),
    'main_specialshop' : ("700, 668"),
    'main_portal' : (809, 668),
    'main_worldboss' : (1182, 392),
    'main_dragonraid' : (1182, 552),
    'main_preparebattle' : (1182, 655),
    'main_backbutton' : (109, 26),
    'main_leftmost_middle_position' : (100, 360),
    'main_rightmost_middle_position' : (1250, 360),
    'main_HeroList_Position1' : (150, 286),  # Exactly half icon size
    'main_HeroList_Position2' : (312, 286),
    'main_HeroList_Position3' : (470, 286),
    'main_HeroList_Position4' : (150, 600),  # This value is found through testing
    'main_HeroList_DeselectPosition' : (1132, 318),

    # Kill King's Raid
    'main_killkingsraid_top' : (1160, 90),
    'main_killkingsraid_bottom' : (1160, 629),

    # Mailbox
    'mailbox_claimall' : (950, 600),
    'mailbox_close' : (1042, 126),

    # Multi - Dragon Raid from main game screen
    'raid_multi' : (1188, 520),
    'raid_select' : (640, 600),
    'raid_select_list_top' : (560, 260),
    'raid_select_list_bottom' : (560, 620),
    'raid_select_decrementlevel' : (496, 298),
    'raid_select_gatherraiders' : (423, 380),
    'raid_select_enter' : (645, 570),
    'raid_select_fire' : (1038, 288),
    'raid_select_frost' : (1038, 450),
    'raid_select_poison' : (1038, 608),
    'raid_select_black' : (1038, 650),
    'raid_select_HeroList_Position1' : (122, 528),  # Exactly half icon size ... (13Aug2018 changed from 529 -> 528)
    'raid_select_HeroList_Position2' : (232, 528),
    'raid_select_HeroList_Position3' : (332, 528),
    'raid_select_HeroList_Position4' : (122, 640),  # This value is found through testing
    'raid_select_SetAutoRepeat' : (880, 592),
    'raid_select_StartBattle' : (1095, 650),
    'raid_select_AcceptInvitation' : (1051, 127),
    'raid_select_CloseAlreadyInvitedPopup' : (770, 130),
    'raid_select_FriendRequest' : (1190, 480),    
    'raid_select_FriendRequest_2nd' : (1190, 515),
    'raid_select_FriendRequest_SearchID' : (350, 170),
    'raid_select_FriendRequest_Find' : (575, 170),
    'raid_select_FriendRequest_Invite' : (1020, 170),
    'raid_select_FriendRequest_ClickNoWhere' : (1140, 170),
    'raid_select_FriendRequest_Close' : (1150, 73),

    # Portal (After Goto UpperDungeon Chapter 1)
    'portal_orvel' : (368, 438),
    'portal_hallofheroes' : (1050, 513),
    'portal_orvel_maysgeneralshop' : (500, 281),
    'portal_orvel_herosinn' : (790, 281),
    'portal_orvel_stockade' : (500, 360),
    'portal_orvel_arena' : (790, 360),
    'portal_orvel_forge' : (500, 430),
    'portal_orvel_orvelcastle' : (790, 430),
    'portal_orvel_guild' : (500, 512),
    'portal_orvel_centralorvel' : (790, 512),

    # Special event at Central Orvel
    'specialevent_enterdungeon' : (640, 370),

    # World Boss
    'worldboss_readyforbattle' : (918, 638),

    # Orvel Castle
    'vault_enterancient' : (630, 366),
    'vault_floor1_top' : (245, 145),
    'vault_floor2' : (245, 290),
    'vault_floor3' : (245, 435),
    'vault_floor4_bottom' : (245, 580),
    'vault_enterancient_selectlowerfloor' : (246, 520),
    'vault_enterancient_getready' : (1112, 650),

    # Arena
    'arena_select' : (636, 370),
    'arena_select_lov' : (270, 622),
    'arena_select_ready' : (982, 660),
    'arena_select_start' : (950, 660),
    'arena_select_start_retry' : (1200, 490),
    'arena_select_start_exit' : (1200, 620),

    # Arena to Stockade
    'stockade_clickfromarena' : (790, 430),

    # Stockade
    'stockade_enter' : (650, 360),
    'stockade_engage_leftmost' : (235, 650),                # Ensured that we do not accidentally click hero when we are at "Get Ready for Battle" screen
    'stockade_engage_middle_ok_autobattle' : (612, 650),
    'stockade_engage_rightmost' : (975, 650),               # Ensured that we do not accidentally click "Start Battle" when we are at "Get Ready for Battle" screen
    'stockade_engage_autobattle' : (827, 650),
    #'stockade_engage_readyforbattle' : (980, 660),
    'stockade_engage_claimskill1' : (489, 368),
    'stockade_engage_claimskill2' : (589, 368),
    'stockade_engage_claimskill3' : (689, 368),
    'stockade_engage_claimskill4' : (789, 368),
    'stockade_engage_ok' : (789, 530),
 
    # Hero's inn
    'herosinn_visit' : (632, 368),
    'herosinn_visit_greet' : (1075, 250),
    'herosinn_visit_conversate' : (1075, 350),
    'herosinn_visit_gift' : (1075, 430),
    'herosinn_visit_close' : (82, 38),
    'herosinn_visit_minigame' : (229, 452),
    'herosinn_visit_minigame_start' : (638, 423),

    # Tower of Ordeals
    'towerofordeals_enter' : (633, 563),
    'towerofordeals_back' : (120, 28),
    'towerofordeals_getreadyforbattle' : (819, 639),
    'towerofordeals_heroselect_startbattle' : (819, 670),

    # Generic points
    'getreadyforbattle_startbattle' : (1080, 660),
    'getreadyforbattle_autorepeat' : (838, 660),
    'battlecompletion_changeparty' : (81, 359),
    'battlecompletion_retry' : (1200, 492),
    'battlecompletion_exit' : (1200, 630),
    'repeatpopup_singlerepeat' : (460, 508),        # WARNING: Be careful NOT to click this button 'staminapot_ok'
    'repeatpopup_repeatbattle' : (790, 508),
    'repeatpopup_close' : (960, 165),
    'staminapot_item_centerright' : (688, 338),
    'staminapot_item_yes' : (728, 588),
    'staminapot_ok' : (759, 558),                   # 
    'minipopup_confirmbutton' : (629, 528),
    'minipopup_closebutton' : (945, 186),           # Works for "Stockade key lacking popup", "Insufficient keys to enter"
    'translucentpopup_close' : (1250, 67),          # Works for notices, minigame, close chatline
    'selectbattle_startbattle' : (475, 508),        # WARNING: Be careful NOT to click this button 'staminapot_ok'
    'selectbattle_continuousbattle' : (805, 508),
    'notice_continuousbattle_ok' : (639, 528),
    'bigicon_lowerright_top' : (1190, 385),
    'bigicon_lowerright_middle' : (1190, 518),
    'bigicon_lowerright_bottom' : (1190, 650),
    
    # Amity points
    'exchange_amity' : (678, 138),
    
    # Mission
    'mission_tab_dailymission' : (230, 108),      #1st
    'mission_tab_weeklymission' : (510, 108),     #2nd
    'mission_tab_eventmission' : (760, 108),      #3rd
    'mission_tab_raidmission' : (1045, 108),      #4th
    'mission_claim_position1' : (1068, 220),      #top
    'mission_claim_position2' : (1068, 360),      #
    'mission_claim_position3' : (1068, 490),      #
    'mission_claim_position4' : (1068, 621)       #bottom
}

rects = {
    'exit_raid' : ((1171, 596), (1233, 654)),
    'abandon_raid' : ((766, 589), (883, 641)),
    'bid_raid' : ((905, 589), (1025, 641)),
    'start_raid' : ((999, 621), (1182, 671)),
    'raid_hero_lineup' : ((125, 182), (1151, 404)),
    'raid_hero_select' : ((81, 483), (390, 683)),
    'claim_reward' : ((766, 589), (1025, 641)),
    'raid_info' : ((853, 615), (977, 680)),
    'stam_potion' : ((593,292), (686, 387)),
    'stam_potion_raid_5' : ((593,292), (675, 387)),
}



nox.initialize(points, rects, nox.find_settings_file)

def get_resolution_from_settings () :
    if nox.find_settings_file :
        nox.resolution = (Settings.Main[Settings.Main_sResolutionX],
                          Settings.Main[Settings.Main_sResolutionY])

def print_macro_details():
    global macro_name
    global file_path
    global desc

    print()
    if macro_name:
        print('Destination Macro Name: {0}'.format(macro_name))
    print('Destination File: {0}'.format(file_path))
    print('Selected Macro: {0}'.format(desc))

def conquest_plus_upper_dungeon():
    Conquest.gen_conquest()
    nox.time += 15000 # sleep for 15s in between
    UpperDungeon.gen_upper_dungeon()


try:
    Settings.SETTINGS_FILENAME = nox.select_settings_file_interactive()
    Manager.OpenLogFile()

    macro_generators = [
        #("NPC Gear Purchasing and Grinding", gen_grindhouse),
        ("Generate Default data to selected settings file", DoAllDailies.Gen_DefaultData),
        ("AFK Raid (Member)", DragonRaid_Deprecated.gen_raid),
        ("AFK Raid (Leader)", DragonRaid_Deprecated.gen_raid_leader),
        ("Story Repeat w/ Natural Stamina Regen", Campaign.gen_natural_stamina_farm),
        ("Conquests (beta)", Conquest.gen_conquest),
        ("Upper Dungeon (beta)", UpperDungeon.gen_upper_dungeon),
        ("Conquest + Upper Dungeon combo (beta)", conquest_plus_upper_dungeon),
        ("Do all dailies (Experimental)", DoAllDailies.Gen_DoAllDailies),
        ("Do DragonRaid after NOX restart", DoAllDailies.Gen_DoLaunchNOX_DragonRaid),
        ("Do Story after NOX restart", DoAllDailies.Gen_DoLaunchNOX_Story)
        ]
    if args.enable_developer_commands:
        macro_generators.extend([
            ("**DEV** Natural Stamina Regen Raid Farming (Non-Leader)", DragonRaid_Deprecated.gen_raid_experimental),
            ("**DEV** Re-enter adventure (potion)", lambda : Campaign.re_enter_adventure(True)),
            ("**DEV** Re-enter adventure (no potion)", lambda : Campaign.re_enter_adventure(False)),
        ])

    print()
    for (n,(desc,fn)) in enumerate(macro_generators):
        print('{0}) {1}'.format(n+1, desc))

    macro_number = nox.prompt_user_for_int('Enter the macro you wish to generate: ',
                                           min=1, max=len(macro_generators))
    if 1 == macro_number:
        (desc, fn) = macro_generators[macro_number - 1]
        # Generate the macro
        fn()
    else:
        (macro_name, file_path) = nox.load_macro_file()

        (desc, fn) = macro_generators[macro_number - 1]

        print_macro_details()
        # Generate the macro
        fn()

        # At this point we're back where we started and the macro can loop.
        nox.close()

        print('File {0} successfully written.'.format(file_path))

    Manager.Close()

except SystemExit:
    pass
except:
    print('Something happened.  Please report this and paste the below text.')
    import traceback
    traceback.print_exc()
    print('Press any key to exit')
    nox.do_input()