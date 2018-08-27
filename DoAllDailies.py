import nox
import datetime
from datetime import timedelta
import Common
import Inventory
import Settings
import Manager
import KRCommon
import KRSelect
import UpperDungeon
import Conquest
import Campaign
import DragonRaid

Vault_TopLevel = 50
Vault_Top3Level = 43

# Main code to do all dailies
def Gen_DoAllDailies() :
    
    # Read our settings file
    Settings.ReadFromFile()

    now = datetime.datetime.now()

    Manager.Trace1 ("NOTES:")
    Manager.Trace1 ("- Main story and conquest share same hero selection list")
    Manager.Trace1 ("  Start time = %02d:%02d:%02d" % ( now.hour,
                                                      now.minute,
                                                      now.second) )

    lTimeTakenSummary = []

    # Do sequence as read from settings file
    i = 0
    for value in Settings.DoAllDailiesSequence :
        Manager.TraceHeader1 ()
        nTimeTemp = nox.time
        _ExecuteSingleDailyFunction(Settings.DoAllDailiesSequence[i])
        Manager.TraceSubHeader1 ()
        currentTaskSummary ="TaskTime = {0}, FinishTime = {1}, TotalTime = {2} \t[\"{3}\"]".format(
            Manager.GetString_TimeLapsed(nTimeTemp),
            Manager.GetString_AddToTime_HMSFormat(now),
            Manager.GetString_TotalRunTime_HMSFormat(),
            Settings.DoAllDailiesSequence[i])
        Manager.Trace1 (currentTaskSummary)
        lTimeTakenSummary.append(currentTaskSummary)
        Manager.TraceFooter1 ()
        i += 1

    # Print time taken summary
    Manager.TraceHeader1()
    Manager.Trace1 ("Summary of time for each tasks: \n")
    for s in lTimeTakenSummary:
        Manager.Trace1 ("%s" % s)
    Manager.TraceFooter1()

    Manager.Trace1("\n\nDoAllDailies will run for {0} and end at {1}\n\n".format(
        Manager.GetString_TotalRunTime_HMSFormat(),
        Manager.GetString_AddToTime_HMSFormat(now)))

# TEST CODES
#def TEST ():
    #KRCommon.Gen_LaunchKingsRaidAndGoToMainScreen()
    
    #KRCommon.Gen_ClaimMailbox()
    #Gen_ExchangeAmity()
    #KRCommon.Gen_ClearInventory()

    #Gen_Stockade(False)

    #KRCommon.Gen_NavigateToMain('portal_orvel_herosinn', False)
    #Gen_Daily_HerosInn(False)
    #UpperDungeon.gen_upper_dungeon()

    #KRCommon.Gen_NavigateToMain('portal_orvel_arena', False)
    #Gen_Arena()
    #Gen_WorldBoss()
    
    ## This is to save some time navigating to Orvel castle after we collected EXP and Gold hot time
    #KRCommon.Gen_NavigateToMain('portal_orvel_orvelcastle', False)
    #KRCommon.Back()
    #Manager.Gen_ClaimEnergyGoldHotTime(Manager.ClaimEXPGoldStepsList[Manager.sClaim_1stEXP_1stGold])
    
    #KRCommon.Gen_NavigateToMain('portal_orvel_orvelcastle', True)
    #Gen_AncientRoyalVault()

    #Conquest.gen_conquest()

    #Manager.Gen_ClaimEnergyGoldHotTime(Manager.ClaimEXPGoldStepsList[Manager.sClaim_2ndEXPNGoldWStamina])
    #KRCommon.Gen_DoStory(Settings.Story[Settings.Story_sAutoRepeatAtChapter])
    #KRCommon.Gen_ClaimDailyMission(6, True)

def Gen_DoLaunchNOX_DragonRaid() :
    _Gen_DoLaunchNOX_DoQuest(True)
    
def Gen_DoLaunchNOX_Story() :
    _Gen_DoLaunchNOX_DoQuest(False)

# Either do story / dragon raids
def _Gen_DoLaunchNOX_DoQuest(i_bIsDragonRaid = True) :

    # Read our settings file
    Settings.ReadFromFile()

    CommonQuestSequence = {
        0 : Settings.DoAllDailies_sLaunchKingsRaidAndGoToMainScreen,
        1 : Settings.DoAllDailies_sClaimMailbox,
        2 : Settings.DoAllDailies_sExchangeAmity,
        3 : Settings.DoAllDailies_sClaimDailyMission,
        4 : Settings.DoAllDailies_sClearInventory
    }
    sQuestType = 'Story'
    if(i_bIsDragonRaid):
        sQuestType = 'DragonRaid'

    for key in CommonQuestSequence:
        Manager.TraceHeader1()
        nTimeTemp = nox.time
        _ExecuteSingleDailyFunction(CommonQuestSequence[key])
        Manager.TraceSubHeader1 ()
        Manager.Trace1 ("Do {0} after NOX restarts {1} : {2} .. Will execute for {3}".format( sQuestType,
                                                                                              key,
                                                                                              CommonQuestSequence[key],
                                                                                              Manager.GetString_TimeLapsed(nTimeTemp)))
        Manager.TraceFooter1 ()

    if i_bIsDragonRaid :
        DragonRaid.Gen_DoDragonRaid()
    else :
        # Claim some energy 
        Manager.Gen_ClaimEnergyGoldHotTime(Manager.ClaimEXPGoldStepsList[Manager.sClaim_3rdEXP_3rdGold])
        KRCommon.Gen_DoStory(Settings.Story[Settings.Story_sAutoRepeatAtChapter])

    Manager.Trace1("DoAllDailies will run for {0}".format(Manager.GetString_TotalRunTime_HMSFormat()))
    
def _ExecuteSingleDailyFunction(i_sDailyFunctionName):
    if Settings.DoAllDailies_sLaunchKingsRaidAndGoToMainScreen == i_sDailyFunctionName:
        KRCommon.Gen_LaunchKingsRaidAndGoToMainScreen()

    elif Settings.DoAllDailies_sClaimMailbox == i_sDailyFunctionName:
        KRCommon.Gen_ClaimMailbox()

    elif Settings.DoAllDailies_sExchangeAmity == i_sDailyFunctionName:
        Gen_ExchangeAmity()

    elif Settings.DoAllDailies_sClearInventory == i_sDailyFunctionName:
        KRCommon.Gen_ClearInventory()

    elif Settings.DoAllDailies_sStockade == i_sDailyFunctionName:
        Gen_Stockade(False)

    elif Settings.DoAllDailies_sTowerOfOrdeals == i_sDailyFunctionName:
        Gen_DoTowerOfOrdeals()

    elif Settings.DoAllDailies_sHerosInn == i_sDailyFunctionName:
        KRCommon.Gen_NavigateToMain('portal_orvel_herosinn', False)
        Gen_Daily_HerosInn(True)

    elif Settings.DoAllDailies_sUpperDungeon == i_sDailyFunctionName:
        UpperDungeon.gen_upper_dungeon()

    elif Settings.DoAllDailies_sArena == i_sDailyFunctionName:
        KRCommon.Gen_NavigateToMain('portal_orvel_arena', False)
        Gen_Arena()

    elif Settings.DoAllDailies_sWorldBoss == i_sDailyFunctionName:
        Gen_WorldBoss()

    elif Settings.DoAllDailies_sClaim_1stEXPNGold == i_sDailyFunctionName:
        Manager.Gen_ClaimEnergyGoldHotTime(Manager.ClaimEXPGoldStepsList[Manager.sClaim_1stEXP_1stGold])

    elif Settings.DoAllDailies_sAncientRoyalVault == i_sDailyFunctionName:
        Gen_AncientRoyalVault()

    elif Settings.DoAllDailies_sConquest == i_sDailyFunctionName:
        Conquest.gen_conquest()

    elif Settings.DoAllDailies_sClaim_2ndEXPNGoldWStamina == i_sDailyFunctionName:
        Manager.Gen_ClaimEnergyGoldHotTime(Manager.ClaimEXPGoldStepsList[Manager.sClaim_2ndEXPNGoldWStamina])

    elif Settings.DoAllDailies_sDoStory_UptoInventoryManagement == i_sDailyFunctionName:
        KRCommon.Gen_DoStory(Settings.Story[Settings.Story_sAutoRepeatAtChapter], False)

    elif Settings.DoAllDailies_sDoDragonRaid == i_sDailyFunctionName:
        DragonRaid.Gen_DoDragonRaid()

    elif Settings.DoAllDailies_sDoDragonRaid_Leader == i_sDailyFunctionName:
        DragonRaid.Gen_DoDragonRaid_Leader()

    elif Settings.DoAllDailies_sDoDragonRaid_Member == i_sDailyFunctionName:
        DragonRaid.Gen_DoDragonRaid_Member()

    elif Settings.DoAllDailies_sClaim_3rdEXP_3rdGold == i_sDailyFunctionName:
        Manager.Gen_ClaimEnergyGoldHotTime(Manager.ClaimEXPGoldStepsList[Manager.sClaim_3rdEXP_3rdGold])

    elif Settings.DoAllDailies_sClaimDailyMission == i_sDailyFunctionName:
        KRCommon.Gen_ClaimDailyMission(6, True)

    elif Settings.DoAllDailies_sClaim_4thEXP_4thdGold == i_sDailyFunctionName:
        Manager.Gen_ClaimEnergyGoldHotTime(Manager.ClaimEXPGoldStepsList[Manager.sClaim_4thEXP_4thGold])

    elif Settings.DoAllDailies_sDoSpecialEvent == i_sDailyFunctionName:
        _Gen_DoSpecialEvent__UNUSED()

    elif Settings.DoAllDailies_sKillKingsRaid == i_sDailyFunctionName:
        KRCommon.KillKingsRaid()

    elif -1 < i_sDailyFunctionName.find(Settings.DoAllDailies_sWait):
        Gen_DoWaitSecs(i_sDailyFunctionName)

def Gen_DoWaitSecs(i_sWaitText):
    # Trim off words
    sWaitDuration = i_sWaitText.replace(Settings.DoAllDailies_sWait, "")
    sWaitDuration = sWaitDuration.replace(Settings.DoAllDailies_sSecs, "")

    Manager.wait_secs(int(sWaitDuration))

def Gen_DoTowerOfOrdeals():
    nTowerOfOrdealsPagesToClose = 0

    # Navigate to Hall of Heroes    
    Manager.click_button_msecs('main_portal', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('ch1_upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # This has to wait longer because we are transiting to another big game screen    
    Manager.click_button_secs('minipopup_confirmbutton', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])
    Manager.click_button_msecs('main_portal', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('portal_hallofheroes', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])

    # Enter from outside at Hall of Heroes
    Manager.click_button_msecs('bigicon_lowerright_bottom', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    nTowerOfOrdealsPagesToClose += 1

    # At "Hall of Heroes" first page
    Manager.click_button_msecs('towerofordeals_enter', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    nTowerOfOrdealsPagesToClose += 1

    # At "Get ready for battle" page
    Manager.click_button_msecs('towerofordeals_getreadyforbattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    # Heroes select
    KRSelect.Gen_SelectQuestHero(KRSelect.QuestType_TowerOfOrdeals, False, Settings.Main_sEasyContent)

    # At "Heroes select" page, Start battles
    Manager.click_button_msecs('towerofordeals_heroselect_startbattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('selectbattle_continuousbattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('notice_continuousbattle_ok', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    Manager.wait_secs(Settings.TowerOfOrdeals[Settings.TowerOfOrdeals_sTotalTimeForAllBattles_s])

    # Loot level 25 completion translucent screen - Click anywhere to close
    # We choose close button for the case where it failed to complete all 25 levels of battles
    Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    # Exit
    Manager.click_button_secs('battlecompletion_exit', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])

    # Exit to main game screen
    for j in range(0, nTowerOfOrdealsPagesToClose):
        # main_backbutton didn't work
        Manager.click_button_msecs('towerofordeals_back', Settings.Main[Settings.Main_sDurationAfterClick_ms])

# UNUSED
def _Gen_DoSpecialEvent__UNUSED():
    SpecialEventPagesOpened = 0

    # Navigate to stockade the hard way
    KRCommon.Gen_NavigateToMain('portal_orvel_centralorvel', False)
    SpecialEventPagesOpened += 1
    
    Manager.click_button_msecs('specialevent_enterdungeon', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    SpecialEventPagesOpened += 1

    # loop these to get to autobattle screen
    for i in range (0, 2) :
        Manager.click_button_msecs('stockade_engage_leftmost', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
        Manager.click_button_msecs('stockade_engage_middle_ok_autobattle', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
        Manager.click_button_msecs('stockade_engage_rightmost', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])

    # Select heroes
    KRSelect.Gen_SelectQuestHero(KRSelect.QuestType_SpecialEvent, False, Settings.Main_sEasyContent)

    # Click autobattle
    Manager.click_button_msecs('getreadyforbattle_autorepeat', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
    # ok to notice popup
    nTimeToWait_s = Settings.SpecialEvent[Settings.SpecialEvent_sNoOfKeys] * Settings.SpecialEvent[Settings.SpecialEvent_sSingleBattleDuration_s]
    Manager.click_button_secs('minipopup_confirmbutton', nTimeToWait_s)
    
    # Finish autobattle
    # click close on Loot (Just in case)
    Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # click close on Notice : Auto repeat has ended due to insufficient tickets
    Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # click close on Notice : Festival entry ticket is lacking
    Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # Same exit button as conquest, this will take longer time to load
    Manager.click_button_secs('exit_conquest', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])

    # Exit to main game screen
    for j in range(0, SpecialEventPagesOpened):
        Manager.click_button_msecs('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])

def Gen_WorldBoss():
    pagesOpened = 0
    Manager.click_button_msecs('main_worldboss', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    pagesOpened += 1
        
    for i in range (0, Settings.WorldBoss[Settings.WorldBoss_sNoOfKeys]):
        Manager.click_button_msecs('getreadyforbattle_startbattle', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        # Select Sub team page
        Manager.click_button_msecs('getreadyforbattle_startbattle', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        # Start battle
        Manager.click_button_msecs('getreadyforbattle_startbattle', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        Manager.wait_secs(Settings.WorldBoss[Settings.WorldBoss_sSingleBattleDuration_s])
        Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        Manager.click_button_secs('battlecompletion_exit', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])

    for i in range (0, pagesOpened) :
        KRCommon.Back()

def Gen_AncientRoyalVault() :
    KRCommon.Gen_NavigateToMain('portal_orvel_orvelcastle', False)
    pagesOpened = 0
    waitTillVaultFinish_s = Settings.Vault[Settings.Vault_sNumOfKeysToday] * Settings.Vault[Settings.Vault_sLongestRunTime_s]

    pagesOpened += 1
    Manager.click_button_msecs('vault_enterancient', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    pagesOpened += 1

    # 1) Drag to correct level
    nNoOfLevelsOnOnePage = 4
    nCurrentLevelToPlay = Settings.Vault[Settings.Vault_sHighestClearedFloor]    
    # Determine number of times to drag
    nTopToCurrent = Vault_TopLevel - nCurrentLevelToPlay
    nNoOfPagesToDrag = int(nTopToCurrent / nNoOfLevelsOnOnePage)
    nNoOfSingleLevelToDrag = (nNoOfPagesToDrag * nNoOfLevelsOnOnePage) + (nTopToCurrent % nNoOfLevelsOnOnePage)    
    # Drag to top (+ 1 just to ensure we really drag to top pixel)
    for i in range (0, nNoOfPagesToDrag+1) :
        Manager.mouse_drag_msecs('vault_floor1_top',
                                 'vault_floor4_bottom',
                                 Settings.Main[Settings.Main_sDurationAfterClick_ms],
                                 0.35,
                                 15)
    # Drag (1 level at a time) to highest cleared level
    for i in range (0, nNoOfSingleLevelToDrag) :
        Manager.mouse_drag_msecs('vault_floor2',
                                 'vault_floor1_top',
                                 Settings.Main[Settings.Main_sDurationAfterClick_ms],
                                 0.35,
                                 15)
    # Click the top position (offset click position = 40 pix)
    Manager.click_button_msecs('vault_floor1_top', Settings.Main[Settings.Main_sDurationAfterClick_ms], True, 30)

    # 2) Get ready and battle
    Manager.click_button_msecs('vault_enterancient_getready', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('getreadyforbattle_autorepeat', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_secs('minipopup_confirmbutton', waitTillVaultFinish_s)

    # 3) Done
    # Close Notice : Auto repeat has ended..
    Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # Close Notice : Royal treasury key is lacking
    Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    # Close game screen "battle completion". This should wait at least 10 secs for full game screen to load
    Manager.click_button_secs('battlecompletion_exit', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])

    for i in range (0, pagesOpened) :
        Manager.click_button_msecs('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])

# Stockade helper
def GetStockadeClaimSkillBook(i_SkillBookToClaim) :
    switchSkills = {
        1 : 'stockade_engage_claimskill1',
        2 : 'stockade_engage_claimskill2',
        3 : 'stockade_engage_claimskill3',
        4 : 'stockade_engage_claimskill4'
    }
    return switchSkills.get(i_SkillBookToClaim, "stockade_engage_claimskill4")

# Stockade dailies
def Gen_Stockade(i_EnterFromArena) :
    StockadePagesOpened = 0

    if True == i_EnterFromArena :        
        # Since we just finished Arena, we should be standing outside Arena in main game screen
        Manager.click_button_msecs('stockade_clickfromarena', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    else :
        # Navigate to stockade the hard way
        KRCommon.Gen_NavigateToMain('portal_orvel_stockade', False)
    
    Manager.click_button_msecs('prepare_battle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    StockadePagesOpened += 1
    Manager.click_button_msecs('stockade_enter', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
    StockadePagesOpened += 1
    # loop these to get to autobattle screen
    for i in range (0, 3) :
        Manager.click_button_msecs('stockade_engage_leftmost', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
        Manager.click_button_msecs('stockade_engage_middle_ok_autobattle', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
        Manager.click_button_msecs('stockade_engage_rightmost', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])

    # Select heroes
    KRSelect.Gen_SelectQuestHero(KRSelect.QuestType_Stockade, False, Settings.Main_sEasyContent)

    # Click autobattle
    Manager.click_button_msecs('stockade_engage_autobattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
    # Select which skill books to claim
    skillbooktoclaim = GetStockadeClaimSkillBook(Settings.Stockade[Settings.Stockade_sClaimSkillBook])
    Manager.click_button_msecs(skillbooktoclaim, Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # ok for skill book selected
    Manager.click_button_msecs('stockade_engage_ok', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # ok to notice popup
    Manager.click_button_msecs('stockade_engage_ok', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
    # Finish autobattle
    Manager.wait_secs(Settings.Stockade[Settings.Stockade_sSingleBattleDuration_s] * Settings.Stockade[Settings.Stockade_sMaxKeys])
    Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # Same exit button as conquest, this will take longer time to load
    Manager.click_button_secs('exit_conquest', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])

    # Exit to main game screen
    for j in range(0, StockadePagesOpened):
        Manager.click_button_msecs('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    # Start from Leftmost
    #drag_screen_to_leftmost('stockade_engage_leftmost', 'stockade_engage_rightmost')

# Arena dailies
def Gen_Arena() :
    ArenaPagesOpened = 0
    Manager.click_button_msecs('arena_select', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    ArenaPagesOpened += 1
    Manager.click_button_msecs('arena_select_lov', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    ArenaPagesOpened += 1
    Manager.click_button_msecs('arena_select_ready', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    ArenaPagesOpened += 1
    # After started, the match begins immediately
    Manager.click_button_msecs('arena_select_start', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # NOTE: This esc button press is just in case we have "The match is deactivated" message
    KRCommon.Back()
    Manager.wait_secs(Settings.Arena[Settings.Arena_sMatchDuration_s])

    # Arena competing
    for i in range(0, Settings.Arena[Settings.Arena_sNoOfMatches]) :
        # First click: just in case we level up
        Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
        Manager.click_button_msecs('arena_select_start_retry', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Close pop up "Arena ticket is lacking"
        Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Close pop up "You have used up all the tickets for Arena"
        Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        Manager.wait_secs(Settings.Arena[Settings.Arena_sMatchDuration_s])

    # Just to be safe wait another Match duration in case another match has started
    Manager.wait_secs(Settings.Arena[Settings.Arena_sMatchDuration_s])
    
    # Close pop up "Arena ticket is lacking"
    Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # Close pop up "You have used up all the tickets for Arena"
    Manager.click_button_msecs('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    # Arena competing done
    Manager.click_button_secs('arena_select_start_exit', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime_s])
    
    # Exit to main game screen
    for j in range(0, ArenaPagesOpened) :
        Manager.click_button_msecs('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
# Hero's inn dailies
def Gen_Daily_HerosInn(i_WaitForReceivingNewHero) :
    HerosInnMAX = int(6)
    HerosInnRouletteDuration_ms = 10000
    HerosInnPagesOpened = 0

    Manager.click_button_msecs('herosinn_visit', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    HerosInnPagesOpened += 1

    # Click away max affinity
    Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    Manager.click_button_msecs('herosinn_visit_greet', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('herosinn_visit_conversate', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
    if True == i_WaitForReceivingNewHero :
        # Click and wait till Hero receive animation finishes
        Manager.click_button_secs('herosinn_visit_gift', Settings.Main[Settings.Main_sReceiveNewHeroDuration_s])
        # Click again to close new hero window
        Manager.click_button_msecs('herosinn_visit_gift', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
    else :
        Manager.click_button_msecs('herosinn_visit_gift', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    Manager.click_button_msecs('herosinn_visit_minigame', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    HerosInnPagesOpened += 1
    
    # Row roulette
    for i in range (0, HerosInnMAX) :
        Manager.click_button_msecs('herosinn_visit_minigame_start', HerosInnRouletteDuration_ms)
        Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    # Close Roulette of fortune popup    
    Manager.click_button_msecs('translucentpopup_close', HerosInnRouletteDuration_ms)

    # return to main game page
    for j in range (0, HerosInnPagesOpened) :
        Manager.click_button_msecs('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])

def Gen_DefaultData() :
    Settings.WriteDefaultSettingsFile()
    
def Gen_ExchangeAmity() :
    Manager.click_button_msecs('main_friend', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    Manager.click_button_msecs('exchange_amity', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    # click anywhere jus in case nothing to claim
    Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    #Manager.click_button_msecs('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    KRCommon.Back()

# UNUSED mouse helper
def drag_screen_to_leftmost (i_StartPosition, i_EndPosition, i_NumOfTimesToDrag=3) :
    for i in range (0, i_NumOfTimesToDrag) :
        Manager.mouse_drag_msecs(i_StartPosition,
                                 i_EndPosition,
                                 Settings.Main[Settings.Main_sDurationAfterClick_ms])
