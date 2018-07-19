import nox
import Settings

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
