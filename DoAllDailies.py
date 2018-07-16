import nox
import Common
import Inventory
import Settings

# TODO REMOVE THIS
import UpperDungeon
import Conquest
import Campaign

Vault_Top3Level = 43

# Main code to do all dailies
def Gen_DoAllDailies() :
    #TODO - Remove this and make this one of the options
    #Settings.WriteDefaultSettingsFile()

    # Read our settings file
    Settings.ReadFromFile()

    Gen_LaunchKingsRaidAndGoToMainScreen()
    Gen_ClaimMailbox()
    Gen_ExchangeAmity()
    Gen_ClearInventory()
    Gen_NavigateToMain('portal_orvel_herosinn')
    Gen_Daily_HerosInn(False)
    Gen_NavigateToMain('portal_orvel_arena', True)
    Gen_Arena()
    #Gen_Stockade(True)
    UpperDungeon.gen_upper_dungeon()
    Gen_ClaimEnergyGotHotTime_FromUntouched()
    Gen_NavigateToMain('portal_orvel_orvelcastle', True)
    Gen_AncientRoyalVault()
    Conquest.gen_conquest()
    Gen_ClaimDailyMission()
    #Gen_GoToDragonRaid()
    Gen_AutoRepeatStoryChapter(8)
    
    # TEST CODES
    #Gen_RestartToDragonRaid()
    #Gen_SelectHero(False, Settings.Main_sEasyContent)
    #UpperDungeon.gen_single_upper_dungeon('ch8_upper_dungeon', 
    #                                      Settings.Main[Settings.Main_sTransitionDuration_Alter],
    #                                      Settings.Main_sHardContent)

def Gen_DoLaunchNOX_DragonRaid() :
    Settings.WriteDefaultSettingsFile()

    # Read our settings file
    Settings.ReadFromFile()

    Gen_LaunchKingsRaidAndGoToMainScreen()
    Gen_ClaimMailbox()
    Gen_ClaimDailyMission()
    Gen_ExchangeAmity()
    Gen_ClearInventory()
    #Gen_ClaimEnergyGotHotTime_FromUntouched()
    Gen_GoToDragonRaid()

def Gen_AutoRepeatStoryChapter(i_sWhichChapter = 8) :
    # Navigate to chapter
    # currently only support chapter 8
    if 8 <= i_sWhichChapter :
        Common.Gen_GoToChapter('conquests', 'ch8_conquest', Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('ch8_conquest_naviTo_story_8_20', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('ch8_conquest_naviTo_story_8_25', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('ch8_conquest_naviTo_story_8_24', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('ch8_conquest_naviTo_story_8_23', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('ch8_conquest_naviTo_story_8_23_2', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # 
    nox.click_button('main_preparebattle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('get_ready_for_battle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # For now we use Conquests Hero selection for story as well
    Gen_SelectHero(False, Settings.Main_sEasyContent)

    Campaign.gen_natural_stamina_farm()

# Assumes NOTHING is claimed yet when game just restarted a new day
def Gen_ClaimEnergyGotHotTime_FromUntouched() :
    nox.click_button('main_mission', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('mission_tab_eventmission', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Claim Today's Bonus Gold
    nox.click_button('mission_claim_position2', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Claim EXP hot time (first)
    nox.click_button('mission_claim_position2', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Claim Gold hot time (first)
    nox.click_button('mission_claim_position3', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Back to main
    nox.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

# Doesn't really matter the order at which we claim
def Gen_ClaimDailyMission (i_nNumOfMissionsToClaim = 6) :
    nox.click_button('main_mission', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    for i in range(0, i_nNumOfMissionsToClaim) :
        nox.click_button('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Back to main
    nox.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

def Gen_AncientRoyalVault() :
    pagesOpened = 0
    waitTillVaultFinish = Settings.Vault[Settings.Vault_sNumOfKeysToday] * Settings.Vault[Settings.Vault_sLongestRunTime]

    pagesOpened += 1
    nox.click_button('vault_enterancient', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    pagesOpened += 1
    if Vault_Top3Level > Settings.Vault[Settings.Vault_sHighestClearedFloor] :
        nox.click_button('vault_enterancient_selectlowerfloor', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('vault_enterancient_getready', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('getreadyforbattle_autorepeat', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('minipopup_confirmbutton', waitTillVaultFinish)

    # Close Notice : Auto repeat has eneded..
    nox.click_button('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Close Notice : Royal treasury key is lacking
    nox.click_button('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Close game screen "battle completion"
    nox.click_button('battlecompletion_exit', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    for i in range (0, pagesOpened) :
        nox.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

def Gen_GoToDragonRaid () :
    whichDragonRaid = Settings.DragonRaidConfig[Settings.DragonRaidConfig_sSelectDragonToAuto]

    nox.click_button('raid_multi', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('raid_select', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # room settings
    # select correct dragon
    roomSelect = 'raid_select_black'
    if Settings.Fire_DragonRaid_sFireDragonRaid == whichDragonRaid :
        roomSelect = 'raid_select_fire'
        DragonSettings = Settings.Fire_DragonRaid.copy()
    elif Settings.Frost_DragonRaid_sFrostDragonRaid == whichDragonRaid :
        roomSelect = 'raid_select_frost'
        DragonSettings = Settings.Frost_DragonRaid.copy()
    elif Settings.Poison_DragonRaid_sPoisonDragonRaid== whichDragonRaid :
        roomSelect = 'raid_select_poison'
        DragonSettings = Settings.Poison_DragonRaid.copy()
    elif Settings.Black_DragonRaid_sBlackDragonRaid == whichDragonRaid :
        DragonSettings = Settings.Black_DragonRaid.copy()
        nox.mouse_drag('raid_select_list_bottom', 'raid_select_list_top', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Click to select the correct dragon room
    nox.click_button(roomSelect, Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # calculate how many levels to decrement
    differenceFromHighestClearedToAutoLevel = abs(DragonSettings[Settings.DragonRaid_sHighestCleared] - DragonSettings[Settings.DragonRaid_sAutoAtThisLevel])
    for i in range (0, differenceFromHighestClearedToAutoLevel) :
        nox.click_button('raid_select_decrementlevel', Settings.Main[Settings.Main_sDurationAfterClick_Short])
    # uncheck gather raiders
    nox.click_button('raid_select_gatherraiders', Settings.Main[Settings.Main_sDurationAfterClick_Short])
    nox.click_button('raid_select_enter', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    Gen_DragonRaid_HeroSelect()

    nox.click_button('raid_select_SetAutoRepeat', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('raid_select_StartBattle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    

# TODO Put to common
def Gen_SelectHero (i_bNavigateToHeroSelectScreen, i_sEasyOrHardContent, i_bExitBackToMainPage = False) :
    pagesOpened = 0

    # Navigate to upper dungeon
    if i_bNavigateToHeroSelectScreen :        
        nox.click_button('main_portal', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('ch1_upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # This has to wait longer because we are transiting to another big game screen    
        nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

        # Go to Heroes selection screen
        nox.click_button('main_preparebattle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        pagesOpened += 1
        nox.click_button('get_ready_for_battle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        pagesOpened += 1

    # Deselect all heroes
    nox.click_button('main_HeroList_DeselectPosition', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('main_HeroList_DeselectPosition', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('main_HeroList_DeselectPosition', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('main_HeroList_DeselectPosition', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    SelectedHeroPosition_Easy = {
        1 : Settings.Conquest[Settings.Main_sEasy_Hero1_Position],
        2 : Settings.Conquest[Settings.Main_sEasy_Hero2_Position],
        3 : Settings.Conquest[Settings.Main_sEasy_Hero3_Position],
        4 : Settings.Conquest[Settings.Main_sEasy_Hero4_Position]
    }
    SelectedHeroPosition_Hard = {
        1 : Settings.Conquest[Settings.Main_sHard_Hero1_Position],
        2 : Settings.Conquest[Settings.Main_sHard_Hero2_Position],
        3 : Settings.Conquest[Settings.Main_sHard_Hero3_Position],
        4 : Settings.Conquest[Settings.Main_sHard_Hero4_Position]
    }
    ClickHeroPosition = {
        1 : 'main_HeroList_Position1',
        2 : 'main_HeroList_Position2',
        3 : 'main_HeroList_Position3'
    }

    # First row icon half height  = (428-144)/2 = 142
    # Top of first row icon = 144
    # Half position of 2nd row icon = 433+142 = 575
    if Settings.Main_sEasyContent == i_sEasyOrHardContent :
        _Gen_SelectHero(4, 3, SelectedHeroPosition_Easy, ClickHeroPosition, 'main_HeroList_Position4', 'main_HeroList_Position1')
    else :
        _Gen_SelectHero(4, 3, SelectedHeroPosition_Hard, ClickHeroPosition, 'main_HeroList_Position4', 'main_HeroList_Position1')

    if i_bExitBackToMainPage :
        # Exit to main game screen
        for i in range(0, pagesOpened):
            nox.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

# Dragon Raid hero selection:
# The numbering goes like this
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# 10, 11, 12
# 13, 14, 15
# 16, 17, 18
# 19, 20, 21
# 22, 23, 24
# 25, 26, 27
# Character select in Dragon Raid
def Gen_DragonRaid_HeroSelect() :
    SelectedHeroPosition = {
        1 : Settings.DragonRaidConfig[Settings.DragonRaidConfig_sHero1_Position],
        2 : Settings.DragonRaidConfig[Settings.DragonRaidConfig_sHero2_Position],
        3 : Settings.DragonRaidConfig[Settings.DragonRaidConfig_sHero3_Position],
        4 : Settings.DragonRaidConfig[Settings.DragonRaidConfig_sHero4_Position]
    }
    ClickHeroPosition = {
        1 : 'raid_select_HeroList_Position1',
        2 : 'raid_select_HeroList_Position2',
        3 : 'raid_select_HeroList_Position3'
    }
    _Gen_SelectHero(4, 3, SelectedHeroPosition, ClickHeroPosition, 'raid_select_HeroList_Position4', 'raid_select_HeroList_Position1')

def _Gen_SelectHero( i_MaxHeroesAllowed,
                    i_MaxHeroesIn1Row,
                    i_lSelectedHeroPosition,
                    i_lClickHeroPosition,
                    i_sDragFromPosition,
                    i_sDragToPosition) :
    modSelectedHeroPosition = 1
    dragCount = 0
    for i in range (0, i_MaxHeroesAllowed) :
        numOfLevelsToDrag = int(i_lSelectedHeroPosition[i+1] / i_MaxHeroesIn1Row)
        modSelectedHeroPosition = i_lSelectedHeroPosition[i+1] % i_MaxHeroesIn1Row

        if 0 == modSelectedHeroPosition :
            modSelectedHeroPosition = i_MaxHeroesIn1Row
            numOfLevelsToDrag -= 1

        print ("i={0}, numOfLevelsToDrag={1}, modSelectedHeroPosition={2}, i_lSelectedHeroPosition[i+1]={3}"
            .format(i, numOfLevelsToDrag, modSelectedHeroPosition, i_lSelectedHeroPosition[i+1]))
        
        # First row icon's half size  = (574-484)/2 = 45
        # Second row icon's half size = (591-574)/2 = 8.5
        # Drag distance = 45 + 8.5 = 53.5
        # Dragon raid has 3 heroes in one row, we will click the selected hero w.r.t 1st row
        if (1 <= numOfLevelsToDrag) and (i_MaxHeroesIn1Row < i_lSelectedHeroPosition[i+1]):  #modSelectedHeroPosition :
            # If selected hero in not in first row, drag list upwards until it is in 1st row
            for j in range (0, numOfLevelsToDrag-dragCount) :
                nox.mouse_drag(i_sDragFromPosition,
                               i_sDragToPosition,
                               Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter],
                               0.3,
                               15)
                dragCount += 1
                print("j={0}, numOfLevelsToDrag={1}, dragCount={2}".format(j, numOfLevelsToDrag, dragCount))
        nox.click_button(i_lClickHeroPosition[modSelectedHeroPosition], Settings.Main[Settings.Main_sDurationAfterClick])

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
    MaxSkillBooksToClaim = 5    # We have only up till 5 now

    if True == i_EnterFromArena :        
        # Since we just finished Arena, we should be standing outside Arena in main game screen
        nox.click_button('stockade_clickfromarena', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    else :
        # Navigate to stockade the hard way
        Gen_NavigateToMain('portal_orvel_stockade')
    
    nox.click_button('prepare_battle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    StockadePagesOpened += 1
    nox.click_button('stockade_enter', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    StockadePagesOpened += 1
    # loop these to get to autobattle screen
    for i in range (0, 4) :
        nox.click_button('stockade_engage_leftmost', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('stockade_engage_middle_ok_autobattle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('stockade_engage_rightmost', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Click autobattle
    nox.click_button('stockade_engage_middle_ok_autobattle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    # Select which skill books to claim
    skillbooktoclaim = GetStockadeClaimSkillBook(Settings.Stockade[Settings.Stockade_sClaimSkillBook])
    nox.click_button(skillbooktoclaim, Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # ok for skill book selected
    nox.click_button('stockade_engage_ok', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # ok to notice popup
    nox.click_button('stockade_engage_ok', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    # Finish autobattle
    nox.wait(Settings.Stockade[Settings.Stockade_sSingleBattleDuration] * 5)
    nox.click_button('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Same exit button as conquest, this will take longer time to load
    nox.click_button('exit_conquest', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Exit to main game screen
    for j in range(0, StockadePagesOpened):
        nox.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Start from Leftmost
    #drag_screen_to_leftmost('stockade_engage_leftmost', 'stockade_engage_rightmost')

# Arena dailies
def Gen_Arena() :
    ArenaPagesOpened = 0
    nox.click_button('arena_select', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    ArenaPagesOpened += 1
    nox.click_button('arena_select_lov', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    ArenaPagesOpened += 1
    nox.click_button('arena_select_ready', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    ArenaPagesOpened += 1
    # After started, the match begins immediately
    nox.click_button('arena_select_start', Settings.Arena[Settings.Arena_sMatchDuration] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Arena competing
    for i in range(0, Settings.Arena[Settings.Arena_sNoOfMatches]) :
        # First click: just in case we level up
        nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('arena_select_start_retry', Settings.Arena[Settings.Arena_sMatchDuration] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Arena competing done
    nox.click_button('arena_select_start_exit', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    # Exit to main game screen
    for j in range(0, ArenaPagesOpened) :
        nox.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
# Hero's inn dailies
def Gen_Daily_HerosInn(i_WaitForReceivingNewHero) :
    HerosInnMAX = int(15)
    HerosInnRouletteDuration = 7000
    HerosInnPagesOpened = 0

    nox.click_button('herosinn_visit', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    HerosInnPagesOpened += 1
    nox.click_button('herosinn_visit_greet', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('herosinn_visit_conversate', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    if True == i_WaitForReceivingNewHero :
        # Click and wait till Hero receive animation finishes
        nox.click_button('herosinn_visit_gift', Settings.Main[Settings.Main_sReceiveNewHeroDuration] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Click again to close new hero window
        nox.click_button('herosinn_visit_gift', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    else :
        nox.click_button('herosinn_visit_gift', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    nox.click_button('herosinn_visit_minigame', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    HerosInnPagesOpened += 1
    
    # Row roulette
    for i in range (1, HerosInnMAX) :
        nox.click_button('herosinn_visit_minigame_start', HerosInnRouletteDuration + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Close Roulette of fortune popup    
    nox.click_button('translucentpopup_close', HerosInnRouletteDuration + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # return to main game page
    for j in range (0, HerosInnPagesOpened) :
        nox.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

# Claim Mailbox
def Gen_ClaimMailbox () :
    # Click mailbox icon
    nox.click_button('main_mailbox', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('mailbox_claimall', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('mailbox_close', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

# Go to main screen after Nox restarted
def Gen_LaunchKingsRaidAndGoToMainScreen () :
    NoOfClicksToClearTranslucentPopups = 3
    # Launch game from Nox screen till Tap to Play screen
    nox.click_button('nox_launchgame', Settings.Main[Settings.Main_sGameLauch_TapToPlayDuration] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Tap to play till main game screen
    nox.click_button('nox_launchgame', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('nox_launchgame', Settings.Main[Settings.Main_sGameLauch_MainGameScreenDuration] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # This will click away main game screen, loading screen, advertisements
    for i in range(0, Settings.Main[Settings.Main_sNoOfClicksToClearAdvertisement]) :
        nox.click_button('main_advertisement_close', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Close translucent popup separately .. don't wait so long to click again
    for i in range(0, NoOfClicksToClearTranslucentPopups) :
        nox.click_button('translucentpopup_close', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Just to be sure - click again to clear advertisement
    for i in range(0, Settings.Main[Settings.Main_sNoOfClicksToClearAdvertisement]) :
        #nox.click_button('translucentpopup_close', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('main_advertisement_close', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

# Clears inventory (Assumes we are at main game screen)
def Gen_ClearInventory() :

    # Click inventory
    nox.click_button('main_inventory', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Grind all (for now)
    Inventory.manage_inventory(True, False)
    # Back to main game screen
    nox.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

def Gen_DefaultData() :
    Settings.WriteDefaultSettingsFile()
    
def Gen_ExchangeAmity() :
    nox.click_button('main_friend', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('exchange_amity', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # click anywhere jus in case nothing to claim
    nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

def Gen_NavigateToMain(i_portal_orvel_placetogo, i_bAlreadyInTown = False) :
    if False == i_bAlreadyInTown :
        nox.click_button('main_portal', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('ch1_upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # This has to wait longer because we are transiting to another big game screen    
        nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    nox.click_button('main_portal', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('portal_orvel', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button(i_portal_orvel_placetogo, Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # This has to wait longer because we are transiting to another big game screen
    nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

# UNUSED mouse helper
def drag_screen_to_leftmost (i_StartPosition, i_EndPosition, i_NumOfTimesToDrag=3) :
    for i in range (0, i_NumOfTimesToDrag) :
        nox.mouse_drag( i_StartPosition,
                        i_EndPosition,
                        Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
