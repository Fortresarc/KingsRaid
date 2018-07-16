import nox
import Settings

import DoAllDailies
sNONE = 'none'

def confirm(properties = None, start_condition = None, notes = []):

    if properties is None:
        properties = {}

    print()

    if len(properties) > 0:
        print('Properties:')
        for (k,v) in properties.items():
            print('  {0}: {1}'.format(k, v))
        if start_condition is not None:
            print('  Start Condition: {0}'.format(start_condition))

        for n in notes:
            print('Note: {0}'.format(n))

    print('Press Enter to confirm or Ctrl+C to cancel. ', end = '')
    nox.do_input()

    print('************************************** WARNING *************************************************')
    print('* Please watch the macro for the first few cycles to make sure everything is working as        *\n'
          '* intended.  If you are selling or grinding gear, make sure your Sell All and Grind All screen *\n'
          '* is pre-configured with the appropriate values.  For extra security, make sure all valuable   *\n'
          '* items are locked.                                                                            *\n'
          '************************************************************************************************')

    nox.wait(500)

def Gen_GoToChapter (i_sConquest_or_UpperDungeon_Button,
                     i_nChapterName,
                     i_nTransition_duration_alter) :
    nox.click_button('portal', 2000 + i_nTransition_duration_alter)
    nox.click_button(i_sConquest_or_UpperDungeon_Button, 2000 + i_nTransition_duration_alter)
    nox.click_button(i_nChapterName, 2000 + i_nTransition_duration_alter)
    nox.click_button('move_to_conquest', 6000 + (i_nTransition_duration_alter * 2))  # map render delay

# Auto Upper Dungeon/ Conquest on one chapter
# Protection is in place if you have used up your keys.  This will then effectively click "open" and "x out" over and over, without clicking reset until the macro completes.
def Gen_Single_Conquest_or_UpperDungeon_Chapter(i_sConquest_or_UpperDungeon_Button,
                                                i_nChapterName,
                                                i_lChapterList,
                                                i_nLongestRunTime_CurrentChapter,
                                                i_nTransition_duration_alter,
                                                i_nHardContentNoOfTimesToRetry,
                                                i_sEasyOrHardContent=sNONE):
    if False == nox.find_settings_file :
        longest_run_time = nox.prompt_user_for_int(
            "Enter longest run in seconds for {0} or 0 to skip (45-90s suggested for hell): ".format(i_nChapterName))  
    else :
        longest_run_time = i_nLongestRunTime_CurrentChapter
        print ("{0} longest run time = {1}".format(i_nChapterName, longest_run_time))

    if longest_run_time > 0:
        #nox.click_button('portal', 2000 + i_nTransition_duration_alter)
        #nox.click_button(i_sConquest_or_UpperDungeon_Button, 2000 + i_nTransition_duration_alter)  #nox.click_button('upper_dungeon', 2000 + i_nTransition_duration_alter)
        #nox.click_button(i_nChapterName, 2000 + i_nTransition_duration_alter)
        #nox.click_button('move_to_conquest', 6000 + (i_nTransition_duration_alter * 2))  # map render delay
        Gen_GoToChapter(i_sConquest_or_UpperDungeon_Button, i_nChapterName, i_nTransition_duration_alter)
        nox.click_button('prepare_battle', 2000 + i_nTransition_duration_alter)
        nox.click_button('get_ready_for_battle', 2000 + i_nTransition_duration_alter)

        if sNONE != i_sEasyOrHardContent:
            DoAllDailies.Gen_SelectHero(False, i_sEasyOrHardContent)

        if Settings.Main_sHardContent == i_sEasyOrHardContent :            
            print("Single gen (HARD)")
            # Start battle instead of Auto repeat
            nox.click_button('getreadyforbattle_startbattle', longest_run_time * 1000)
            # loop starts from 1 as we've already started the timer after 'Start battle' is clicked
            for i in range(1, i_nHardContentNoOfTimesToRetry) :
                nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                nox.click_button('battlecompletion_retry', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                nox.click_button('repeatpopup_singlerepeat', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                nox.click_button('repeatpopup_close', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                nox.click_button('repeatpopup_close', longest_run_time * 1000)
            
            # After we complete click away the obtained message
            nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
            nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
            nox.click_button('battlecompletion_exit', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        else :            
            print("Single gen (EASY)")
            nox.click_button('auto_repeat', 2000 + i_nTransition_duration_alter)
            nox.click_button('repeat_ok', (longest_run_time * 1000 * 5))  # for now this will be 60s per run or 5 min total.  We can make this smarter later.
            # nox.click_button('insufficient_keys', 2000 + i_nTransition_duration_alter) # should click x_out instead
            nox.click_button('x_out', 1000 + i_nTransition_duration_alter)
            nox.click_button('x_out', 1000 + i_nTransition_duration_alter) # second x_out in case of key reset
            nox.click_button('exit_conquest', 20000 + (i_nTransition_duration_alter * 3)) # long render

# Highest cleared level shouldn't exceed amount of chapters available for clearing Conquest/Upper dungeon
def Gen_Conquest_UpperDungeon_Helper (i_sConquest_or_UpperDungeon_Button,
                                      i_lChapterList,
                                      i_lLongestRunTimeList,
                                      i_nHighestClearedChapter,
                                      i_nHardContentNoOfTimesToRetry,
                                      i_nSelectEasyContentHeroesAt,
                                      i_nSelectHardContentHeroesAt):
    #print('All Upper Dungeons should have set levels.  To do this manually, you can start and then stop a battle on the chosen level per dungeon.  This is also a good way to alter which levels/fragments you want to focus on.')

    if False == nox.find_settings_file :
        transition_duration_alter = nox.prompt_user_for_int(
            "Main transition times are 2000 milliseconds.  Please enter a positive or negative value in milliseconds if you want this changed or (enter) for no change: "
        )
    else :
        transition_duration_alter = Settings.Main[Settings.Main_sTransitionDuration_Alter]

    #nHighestClearedLevel = i_nHighestClearedChapter
    #if len(i_lChapterList) < i_nHighestClearedChapter :
    #    nHighestClearedLevel = len(i_lChapterList)

    bEasyHeroHasBeenSelected = False
    bHardHeroHasBeenSelected = False

    for i in range (1, i_nHighestClearedChapter+1) :
        sContent = sNONE
        if (i_nSelectHardContentHeroesAt <= i) :
            if (False == bHardHeroHasBeenSelected) :
                sContent = Settings.Main_sHardContent
                bHardHeroHasBeenSelected = True
                #print ("Hard content at {0} {1}".format(i, i_lChapterList[i]))
        elif (i_nSelectEasyContentHeroesAt <= i):
            if (False == bEasyHeroHasBeenSelected):
                sContent = Settings.Main_sEasyContent
                bEasyHeroHasBeenSelected = True
                #print ("Easy content at {0} {1}".format(i, i_lChapterList[i]))
        Gen_Single_Conquest_or_UpperDungeon_Chapter(i_sConquest_or_UpperDungeon_Button,
                                                    i_lChapterList[i],
                                                    i_lChapterList,
                                                    i_lLongestRunTimeList[i_lChapterList[i]],
                                                    transition_duration_alter,
                                                    i_nHardContentNoOfTimesToRetry,
                                                    sContent)

    confirm(start_condition='The macro should be started only when the Portal button is visible')
