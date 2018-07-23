import nox
import Common
import Inventory
import Settings
import Manager
import KRCommon
import KRSelect

# TODO REMOVE THIS
import UpperDungeon
import Conquest
import Campaign

Vault_Top3Level = 43

# Main code to do all dailies
def Gen_DoAllDailies() :
    
    # Read our settings file
    Settings.ReadFromFile()

    KRCommon.Gen_LaunchKingsRaidAndGoToMainScreen()
    
    KRCommon.Gen_ClaimMailbox()
    Gen_ExchangeAmity()
    KRCommon.Gen_ClearInventory()

    Gen_Stockade(False) 

    KRCommon.Gen_NavigateToMain('portal_orvel_herosinn', False)
    Gen_Daily_HerosInn(False)
    UpperDungeon.gen_upper_dungeon()

    KRCommon.Gen_NavigateToMain('portal_orvel_arena', False) # True)
    Gen_Arena()
    Gen_WorldBoss()
    #TODO Remove this .. #UpperDungeon.gen_upper_dungeon()
    
    KRCommon.Gen_NavigateToMain('portal_orvel_orvelcastle', False)
    KRCommon.Back()
    Manager.Gen_ClaimEnergyGoldHotTime(Manager.ClaimEXPGoldStepsList[Manager.sClaim_1stEXP_1stGold])
    Gen_AncientRoyalVault()

    Conquest.gen_conquest()

    Manager.Gen_ClaimEnergyGoldHotTime(Manager.ClaimEXPGoldStepsList[Manager.sClaim_BonusStamina_BonusGold])
    KRCommon.Gen_DoStory(Settings.Main[Settings.Main_sAutoStory_AtChapter])
    KRCommon.Gen_ClaimDailyMission(6, True)

    Manager.PrintTotalRunTime()
    print ("NOTES:")
    print ("- Main story and conquest share same hero selection list")

    # TEST CODES

def Gen_DoLaunchNOX_DragonRaid() :
    _Gen_DoLaunchNOX_DoQuest(True)
    
def Gen_DoLaunchNOX_Story() :
    _Gen_DoLaunchNOX_DoQuest(False)

# Either do story / dragon raids
def _Gen_DoLaunchNOX_DoQuest(i_bIsDragonRaid = True) :

    # Read our settings file
    Settings.ReadFromFile()

    KRCommon.Gen_LaunchKingsRaidAndGoToMainScreen()
    KRCommon.Gen_ClaimMailbox()
    Gen_ExchangeAmity()
    KRCommon.Gen_ClaimDailyMission()
    KRCommon.Gen_ClearInventory()

    if i_bIsDragonRaid :
        KRCommon.Gen_DoDragonRaid()
    else :
        # Claim some energy 
        Manager.Gen_ClaimEnergyGoldHotTime(Manager.ClaimEXPGoldStepsList[Manager.sClaim_3rdEXP_3rdGold])
        KRCommon.Gen_DoStory(Settings.Main[Settings.Main_sAutoStory_AtChapter])

    Manager.PrintTotalRunTime()

def Gen_WorldBoss():
    pagesOpened = 0
    Manager.click_button('main_worldboss', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    pagesOpened += 1
        
    for i in range (0, Settings.WorldBoss[Settings.WorldBoss_sNoOfKeys]):
        Manager.click_button('getreadyforbattle_startbattle', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Select Sub team page
        Manager.click_button('getreadyforbattle_startbattle', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Start battle
        Manager.click_button('getreadyforbattle_startbattle', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.wait(Settings.WorldBoss[Settings.WorldBoss_sSingleBattleDuration] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('battlecompletion_exit', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    for i in range (0, pagesOpened) :
        KRCommon.Back()

def Gen_AncientRoyalVault() :
    pagesOpened = 0
    waitTillVaultFinish = Settings.Vault[Settings.Vault_sNumOfKeysToday] * Settings.Vault[Settings.Vault_sLongestRunTime]

    pagesOpened += 1
    Manager.click_button('vault_enterancient', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    pagesOpened += 1
    if Vault_Top3Level > Settings.Vault[Settings.Vault_sHighestClearedFloor] :
        Manager.click_button('vault_enterancient_selectlowerfloor', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('vault_enterancient_getready', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('getreadyforbattle_autorepeat', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('minipopup_confirmbutton', waitTillVaultFinish)

    # Close Notice : Auto repeat has eneded..
    Manager.click_button('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Close Notice : Royal treasury key is lacking
    Manager.click_button('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Close game screen "battle completion". This should wait at least 10 secs for full game screen to load
    Manager.click_button('battlecompletion_exit', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    for i in range (0, pagesOpened) :
        Manager.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

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
        Manager.click_button('stockade_clickfromarena', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    else :
        # Navigate to stockade the hard way
        KRCommon.Gen_NavigateToMain('portal_orvel_stockade', False)
    
    Manager.click_button('prepare_battle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    StockadePagesOpened += 1
    Manager.click_button('stockade_enter', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    StockadePagesOpened += 1
    # loop these to get to autobattle screen
    for i in range (0, 4) :
        Manager.click_button('stockade_engage_leftmost', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('stockade_engage_middle_ok_autobattle', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('stockade_engage_rightmost', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Click autobattle
    Manager.click_button('stockade_engage_autobattle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    # Select which skill books to claim
    skillbooktoclaim = GetStockadeClaimSkillBook(Settings.Stockade[Settings.Stockade_sClaimSkillBook])
    Manager.click_button(skillbooktoclaim, Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # ok for skill book selected
    Manager.click_button('stockade_engage_ok', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # ok to notice popup
    Manager.click_button('stockade_engage_ok', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    # Finish autobattle
    nox.wait(Settings.Stockade[Settings.Stockade_sSingleBattleDuration] * 5)
    Manager.click_button('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('minipopup_closebutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Same exit button as conquest, this will take longer time to load
    Manager.click_button('exit_conquest', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Exit to main game screen
    for j in range(0, StockadePagesOpened):
        Manager.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Start from Leftmost
    #drag_screen_to_leftmost('stockade_engage_leftmost', 'stockade_engage_rightmost')

# Arena dailies
def Gen_Arena() :
    ArenaPagesOpened = 0
    Manager.click_button('arena_select', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    ArenaPagesOpened += 1
    Manager.click_button('arena_select_lov', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    ArenaPagesOpened += 1
    Manager.click_button('arena_select_ready', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    ArenaPagesOpened += 1
    # After started, the match begins immediately
    Manager.click_button('arena_select_start', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # NOTE: This esc button press is just in case we have "The match is deactivated" message
    KRCommon.Back()
    Manager.wait(Settings.Arena[Settings.Arena_sMatchDuration] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Arena competing
    for i in range(0, Settings.Arena[Settings.Arena_sNoOfMatches]) :
        # First click: just in case we level up
        Manager.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('arena_select_start_retry', Settings.Arena[Settings.Arena_sMatchDuration] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Arena competing done
    Manager.click_button('arena_select_start_exit', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    # Exit to main game screen
    for j in range(0, ArenaPagesOpened) :
        Manager.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
# Hero's inn dailies
def Gen_Daily_HerosInn(i_WaitForReceivingNewHero) :
    HerosInnMAX = int(15)
    HerosInnRouletteDuration = 7000
    HerosInnPagesOpened = 0

    Manager.click_button('herosinn_visit', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    HerosInnPagesOpened += 1
    Manager.click_button('herosinn_visit_greet', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('herosinn_visit_conversate', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    if True == i_WaitForReceivingNewHero :
        # Click and wait till Hero receive animation finishes
        Manager.click_button('herosinn_visit_gift', Settings.Main[Settings.Main_sReceiveNewHeroDuration] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Click again to close new hero window
        Manager.click_button('herosinn_visit_gift', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    else :
        Manager.click_button('herosinn_visit_gift', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    Manager.click_button('herosinn_visit_minigame', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    HerosInnPagesOpened += 1
    
    # Row roulette
    for i in range (1, HerosInnMAX) :
        Manager.click_button('herosinn_visit_minigame_start', HerosInnRouletteDuration + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Close Roulette of fortune popup    
    Manager.click_button('translucentpopup_close', HerosInnRouletteDuration + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # return to main game page
    for j in range (0, HerosInnPagesOpened) :
        Manager.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

def Gen_DefaultData() :
    Settings.WriteDefaultSettingsFile()
    
def Gen_ExchangeAmity() :
    Manager.click_button('main_friend', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('exchange_amity', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # click anywhere jus in case nothing to claim
    Manager.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    #Manager.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    KRCommon.Back()

# UNUSED mouse helper
def drag_screen_to_leftmost (i_StartPosition, i_EndPosition, i_NumOfTimesToDrag=3) :
    for i in range (0, i_NumOfTimesToDrag) :
        nox.mouse_drag( i_StartPosition,
                        i_EndPosition,
                        Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
