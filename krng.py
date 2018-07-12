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
	'ch8_upper_dungeon' : (840, 520)
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
		("Conquest + Upper Dungeon combo (beta)", conquest_plus_upper_dungeon)
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