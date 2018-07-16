import nox
import Common
import DoAllDailies
import Settings

sNONE = 'none'

# auto upper dungeon on one chapter
# Protection is in place if you have used up your keys.  This will then effectively click "open" and "x out" over and over, without clicking reset until the macro completes.
def gen_single_upper_dungeon(chapter, transition_duration_alter, i_sEasyOrHardContent=sNONE):
    chapterlist = {
        'ch1_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap1],
        'ch2_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap2],
        'ch3_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap3],
        'ch4_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap4],
        'ch5_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap5],
        'ch6_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap6],
        'ch7_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap7],
        'ch8_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap8]
        }
    if False == nox.find_settings_file :
        longest_run_time = nox.prompt_user_for_int(
            "Enter longest run in seconds for {0} or 0 to skip (45-90s suggested for hell): ".format(chapter))  
    else :
        longest_run_time = chapterlist[chapter]
        print ("{0} longest run time = {1}".format(chapter, longest_run_time))

    if longest_run_time > 0:
        nox.click_button('portal', 2000 + transition_duration_alter)
        nox.click_button('upper_dungeon', 2000 + transition_duration_alter)
        nox.click_button(chapter, 2000 + transition_duration_alter)
        nox.click_button('move_to_conquest', 6000 + (transition_duration_alter * 2))  # map render delay
        nox.click_button('prepare_battle', 2000 + transition_duration_alter)
        nox.click_button('get_ready_for_battle', 2000 + transition_duration_alter)

        if 'ch1_upper_dungeon' == chapter:
            DoAllDailies.Gen_SelectHero(False, i_sEasyOrHardContent)

        if Settings.Main_sEasyContent == i_sEasyOrHardContent :
            nox.click_button('auto_repeat', 2000 + transition_duration_alter)
            nox.click_button('repeat_ok', (longest_run_time * 1000 * 5))  # for now this will be 60s per run or 5 min total.  We can make this smarter later.
            # nox.click_button('insufficient_keys', 2000 + transition_duration_alter) # should click x_out instead
            nox.click_button('x_out', 1000 + transition_duration_alter)
            nox.click_button('x_out', 1000 + transition_duration_alter) # second x_out in case of key reset
            nox.click_button('exit_conquest', 20000 + (transition_duration_alter * 3)) # long render
        else :
            # Start battle instead of Auto repeat
            nox.click_button('getreadyforbattle_startbattle', longest_run_time * 1000)
            # loop starts from 1 as we've already started the timer after 'Start battle' is clicked
            for i in range(1, Settings.UpperDungeon[Settings.UpperDungeon_sHardContentRetryTimes]) :
                nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                nox.click_button('battlecompletion_retry', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                nox.click_button('repeatpopup_singlerepeat', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                nox.click_button('repeatpopup_close', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                nox.click_button('repeatpopup_close', longest_run_time * 1000)
            nox.click_button('battlecompletion_exit', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

def gen_upper_dungeon():
    chapterlist = {
        1 : 'ch1_upper_dungeon',
        2 : 'ch2_upper_dungeon',
        3 : 'ch3_upper_dungeon',
        4 : 'ch4_upper_dungeon',
        5 : 'ch5_upper_dungeon',
        6 : 'ch6_upper_dungeon',
        7 : 'ch7_upper_dungeon',
        8 : 'ch8_upper_dungeon'
        }

    print('All Upper Dungeons should have set levels.  To do this manually, you can start and then stop a battle on the chosen level per dungeon.  This is also a good way to alter which levels/fragments you want to focus on.')

    if False == nox.find_settings_file :
        transition_duration_alter = nox.prompt_user_for_int(
            "Main transition times are 2000 milliseconds.  Please enter a positive or negative value in milliseconds if you want this changed or (enter) for no change: "
        )
    else :
        transition_duration_alter = Settings.Main[Settings.Main_sTransitionDuration_Alter]

    if len(chapterlist) < Settings.UpperDungeon[Settings.UpperDungeon_sHighestClearedChapter]:
        Settings.UpperDungeon[Settings.UpperDungeon_sHighestClearedChapter] = len(chapterlist)

    for i in range (1, Settings.UpperDungeon[Settings.UpperDungeon_sHighestClearedChapter]+1) :
        sContent = Settings.Main_sEasyContent
        if 8 <= i :
            sContent = Settings.Main_sHardContent
        gen_single_upper_dungeon(chapterlist[i], transition_duration_alter, sContent)

    Common.confirm(start_condition='The macro should be started only when the Portal button is visible')
