import nox
import Common

import DoAllDailies
import Settings

# auto conquest on one chapter
# Protection is in place if you have used up your keys.  This will then effectively click "open" and "x out" over and over, without clicking reset until the macro completes.
#def gen_single_conquest(conquest_chapter, transition_duration_alter, i_sEasyOrHardContent='none'):

#    longest_run_time = nox.prompt_user_for_int(
#        "Enter longest run in seconds for {0} or 0 to skip (45-90s suggested for hell): ".format(conquest_chapter))  

#    if longest_run_time > 0:
#        nox.click_button('portal', 2000 + transition_duration_alter)
#        nox.click_button('conquests', 2000 + transition_duration_alter)
#        nox.click_button(conquest_chapter, 2000 + transition_duration_alter)
#        nox.click_button('move_to_conquest', 6000 + (transition_duration_alter * 2))  # map render delay
#        nox.click_button('prepare_battle', 2000 + transition_duration_alter)
#        nox.click_button('get_ready_for_battle', 2000 + transition_duration_alter)

#        if 'none' != i_sEasyOrHardContent:
#            DoAllDailies.Gen_SelectHero(False, i_sEasyOrHardContent)

#        nox.click_button('auto_repeat', 2000 + transition_duration_alter)
#        nox.click_button('repeat_ok', (longest_run_time * 1000 * 5))  # for now this will be 60s per run or 5 min total.  We can make this smarter later.
#        # nox.click_button('insufficient_keys', 2000 + transition_duration_alter) # should click x_out instead
#        nox.click_button('x_out', 1000 + transition_duration_alter)
#        nox.click_button('x_out', 1000 + transition_duration_alter) # second x_out in case of key reset
#        nox.click_button('exit_conquest', 20000 + (transition_duration_alter * 3)) # long render
        
def gen_conquest():
    chapterList = {
        1 : 'ch2_conquest',
        2 : 'ch3_conquest',
        3 : 'ch4_conquest',
        4 : 'ch5_conquest',
        5 : 'ch6_conquest',
        6 : 'ch7_conquest',
        7 : 'ch8_conquest'
        }
    longestRunTimeList = {
        'ch2_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap2],
        'ch3_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap3],
        'ch4_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap4],
        'ch5_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap5],
        'ch6_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap6],
        'ch7_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap7],
        'ch8_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap8]
        }

    #print('All Upper Dungeons should have set levels.  To do this manually, you can start and then stop a battle on the chosen level per dungeon.  This is also a good way to alter which levels/fragments you want to focus on.')

    Conquest_SelectEasyContentHeroesAt = 1  # Select heroes for easy content
    Conquest_SelectHardContentHeroesAt = 8  # Select heroes for hard content (Chapter 8)
    Common.Gen_Conquest_UpperDungeon_Helper('conquests',    # Portal > Conquest
                                            chapterList,
                                            longestRunTimeList,
                                            Settings.Conquest[Settings.Conquest_sHighestClearedChapter] - 1,    # Conquests chapters starts from 2
                                            Settings.Conquest[Settings.Conquest_sHardContentNoOfTimesToRetry],
                                            Conquest_SelectEasyContentHeroesAt,
                                            Conquest_SelectHardContentHeroesAt - 1)     # Conquests chapters starts from 2
    #transition_duration_alter = nox.prompt_user_for_int(
    #    "Main transition times are 2000 milliseconds.  Please enter a positive or negative value in milliseconds if you want this changed or (enter) for no change: "
    #)

    #gen_single_conquest('ch2_conquest', transition_duration_alter, Settings.Main_sEasyContent)
    #gen_single_conquest('ch3_conquest', transition_duration_alter)
    #gen_single_conquest('ch4_conquest', transition_duration_alter)
    #gen_single_conquest('ch5_conquest', transition_duration_alter)
    #gen_single_conquest('ch6_conquest', transition_duration_alter)
    #gen_single_conquest('ch7_conquest', transition_duration_alter)
    #gen_single_conquest('ch8_conquest', transition_duration_alter, Settings.Main_sHardContent)

    #Common.confirm(start_condition='The macro should be started only when the Portal button is visible')
