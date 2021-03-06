import nox
import Settings
import Inventory
import DoAllDailies
import KRSelect
import Campaign
import Common
import Manager

sNONE = 'none'
nNoOfKeysPerChapter = 5

##############
# NOX Helpers
##############
def KillKingsRaid():
    # Bring up recent apps
    Manager.keypress_msecs(nox.keypress_RecentApps, Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
    # Kill King's Raid app
    nox.mouse_drag('main_killkingsraid_bottom', 'main_killkingsraid_top', Settings.Main[Settings.Main_sDurationAfterClick_ms], 0.5)

def Back():
    Manager.keypress_msecs(nox.keypress_Back, Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])

##############
# Public Helpers
##############
def Gen_RelaunchKingsRaid ():
    KillKingsRaid()
    Gen_LaunchKingsRaidAndGoToMainScreen()

# Go to main screen after Nox restarted
def Gen_LaunchKingsRaidAndGoToMainScreen () :
    NoOfClicksToClearTranslucentPopups = 3
    # Launch game from Nox screen till Tap to Play screen
    Manager.click_button_secs('nox_launchgame', Settings.Main[Settings.Main_sGameLaunch_TapToPlayDuration_s])

    # Tap to play till main game screen
    Manager.click_button_msecs('nox_launchgame', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_secs('nox_launchgame', Settings.Main[Settings.Main_sGameLaunch_MainGameScreenDuration_s])

    # This will click away main game screen, loading screen, advertisements
    for i in range(0, Settings.Main[Settings.Main_sNoOfClicksToClearAdvertisement]) :
        Manager.click_button_msecs('main_advertisement_close', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])

    # Close translucent popup separately .. don't wait so long to click again
    for i in range(0, NoOfClicksToClearTranslucentPopups) :
        Manager.click_button_msecs('translucentpopup_close', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])

    # Just to be sure - click again to clear advertisement
    for i in range(0, Settings.Main[Settings.Main_sNoOfClicksToClearAdvertisement]) :
        Manager.click_button_msecs('main_advertisement_close', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
        
def Gen_DoStory(i_sWhichChapter = 8, i_bReenterStoryAfterGrindOrSell = True) :
    # Navigate to chapter
    # currently only support chapter 6 to 8
    if 8 <= i_sWhichChapter :
        Gen_GoToChapter('conquests', 'ch8_conquest', Settings.Main[Settings.Main_sTransitionDuration_ms])
        Manager.click_button_msecs('ch8_conquest_naviTo_story_8_20', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        Manager.click_button_msecs('ch8_conquest_naviTo_story_8_25', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        Manager.click_button_msecs('ch8_conquest_naviTo_story_8_24', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        Manager.click_button_msecs('ch8_conquest_naviTo_story_8_23', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        Manager.click_button_msecs('ch8_conquest_naviTo_story_8_23_2', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    elif 7 == i_sWhichChapter :
        Gen_GoToChapter('conquests', 'ch7_conquest', Settings.Main[Settings.Main_sTransitionDuration_ms])
        Manager.click_button_msecs('ch7_conquest_naviTo_story_7_8', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    elif 6 == i_sWhichChapter :
        Gen_GoToChapter('conquests', 'ch6_conquest', Settings.Main[Settings.Main_sTransitionDuration_ms])
        Manager.click_button_msecs('ch6_conquest_naviTo_story_6_10', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])

    Manager.click_button_msecs('main_preparebattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('get_ready_for_battle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # For now we use Conquests Hero selection for story as well
    KRSelect.Gen_SelectQuestHero(KRSelect.QuestType_Story, False, Settings.Main_sEasyContent)

    Campaign.gen_natural_stamina_farm(i_bReenterStoryAfterGrindOrSell)
    
def Gen_NavigateToGameHomePage(i_bAlreadyInTown = False):
    Gen_NavigateToMain('portal_orvel_herosinn', i_bAlreadyInTown)
    # Exit to home page
    Back()

def Gen_NavigateToMain(i_portal_orvel_placetogo, i_bAlreadyInTown = False) :
    if False == i_bAlreadyInTown :
        Manager.click_button_msecs('main_portal', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        Manager.click_button_msecs('upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        Manager.click_button_msecs('ch1_upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # This has to wait longer because we are transiting to another big game screen    
        Manager.click_button_secs('minipopup_confirmbutton', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])
    
    Manager.click_button_msecs('main_portal', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('portal_orvel', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    Manager.click_button_msecs(i_portal_orvel_placetogo, Settings.Main[Settings.Main_sDurationAfterClick_ms])

    # This has to wait longer because we are transiting to another big game screen
    Manager.click_button_secs('minipopup_confirmbutton', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])
    
# Clears inventory (Assumes we are at main game screen)
def Gen_ClearInventory() :
    # Click inventory
    Manager.click_button_msecs('main_inventory', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    if ('g' == Settings.Story[Settings.Story_sGrindOrSellInventory]):
        Inventory.manage_inventory(True, False)
    else:
        Inventory.manage_inventory(False, True)

    # Back to main game screen
    Back()

# Claim Mailbox
def Gen_ClaimMailbox () :
    # Click mailbox icon
    Manager.click_button_msecs('main_mailbox', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('mailbox_claimall', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
    Manager.click_button_msecs('mailbox_close', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])

# Doesn't really matter the order at which we claim
def Gen_ClaimDailyMission (i_nNumOfMissionsToClaim = 3, i_bClaimFromHomePage = False) :
    Manager.click_button_msecs('main_mission', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    for i in range(0, i_nNumOfMissionsToClaim) :
        Manager.click_button_msecs('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # Back to main
    Back()
    Gen_NavigateToGameHomePage(i_bClaimFromHomePage)

def Gen_GoToChapter (i_sQuestButtonName,
                     i_nChapterName,
                     i_nTransition_duration_alter) :
    Manager.click_button_msecs('main_portal', 2000 + i_nTransition_duration_alter, False)
    Manager.click_button_msecs(i_sQuestButtonName, 2000 + i_nTransition_duration_alter, False)
    Manager.click_button_msecs(i_nChapterName, 2000 + i_nTransition_duration_alter, False)
    Manager.click_button_msecs('move_to_conquest', 6000 + (i_nTransition_duration_alter * 2), False)  # map render delay

def _GetQuestTypeFromButtonName(i_sButtonName):
    if 'conquests' == i_sButtonName:
        return KRSelect.QuestType_Conquest
    elif 'upper_dungeon':
        return KRSelect.QuestType_UpperDungeon
    else:
        return KRSelect.QuestType_Story

# Auto Upper Dungeon/ Conquest on one chapter
# Protection is in place if you have used up your keys.  This will then effectively click "open" and "x out" over and over, without clicking reset until the macro completes.
def _Gen_EasyStages_Conquest_or_UpperDungeon(i_sQuestButtonName,
                                            i_lChapterList,
                                            i_lLongestRunTimeList,
                                            i_nStartAtChapter,
                                            i_nHighestClearedChapter,
                                            i_nSelectEasyContentHeroesAt,
                                            i_nSelectHardContentHeroesAt,
                                            i_nHardContentNoOfTimesToRetry,
                                            i_nTransitionDurationAlter):
    # Init variables
    nTotalTime_AllEasyChapters_s = 0

    # Find total run time for all Easy chapters
    if False == nox.find_settings_file :
        Manager.Trace2 ("ERROR: Please generate Settings.json for this to work")
    else :
        # NOTE: index starts from 1
        for i in range(i_nStartAtChapter, i_nHighestClearedChapter + 1) :
            # Add up all easy chapters
            # nNoOfKeysPerChapter = 5 for each chapter
            if (i >= i_nSelectEasyContentHeroesAt) and (i < i_nSelectHardContentHeroesAt) :
                nTotalTime_AllEasyChapters_s += (i_lLongestRunTimeList[i_lChapterList[i]] * nNoOfKeysPerChapter)

    Manager.Trace2 ("Easy chapters will take {0} to complete\n".format( 
        Manager.GetString_HMSFormat( Manager.ConvertSecsToMsecs(nTotalTime_AllEasyChapters_s)) )
        )

    if nTotalTime_AllEasyChapters_s > 0:
        # Go to easy chapter first
        Gen_GoToChapter(i_sQuestButtonName, i_lChapterList[i_nStartAtChapter], i_nTransitionDurationAlter)
        Manager.click_button_msecs('prepare_battle', 2000 + i_nTransitionDurationAlter, False)
        Manager.click_button_msecs('get_ready_for_battle', 2000 + i_nTransitionDurationAlter, False)

        # Select easy hero
        KRSelect.Gen_SelectQuestHero(_GetQuestTypeFromButtonName(i_sQuestButtonName),
                                     False,
                                     Settings.Main_sEasyContent)

        Manager.Trace2("Continous Battle through all Chapters (EASY HEROES)")
        Manager.click_button_msecs('getreadyforbattle_startbattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        Manager.click_button_msecs('selectbattle_continuousbattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        Manager.click_button_msecs('notice_continuousbattle_ok', Settings.Main[Settings.Main_sDurationAfterClick_ms])

        # Wait till we propagated to the hard chapter
        Manager.wait_secs(nTotalTime_AllEasyChapters_s)

def _Gen_HardStages_Conquest_or_UpperDungeon(i_sQuestButtonName,
                                            i_lChapterList,
                                            i_lLongestRunTimeList,
                                            i_nStartAtChapter,
                                            i_nHighestClearedChapter,
                                            i_nSelectEasyContentHeroesAt,
                                            i_nSelectHardContentHeroesAt,
                                            i_nHardContentNoOfTimesToRetry,
                                            i_nTransitionDurationAlter,
                                            i_bContinueFromEasy = True):
    # Init variables
    nLongestRunTime_HardChapter_s = 0
    nCountHardChapters = 0
    nConquestChapter8 = 7
    bChap8HellModeUnlocked = False

    # Get the longest of all hard chapter(s) 
    if False == nox.find_settings_file :
        Manager.Trace2 ("ERROR: Please generate Settings.json for this to work")
    else :
        # NOTE: index starts from 1
        for i in range(i_nStartAtChapter, i_nHighestClearedChapter + 1) :
            if (i_lLongestRunTimeList[i_lChapterList[i]] > nLongestRunTime_HardChapter_s) \
               and (i >= i_nSelectHardContentHeroesAt):
                nLongestRunTime_HardChapter_s = i_lLongestRunTimeList[i_lChapterList[i]]

    # Early return
    if nLongestRunTime_HardChapter_s <= 0:
        return

    sChap8HellModeUnlocked = Settings.Main[Settings.Main_sHellModeUnlocked_Chap8]
    sChap8HellModeUnlocked = sChap8HellModeUnlocked.lower()
    if sChap8HellModeUnlocked == 'n':
        bChap8HellModeUnlocked = False
    elif sChap8HellModeUnlocked == 'y':
        bChap8HellModeUnlocked = True

    bIsConquest = (KRSelect.QuestType_Conquest == _GetQuestTypeFromButtonName(i_sQuestButtonName))
    # Loop same chapter for i_nHardContentNoOfTimesToRetry times
    for i in range (i_nSelectHardContentHeroesAt, i_nHighestClearedChapter+1):
        # Conquest starts from Chapter 2
        nChapterNumber = i
        if bIsConquest:
            nChapterNumber = i + 1

        # Conquest Continuous battle will only automatically proceed to next Chapter's same mode 
        # i.e. Chap1(Hell) -> Chap2(Hell) -> Chap3(Hell) ... Chap8(Hard)
        #                 cont           cont               stop at 8

        bIsConquest_And_Chap8NoHellMode = bIsConquest \
                                          and (nConquestChapter8 == i) \
                                          and (False == bChap8HellModeUnlocked)
        bShouldGoToChapterManually = bIsConquest_And_Chap8NoHellMode \
                                     or (nCountHardChapters > 0) \
                                     or i_bContinueFromEasy == False
        if bShouldGoToChapterManually:
            # Conquest Continuous battle will only automatically proceed to next Chapter's same mode 
            # i.e. Chap1(Hell) -> Chap2(Hell) -> Chap3(Hell) ... Chap8(Hard)
            #                 cont           cont               stop at 8
            #
            # Chap 8 has no hell mode unlocked yet, it will stop Continuous battle at Chap 7 victory screen.
            # Lets manually go to Chap 8
            if bIsConquest_And_Chap8NoHellMode:
                Manager.Trace2("Continuous Battle >> Hell mode on Conquest (Chapter {0}) has NOT been unlocked yet! Let's manually navigate ".format(nChapterNumber))
                Manager.Trace2("to Chapter {0} ourselves".format(nChapterNumber))
                Manager.click_button_secs('battlecompletion_exit', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])

            Gen_GoToChapter(i_sQuestButtonName, i_lChapterList[i], i_nTransitionDurationAlter)
            Manager.click_button_msecs('prepare_battle', 2000 + i_nTransitionDurationAlter, False)
            Manager.click_button_msecs('get_ready_for_battle', 2000 + i_nTransitionDurationAlter, False)

        # Conquest Continuous battle will only automatically proceed to next Chapter's same mode 
        # i.e. Chap1(Hell) -> Chap2(Hell) -> Chap3(Hell) ... Chap8(Hard)
        #                 cont           cont               stop at 8
        #
        # Chap 8 has hell mode unlocked!! Here we probably lost the battle once, change party to hard heroes
        if i_bContinueFromEasy and bIsConquest_And_Chap8NoHellMode == False:
            Manager.Trace2("Continuous Battle >> Automatically went to Chapter {0} and we will probably lose here because we are using Easy"\
                .format(nChapterNumber))
            Manager.Trace2("Heroes on Hell mode, don't worry let's do a Change Party to Hard heroes and start winning!".format(nChapterNumber))
            # Wait for easy heroes to fail hard chapter 1 time(s)
            Manager.wait_secs(nLongestRunTime_HardChapter_s * 1)

            # Goto change party screen
            Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            Manager.click_button_secs('battlecompletion_changeparty', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])

        # Select hard heroes
        Manager.Trace2("")
        Manager.Trace2("Generating Single Chapter{0} (HARD HEROES)".format(nChapterNumber))
        KRSelect.Gen_SelectQuestHero(_GetQuestTypeFromButtonName(i_sQuestButtonName),
                                     False,
                                     Settings.Main_sHardContent)

        # Start battle instead of Auto repeat
        Manager.click_button_msecs('getreadyforbattle_startbattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        Manager.click_button_secs('selectbattle_startbattle', nLongestRunTime_HardChapter_s, False)
        # loop starts from 1 as we've already started the timer after 'Start battle' is clicked
        for i in range(1, i_nHardContentNoOfTimesToRetry+1) :
            Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
            Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            # Just to be sure we have clicked away all obtained messages
            Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])

            Manager.click_button_msecs('battlecompletion_retry', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            Manager.click_button_msecs('repeatpopup_singlerepeat', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
            Manager.click_button_msecs('repeatpopup_close', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            Manager.click_button_msecs('repeatpopup_close', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            # Just to be sure
            Manager.click_button_msecs('repeatpopup_close', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            Manager.wait_secs(nLongestRunTime_HardChapter_s)

        # Done!
        # After we complete click away the obtained message
        Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        # Just to be sure
        Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        # Just to be sure
        Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        # Just to be sure once more
        Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        # Back to map
        Manager.click_button_msecs('battlecompletion_exit', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])

        nCountHardChapters += 1

    # Done all conquests/ upper dungeons. 
    # This is to ensure that we exit to main screen (in this case to chapter map)
    Manager.wait_secs(Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])

# Highest cleared level shouldn't exceed amount of chapters available for clearing Conquest/Upper dungeon
def Gen_Conquest_UpperDungeon_Helper (i_sQuestButtonName,           #button name.. 
                                      i_lChapterList,
                                      i_lLongestRunTimeList,
                                      i_nHighestClearedChapter,
                                      i_nHardContentNoOfTimesToRetry,
                                      i_nSelectEasyContentHeroesAt,
                                      i_nSelectHardContentHeroesAt,
                                      i_nStartAtChapter = 1):
    #Manager.Trace2('All Upper Dungeons should have set levels.  To do this manually, you can start and then stop a battle on the chosen level per dungeon.  This is also a good way to alter which levels/fragments you want to focus on.')
    
    # Find transition time
    if False == nox.find_settings_file :
        nTransitionDurationAlter = nox.prompt_user_for_int(
            "Main transition times are 2000 milliseconds.  Please enter a positive or negative value in milliseconds if you want this changed or (enter) for no change: "
        )
    else :
        nTransitionDurationAlter = Settings.Main[Settings.Main_sTransitionDuration_ms]

    _Gen_EasyStages_Conquest_or_UpperDungeon(i_sQuestButtonName,
                                            i_lChapterList,
                                            i_lLongestRunTimeList,
                                            i_nStartAtChapter,
                                            i_nHighestClearedChapter,
                                            i_nSelectEasyContentHeroesAt,
                                            i_nSelectHardContentHeroesAt,
                                            i_nHardContentNoOfTimesToRetry,
                                            nTransitionDurationAlter)

    _Gen_HardStages_Conquest_or_UpperDungeon(i_sQuestButtonName,
                                            i_lChapterList,
                                            i_lLongestRunTimeList,
                                            i_nStartAtChapter,
                                            i_nHighestClearedChapter,
                                            i_nSelectEasyContentHeroesAt,
                                            i_nSelectHardContentHeroesAt,
                                            i_nHardContentNoOfTimesToRetry,
                                            nTransitionDurationAlter,
                                            True)
    
# Auto Upper Dungeon/ Conquest on one chapter
# Protection is in place if you have used up your keys.  This will then effectively click "open" and "x out" over and over, without clicking reset until the macro completes.
def _Gen_Single_Conquest_or_UpperDungeon_Chapter_DEPRECATED(i_sQuestButtonName,
                                                i_nChapterName,
                                                i_lChapterList,
                                                i_nLongestRunTime_CurrentChapter,
                                                i_nTransition_duration_alter,
                                                i_nHardContentNoOfTimesToRetry,
                                                i_sEasyOrHardContent=sNONE):
    if False == nox.find_settings_file :
        longest_run_time_s = nox.prompt_user_for_int(
            "Enter longest run in seconds for {0} or 0 to skip (45-90s suggested for hell): ".format(i_nChapterName))  
    else :
        longest_run_time_s = i_nLongestRunTime_CurrentChapter
        Manager.Trace2 ("{0} longest run time = {1}".format(i_nChapterName, longest_run_time_s))

    if longest_run_time_s > 0:
        Gen_GoToChapter(i_sQuestButtonName, i_nChapterName, i_nTransition_duration_alter)
        Manager.click_button_msecs('prepare_battle', 2000 + i_nTransition_duration_alter, False)
        Manager.click_button_msecs('get_ready_for_battle', 2000 + i_nTransition_duration_alter, False)

        if sNONE != i_sEasyOrHardContent:
            KRSelect.Gen_SelectQuestHero(_GetQuestTypeFromButtonName(i_sQuestButtonName),
                                         False,
                                         i_sEasyOrHardContent)

        if Settings.Main_sHardContent == i_sEasyOrHardContent :
            Manager.Trace2("Single chap gen (HARD)")
            # Start battle instead of Auto repeat
            Manager.click_button_msecs('getreadyforbattle_startbattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            Manager.click_button_secs('selectbattle_startbattle', longest_run_time_s, False)
            # loop starts from 1 as we've already started the timer after 'Start battle' is clicked
            for i in range(1, i_nHardContentNoOfTimesToRetry) :
                Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
                Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])
                # Just to be sure we have clicked away all obtained messages
                Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])

                Manager.click_button_msecs('battlecompletion_retry', Settings.Main[Settings.Main_sDurationAfterClick_ms])
                Manager.click_button_msecs('repeatpopup_singlerepeat', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
                Manager.click_button_msecs('repeatpopup_close', Settings.Main[Settings.Main_sDurationAfterClick_ms])
                Manager.click_button_msecs('repeatpopup_close', Settings.Main[Settings.Main_sDurationAfterClick_ms])
                # Just to be sure
                Manager.click_button_msecs('repeatpopup_close', Settings.Main[Settings.Main_sDurationAfterClick_ms])
                Manager.wait_secs(longest_run_time_s)
            
            # After we complete click away the obtained message
            Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
            # Just to be sure
            Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
            # Just to be sure
            Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
            # Just to be sure once more
            Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
            # Back to map
            Manager.click_button_msecs('battlecompletion_exit', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        else :            
            Manager.Trace2("Single chap gen (EASY)")
            Manager.click_button_msecs('auto_repeat', 2000 + i_nTransition_duration_alter, False)
            Manager.click_button_secs('repeat_ok', (longest_run_time_s * 5), False)  # for now this will be 60s per run or 5 min total.  We can make this smarter later.
            # Manager.click_button_msecs('insufficient_keys', 2000 + i_nTransition_duration_alter, False) # should click x_out instead
            Manager.click_button_msecs('x_out', 1000 + i_nTransition_duration_alter, False)
            Manager.click_button_msecs('x_out', 1000 + i_nTransition_duration_alter, False) # second x_out in case of key reset
            Manager.click_button_msecs('exit_conquest', 20000 + (i_nTransition_duration_alter * 3), False) # long render

    # Done all conquests/ upper dungeons. 
    # This is to ensure that we exit to main screen (in this case to chapter map)
    Manager.wait_secs(Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])

# Highest cleared level shouldn't exceed amount of chapters available for clearing Conquest/Upper dungeon
def Gen_Conquest_UpperDungeon_Helper_DEPRECATED (i_sQuestButtonName,           #button name.. 
                                      i_lChapterList,
                                      i_lLongestRunTimeList,
                                      i_nHighestClearedChapter,
                                      i_nHardContentNoOfTimesToRetry,
                                      i_nSelectEasyContentHeroesAt,
                                      i_nSelectHardContentHeroesAt,
                                      i_nStartAtChapter = 1):
    #Manager.Trace2('All Upper Dungeons should have set levels.  To do this manually, you can start and then stop a battle on the chosen level per dungeon.  This is also a good way to alter which levels/fragments you want to focus on.')

    if False == nox.find_settings_file :
        transition_duration_alter = nox.prompt_user_for_int(
            "Main transition times are 2000 milliseconds.  Please enter a positive or negative value in milliseconds if you want this changed or (enter) for no change: "
        )
    else :
        transition_duration_alter = Settings.Main[Settings.Main_sTransitionDuration_ms]

    #nHighestClearedLevel = i_nHighestClearedChapter
    #if len(i_lChapterList) < i_nHighestClearedChapter :
    #    nHighestClearedLevel = len(i_lChapterList)

    bEasyHeroHasBeenSelected = False
    bHardHeroHasBeenSelected = False

    # Select easy/ hard heroes before doing conquest / upper dungeon for single chap
    for i in range(i_nStartAtChapter, i_nHighestClearedChapter + 1) :
        sContent = sNONE
        if (i_nSelectHardContentHeroesAt <= i) :
            if (False == bHardHeroHasBeenSelected) :
                sContent = Settings.Main_sHardContent
                bHardHeroHasBeenSelected = True
                Manager.TraceHeader2()
                Manager.Trace2 ("Hard content from: {0}) {1}".format(i, i_lChapterList[i]))
        elif (i_nSelectEasyContentHeroesAt <= i):
            if (False == bEasyHeroHasBeenSelected):
                sContent = Settings.Main_sEasyContent
                bEasyHeroHasBeenSelected = True
                Manager.TraceHeader2()
                Manager.Trace2 ("Easy content from: {0}) {1}".format(i, i_lChapterList[i]))
        _Gen_Single_Conquest_or_UpperDungeon_Chapter(i_sQuestButtonName,
                                                    i_lChapterList[i],
                                                    i_lChapterList,
                                                    i_lLongestRunTimeList[i_lChapterList[i]],
                                                    transition_duration_alter,
                                                    i_nHardContentNoOfTimesToRetry,
                                                    sContent)

    Common.confirm(start_condition='The macro should be started only when the Portal button is visible')
