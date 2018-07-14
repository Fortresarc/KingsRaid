from __future__ import print_function

import argparse
import json
import os
import sys

import nox
import DragonRaid
import Conquest
import Campaign
import Inventory
import NPC
import UpperDungeon
import DoAllDailies

print('Nox Macro Generator v2.1')
print('By: cpp (Reddit: u/cpp_is_king, Discord: @cpp#0120)')
print('Paypal: cppisking@gmail.com')
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
	'grind' : (839,629),
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
	# Conquests
	'portal' : (703, 656),
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
    'main_friend' : (488, 668),
    'main_specialshop' : ("598, 668"),
    'main_portal' : (700, 668),
    'main_worldboss' : (1182, 392),
    'main_dragonraid' : (1182, 552),
    'main_preparebattle' : (1182, 655),
    'main_backbutton' : (109, 26),
    'main_leftmost_middle_position' : (100, 360),
    'main_rightmost_middle_position' : (1250, 360),

    # Mailbox
    'mailbox_claimall' : (950, 600),
    'mailbox_close' : (1042, 126),

    # Portal (After Goto UpperDungeon Chapter 1)
    'portal_orvel' : (368, 438),
    'portal_orvel_maysgeneralshop' : (500, 281),
    'portal_orvel_herosinn' : (790, 281),
    'portal_orvel_stockade' : (500, 360),
    'portal_orvel_arena' : (790, 360),
    'portal_orvel_forge' : (500, 430),
    'portal_orvel_orvelcastle' : (790, 430),
    'portal_orvel_guild' : (500, 512),

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
    'stockade_engage_leftmost' : (225, 650),
    'stockade_engage_middle_ok_autobattle' : (756, 650),
    'stockade_engage_rightmost' : (980, 650),
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

    # All pop ups
    'minipopup_confirmbutton' : (629, 528),
    'minipopup_closebutton' : (945, 186),   # Works for "Stockade key lacking popup", "Insufficient keys to enter"
    'translucentpopup_close' : (1250, 67),  #Works for notices, minigame, close chatline
    
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



nox.initialize(points, rects)

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
	macro_generators = [
		#("NPC Gear Purchasing and Grinding", gen_grindhouse),
		("AFK Raid (Member)", DragonRaid.gen_raid),
		("AFK Raid (Leader)", DragonRaid.gen_raid_leader),
		("Story Repeat w/ Natural Stamina Regen", Campaign.gen_natural_stamina_farm),
		("Conquests (beta)", Conquest.gen_conquest),
		("Upper Dungeon (beta)", UpperDungeon.gen_upper_dungeon),
		("Conquest + Upper Dungeon combo (beta)", conquest_plus_upper_dungeon),
        ("Do all dailies (Experimental)", DoAllDailies.Gen_DoAllDailies),
        ("Generate default data", DoAllDailies.Gen_DefaultData)
		]
	if args.enable_developer_commands:
		macro_generators.extend([
			("**DEV** Natural Stamina Regen Raid Farming (Non-Leader)", DragonRaid.gen_raid_experimental),
			("**DEV** Re-enter adventure (potion)", lambda : Campaign.re_enter_adventure(True)),
			("**DEV** Re-enter adventure (no potion)", lambda : Campaign.re_enter_adventure(False)),
		])

	print()
	for (n,(desc,fn)) in enumerate(macro_generators):
		print('{0}) {1}'.format(n+1, desc))

	macro_number = nox.prompt_user_for_int('Enter the macro you wish to generate: ',
										   min=1, max=len(macro_generators))

	(macro_name, file_path) = nox.load_macro_file()

	(desc, fn) = macro_generators[macro_number - 1]

	print_macro_details()
	# Generate the macro
	fn()

	# At this point we're back where we started and the macro can loop.
	nox.close()

	print('File {0} successfully written.'.format(file_path))
except SystemExit:
	pass
except:
	print('Something happened.  Please report this and paste the below text.')
	import traceback
	traceback.print_exc()
	print('Press any key to exit')
	nox.do_input()