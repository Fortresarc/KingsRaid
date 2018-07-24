import sys

import os
import nox
import Manager

def grind_or_sell_all(is_grind):
	# Grind
	button = 'grind' if is_grind else 'sell'

	Manager.click_button_msecs(button, 3500, False)

	# Grind all
	Manager.click_button_msecs('grind_all', 3500, False)

	# Click the Grind button on the window that pops up
	Manager.click_button_msecs('grind_2', 3500, False)

	# Confirmation
	Manager.click_button_msecs('grind_confirm', 3500, False)

	if is_grind:
		# Click on the screen to get rid of the results
		Manager.click_button_msecs('dismiss_results', 3500, False)

def manage_inventory(should_grind, should_sell):
	if should_grind:
		grind_or_sell_all(True)
	if should_sell:
		grind_or_sell_all(False)
