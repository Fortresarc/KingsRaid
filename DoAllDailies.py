import nox
import Common
import Inventory
import Settings

# Main code to do all dailies
def Gen_DoAllDailies() :
    #TODO - Remove this and make this one of the options
    Settings.WriteDefaultSettingsFile()

    # Read our settings file
    Settings.ReadFromFile()

    Gen_LaunchKingsRaidAndGoToMainScreen()
    Gen_ClaimMailbox()
    Gen_ExchangeAmity()
    Gen_ClearInventory()
    Gen_NavigateToMain('portal_orvel_herosinn')
    Gen_Daily_HerosInn(False)
    Gen_NavigateToMain('portal_orvel_arena')
    Gen_Arena()
    Gen_Stockade(True)

# UNUSED mouse helper
def drag_screen_to_leftmost (startposition, endposition, numberoftimestodrag=3) :
    for i in range (0, numberoftimestodrag) :
        nox.mouse_drag( startposition,
                        endposition,
                        Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

# Stockade helper
def GetStockadeClaimSkillBook(i_skilltoclaim) :
    switchSkills = {
        1 : 'stockade_engage_claimskill1',
        2 : 'stockade_engage_claimskill2',
        3 : 'stockade_engage_claimskill3',
        4 : 'stockade_engage_claimskill4'
    }
    return switchSkills.get(i_skilltoclaim, "stockade_engage_claimskill4")

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
    for j in range(1, StockadePagesOpened):
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
def Gen_Daily_HerosInn(i_waitforheroreceive) :
    HerosInnMAX = int(15)
    HerosInnRouletteDuration = 7000
    HerosInnPagesOpened = 0

    nox.click_button('herosinn_visit', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    HerosInnPagesOpened += 1
    nox.click_button('herosinn_visit_greet', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('herosinn_visit_conversate', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    if True == i_waitforheroreceive :
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

def Gen_NavigateToMain(i_portal_orvel_placetogo) :
    nox.click_button('main_portal', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('ch1_upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # This has to wait longer because we are transiting to another big game screen    
    nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    nox.click_button('main_portal', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('portal_orvel', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button(i_portal_orvel_placetogo, Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # This has to wait longer because we are transiting to another big game screen
    nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
