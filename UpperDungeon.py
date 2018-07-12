import nox
import Common

# auto upper dungeon on one chapter
# Protection is in place if you have used up your keys.  This will then effectively click "open" and "x out" over and over, without clicking reset until the macro completes.
def gen_single_upper_dungeon(chapter, transition_duration_alter):

	longest_run_time = nox.prompt_user_for_int(
		"Enter longest run in seconds for {0} or 0 to skip (45-90s suggested for hell): ".format(chapter))  

	if longest_run_time > 0:
		nox.click_button('portal', 2000 + transition_duration_alter)
		nox.click_button('upper_dungeon', 2000 + transition_duration_alter)
		nox.click_button(chapter, 2000 + transition_duration_alter)
		nox.click_button('move_to_conquest', 6000 + (transition_duration_alter * 2))  # map render delay
		nox.click_button('prepare_battle', 2000 + transition_duration_alter)
		nox.click_button('get_ready_for_battle', 2000 + transition_duration_alter)
		nox.click_button('auto_repeat', 2000 + transition_duration_alter)
		nox.click_button('repeat_ok', (longest_run_time * 1000 * 5))  # for now this will be 60s per run or 5 min total.  We can make this smarter later.
		# nox.click_button('insufficient_keys', 2000 + transition_duration_alter) # should click x_out instead
		nox.click_button('x_out', 1000 + transition_duration_alter)
		nox.click_button('x_out', 1000 + transition_duration_alter) # second x_out in case of key reset
		nox.click_button('exit_conquest', 20000 + (transition_duration_alter * 3)) # long render
		
def gen_upper_dungeon():

	print('All Upper Dungeons should have set levels.  To do this manually, you can start and then stop a battle on the chosen level per dungeon.  This is also a good way to alter which levels/fragments you want to focus on.')

	transition_duration_alter = nox.prompt_user_for_int(
		"Main transition times are 2000 milliseconds.  Please enter a positive or negative value in milliseconds if you want this changed or (enter) for no change: "
	)

	gen_single_upper_dungeon('ch1_upper_dungeon', transition_duration_alter)
	gen_single_upper_dungeon('ch2_upper_dungeon', transition_duration_alter)
	gen_single_upper_dungeon('ch3_upper_dungeon', transition_duration_alter)
	gen_single_upper_dungeon('ch4_upper_dungeon', transition_duration_alter)
	gen_single_upper_dungeon('ch5_upper_dungeon', transition_duration_alter)
	gen_single_upper_dungeon('ch6_upper_dungeon', transition_duration_alter)
	gen_single_upper_dungeon('ch7_upper_dungeon', transition_duration_alter)
	gen_single_upper_dungeon('ch8_upper_dungeon', transition_duration_alter)

	Common.confirm(start_condition='The macro should be started only when the Portal button is visible')
