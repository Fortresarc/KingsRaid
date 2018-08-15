import sys

import os
import nox
import Common

def gen_raid():
	Common.confirm(start_condition='The macro can be started in a raid lobby or while a raid is in progress.')

	nox.click_button('start_raid', 5000)
	nox.click_button('confirm_insufficient_members', 500)
	nox.click_button('abandon_raid', 5000)

def gen_raid_leader():
	Common.confirm(start_condition='The macro can be started in a raid lobby or while a raid is in progress.')

	start_clicks = nox.prompt_user_for_int('How many repetitive start clicks? (default is 3)', default = 3)
	click_duration = nox.prompt_user_for_int('How many milliseconds between clicks? (default is 500)', default = 500)

	# click here first to add a long wait and slow the macro down
	nox.click_button('abandon_raid', 2500)

	for i in range(0, start_clicks):
		nox.click_button('start_raid', click_duration)
		nox.click_button('confirm_insufficient_members', click_duration)

def gen_raid_experimental():

	Common.confirm()
	nox.click_button('start_raid', 10000)
	nox.click_button('stam_potion_confirm', 1000)
	nox.click_button('abandon_raid', 1000)
