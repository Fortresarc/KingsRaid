import nox
import json
import os
import Manager

SETTINGS_FILENAME                                   = 'settings.json'

# Settings read from file

# TODO : Customizable sequences for doing all dailies
# Do all dailies sequence
DoAllDailies_sDoAllDailies                          = 'DoAllDailiesSequence'
DoAllDailies_sLaunchKingsRaidAndGoToMainScreen      = 'LaunchKingsRaidAndGoToMainScreen'
DoAllDailies_sClaimMailbox                          = 'ClaimMailbox'
DoAllDailies_sExchangeAmity                         = 'ExchangeAmity'
DoAllDailies_sClearInventory                        = 'ClearInventory'
DoAllDailies_sStockade                              = 'Stockade'
DoAllDailies_sHerosInn                              = 'HerosInn'
DoAllDailies_sUpperDungeon                          = 'UpperDungeon'
DoAllDailies_sArena                                 = 'Arena'
DoAllDailies_sWorldBoss                             = 'WorldBoss'
DoAllDailies_sClaim_1stEXPNGold                     = 'Claim_1stEXPNGold'
DoAllDailies_sAncientRoyalVault                     = 'AncientRoyalVault'
DoAllDailies_sConquest                              = 'Conquest'
DoAllDailies_sClaim_2ndEXPNGoldWStamina             = 'Claim_2ndEXPNGoldWStamina'
DoAllDailies_sDoStory_UptoInventoryManagement       = 'DoStory_UptoInventoryManagement'
DoAllDailies_sDoDragonRaid                          = 'DoDragonRaid'
DoAllDailies_sDoDragonRaid_Leader                   = 'DoDragonRaid_Leader'
DoAllDailies_sDoDragonRaid_Member                   = 'DoDragonRaid_Member'
DoAllDailies_sClaim_3rdEXP_3rdGold                  = 'Claim_3rdEXP_3rdGold'
DoAllDailies_sClaimDailyMission                     = 'ClaimDailyMission'
DoAllDailies_sClaim_4thEXP_4thdGold                 = 'Claim_4thEXP_4thdGold'
DoAllDailies_sDoSpecialEvent                        = 'DoSpecialEvent'
DoAllDailies_sKillKingsRaid                         = 'KillKingsRaid'
DoAllDailies_sWait_s                                = 'Wait_secs'
DoAllDailies_sTowerOfOrdeals                        = 'DoTowerOfOrdeals'

# Main
Main_sMain                                          = 'Main'
Main_sResolutionX                                   = 'ResolutionX'
Main_sResolutionY                                   = 'ResolutionY'
Main_sGameLaunch_TapToPlayDuration_s                = 'GameLaunch_TapToPlayDuration_secs'
Main_sGameLaunch_MainGameScreenDuration_s           = 'GameLaunch_MainGameScreenDuration_secs'
Main_sNoOfClicksToClearAdvertisement                = 'NoOfClicksToClearAdvertisement'
Main_sTransitionDuration_ms                         = 'TransitionDuration_msecs'
Main_sDurationAfterClick_ms                         = 'DurationAfterClick_msecs'
Main_sDurationAfterClick_Short_ms                   = 'DurationAfterClick_Short_msecs'
Main_sDurationAfterClick_Long_ms                    = 'DurationAfterClick_Long_msecs'
Main_sAnyGameScreenLoadingTime_s                    = 'AnyGameScreenLoadingTime_secs'
Main_sReceiveNewHeroDuration_s                      = 'ReceiveNewHeroDuration_secs'
Main_sWaitDuration_s                                = 'WaitDuration_secs'
# Conquests and upper dungeons
Main_sEasyContent                                   = "EasyContent"
Main_sHardContent                                   = "HardContent"
Main_sEasy_Hero1_Position                           = 'Easy_Hero1_Position'
Main_sEasy_Hero2_Position                           = 'Easy_Hero2_Position'
Main_sEasy_Hero3_Position                           = 'Easy_Hero3_Position'
Main_sEasy_Hero4_Position                           = 'Easy_Hero4_Position'
Main_sHard_Hero1_Position                           = 'Hard_Hero1_Position'
Main_sHard_Hero2_Position                           = 'Hard_Hero2_Position'
Main_sHard_Hero3_Position                           = 'Hard_Hero3_Position'
Main_sHard_Hero4_Position                           = 'Hard_Hero4_Position'

# Special event
SpecialEvent_sSpecialEvent                          = 'SpecialEvent'
SpecialEvent_sNoOfKeys                              = 'NoOfKeys'
SpecialEvent_sSingleBattleDuration_s                = 'SingleBattleDuration_secs'

# World boss
WorldBoss_sWorldBoss                                = 'WorldBoss'
WorldBoss_sNoOfKeys                                 = 'NoOfKeys'
WorldBoss_sSingleBattleDuration_s                   = 'SingleBattleDuration_secs'

# Ancient royal vault
Vault_sVault                                        = 'Vault'
Vault_sHighestClearedFloor                          = 'HighestClearedFloor'
Vault_sLongestRunTime_s                             = 'LongestRunTime_secs'
Vault_sNumOfKeysToday                               = 'NumOfKeysToday'

# Arena
Arena_sArena                                        = 'Arena'
Arena_sNoOfMatches                                  = 'NoOfMatches'
Arena_sMatchDuration_s                              = 'MatchDuration_secs'

# Stockade
Stockade_sStockade                                  = 'Stockade'
Stockade_sClaimSkillBook                            = 'ClaimSkillBook'
Stockade_sSingleBattleDuration_s                    = 'SingleBattleDuration_secs'
Stockade_sMaxKeys                                   = 'MaxKeys'

# Tower of Ordeals
TowerOfOrdeals_sTowerOfOrdeals                      = 'TowerOfOrdeals'
TowerOfOrdeals_sTotalTimeForAllBattles_s            = 'TotalTimeForAllBattles_secs'

# Story
Story_sStory                                        = 'Story'
Story_sAutoRepeatAtChapter                          = 'AutoRepeatAtChapter'
Story_sUseStaminaPot                                = 'UseStaminaPot'
Story_sLongestRunningTime_s                         = 'LongestRunningTime_secs'
Story_sManageInventoryInterval_m                    = 'ManageInventoryInterval_mins'
Story_sGrindOrSellInventory                         = 'GrindOrSellInventory'

# Conquests
Conquest_sConquest                                  = 'Conquest'
Conquest_sHighestClearedChapter                     = 'HighestClearedChapter'
Conquest_sHardContent_StartsFrom                    = 'HardContent_StartsFrom'
Conquest_sHardContent_NoOfTimesToRetry              = 'HardContent_NoOfTimesToRetry'
Conquest_sLongestRunTime_Chap2_s                    = 'LongestRunTime_Chap2_secs'
Conquest_sLongestRunTime_Chap3_s                    = 'LongestRunTime_Chap3_secs'
Conquest_sLongestRunTime_Chap4_s                    = 'LongestRunTime_Chap4_secs'
Conquest_sLongestRunTime_Chap5_s                    = 'LongestRunTime_Chap5_secs'
Conquest_sLongestRunTime_Chap6_s                    = 'LongestRunTime_Chap6_secs'
Conquest_sLongestRunTime_Chap7_s                    = 'LongestRunTime_Chap7_secs'
Conquest_sLongestRunTime_Chap8_s                    = 'LongestRunTime_Chap8_secs'

# Upper Dungeons
UpperDungeon_sUpperDungeon                          = 'UpperDungeon'
UpperDungeon_sHighestClearedChapter                 = 'HighestClearedChapter'
UpperDungeon_sHardContent_StartsFrom                = 'HardContent_StartsFrom'
UpperDungeon_sHardContent_NoOfTimesToRetry          = 'HardContent_NoOfTimesToRetry'
UpperDungeon_sLongestRunTime_Chap1_s                = 'LongestRunTime_Chap1_secs'
UpperDungeon_sLongestRunTime_Chap2_s                = 'LongestRunTime_Chap2_secs'
UpperDungeon_sLongestRunTime_Chap3_s                = 'LongestRunTime_Chap3_secs'
UpperDungeon_sLongestRunTime_Chap4_s                = 'LongestRunTime_Chap4_secs'
UpperDungeon_sLongestRunTime_Chap5_s                = 'LongestRunTime_Chap5_secs'
UpperDungeon_sLongestRunTime_Chap6_s                = 'LongestRunTime_Chap6_secs'
UpperDungeon_sLongestRunTime_Chap7_s                = 'LongestRunTime_Chap7_secs'
UpperDungeon_sLongestRunTime_Chap8_s                = 'LongestRunTime_Chap8_secs'

# Dragon Raid configuration for all
DragonRaidConfig_sSelectDragonToAuto                = 'SelectDragonToAuto'
DragonRaidConfig_sHero1_Position                    = 'Hero1_Position'
DragonRaidConfig_sHero2_Position                    = 'Hero2_Position'
DragonRaidConfig_sHero3_Position                    = 'Hero3_Position'
DragonRaidConfig_sHero4_Position                    = 'Hero4_Position'
DragonRaidConfig_sCoopLeaderName                    = 'LeaderName'
DragonRaidConfig_sCoopMemberName1                   = 'MemberName1'
DragonRaidConfig_sCoopMemberName2                   = 'MemberName2'
DragonRaidConfig_sCoopMemberName3                   = 'MemberName3'
DragonRaidConfig_sCoopWaitMemberJoin_s              = 'CoopWaitMemberJoin_secs'
DragonRaidConfig_sCoopHero1_Position                = 'CoopHero1_Position'
DragonRaidConfig_sCoopHero2_Position                = 'CoopHero2_Position'
DragonRaidConfig_sCoopHero3_Position                = 'CoopHero3_Position'
DragonRaidConfig_sCoopHero4_Position                = 'CoopHero4_Position'


# Dragon Raid
DragonRaid_sDragonRaidConfig                        = 'DragonRaidConfig'
DragonRaid_sHighestCleared                          = 'HighestCleared'
DragonRaid_sAutoAtThisLevel                         = 'AutoAtThisLevel'
DragonRaid_sCoopAutoAtThisLevel                     = 'Coop_AutoAtThisLevel'
Fire_DragonRaid_sFireDragonRaid                     = 'Fire_DragonRaid'
Frost_DragonRaid_sFrostDragonRaid                   = 'Frost_DragonRaid'
Poison_DragonRaid_sPoisonDragonRaid                 = 'Poison_DragonRaid'
Black_DragonRaid_sBlackDragonRaid                   = 'Black_DragonRaid'

DoAllDailiesSequence = [
    DoAllDailies_sLaunchKingsRaidAndGoToMainScreen,
    DoAllDailies_sClaimMailbox,
    DoAllDailies_sExchangeAmity,
    DoAllDailies_sClearInventory,
    DoAllDailies_sStockade,
    DoAllDailies_sHerosInn,
    DoAllDailies_sUpperDungeon,
    DoAllDailies_sArena,
    DoAllDailies_sWorldBoss,
    DoAllDailies_sClaim_1stEXPNGold,
    DoAllDailies_sAncientRoyalVault,
    DoAllDailies_sConquest,
    DoAllDailies_sClaim_2ndEXPNGoldWStamina,
    DoAllDailies_sDoStory_UptoInventoryManagement,
    DoAllDailies_sClaimDailyMission,
    DoAllDailies_sClaim_3rdEXP_3rdGold,
    DoAllDailies_sDoStory_UptoInventoryManagement,
    DoAllDailies_sClaim_4thEXP_4thdGold,
    DoAllDailies_sDoStory_UptoInventoryManagement,
    DoAllDailies_sDoDragonRaid,
    "",
    "",
    "",
    "",
    "",
    ""
]

Main = {
    Main_sResolutionX                               : 1280,
    Main_sResolutionY                               : 720,
    Main_sGameLaunch_TapToPlayDuration_s            : 50,    # 50s From game launched to Tap to Play
    Main_sGameLaunch_MainGameScreenDuration_s       : 10,    # 10s From Press to Enter to Main game screen
    Main_sNoOfClicksToClearAdvertisement            : 5,
    Main_sTransitionDuration_ms                     : 3000,
    Main_sDurationAfterClick_ms                     : 2000,
    Main_sDurationAfterClick_Short_ms               : 600,
    Main_sDurationAfterClick_Long_ms                : 5000,
    Main_sAnyGameScreenLoadingTime_s                : 15,    # 15s E.g. Arena exit can take a long time
    Main_sReceiveNewHeroDuration_s                  : 12,    # 12 s
    Main_sWaitDuration_s                            : 5,     # 5 s
}

SpecialEvent = {
    SpecialEvent_sNoOfKeys                          : 5,
    SpecialEvent_sSingleBattleDuration_s            : 110,      # secs
    Main_sEasy_Hero1_Position                       : 3,
    Main_sEasy_Hero2_Position                       : 5,
    Main_sEasy_Hero3_Position                       : 8,
    Main_sEasy_Hero4_Position                       : 10
}

WorldBoss = {
    WorldBoss_sNoOfKeys                             : 2,        # number of keys for the day
    WorldBoss_sSingleBattleDuration_s               : 400       # 400 i.e. 6 mins 40 secs
}

Vault = {
    Vault_sHighestClearedFloor                      : 45,
    Vault_sLongestRunTime_s                         : 100,    # 100 secs
    Vault_sNumOfKeysToday                           : 5
}

Arena = {
    Arena_sNoOfMatches                              : 5,
    Arena_sMatchDuration_s                          : 110     # 110s i.e. 1 min 50secs inclusive of "New challenger delay"
}

Stockade = {
    Stockade_sClaimSkillBook                        : 3,        # Claim skill book 1 or 2 or 3 or 4
    Stockade_sSingleBattleDuration_s                : 75,       # 75s
    Stockade_sMaxKeys                               : 5,
    Main_sEasy_Hero1_Position                       : 3,
    Main_sEasy_Hero2_Position                       : 5,
    Main_sEasy_Hero3_Position                       : 8,
    Main_sEasy_Hero4_Position                       : 10
}

TowerOfOrdeals = {
    TowerOfOrdeals_sTotalTimeForAllBattles_s        : 1200,
    Main_sEasy_Hero1_Position                       : 1,
    Main_sEasy_Hero2_Position                       : 3,
    Main_sEasy_Hero3_Position                       : 5,
    Main_sEasy_Hero4_Position                       : 8
}

Story = {
    Story_sAutoRepeatAtChapter                      : 8,        # Auto repeat this chapter
    Story_sUseStaminaPot                            : 'N',
    Story_sLongestRunningTime_s                     : 180,      # 180s i.e. 3 minutes
    Story_sManageInventoryInterval_m                : 60,       # Every 60 minutes do inventory management
    Story_sGrindOrSellInventory                     : 'g',      # g = grind, s = sell
}

Conquest = {
    Conquest_sHighestClearedChapter                 : 8,
    Conquest_sHardContent_StartsFrom                : 8,
    Conquest_sHardContent_NoOfTimesToRetry          : 9,
    Conquest_sLongestRunTime_Chap2_s                : 40,       #secs
    Conquest_sLongestRunTime_Chap3_s                : 50,
    Conquest_sLongestRunTime_Chap4_s                : 40,
    Conquest_sLongestRunTime_Chap5_s                : 60,
    Conquest_sLongestRunTime_Chap6_s                : 50,
    Conquest_sLongestRunTime_Chap7_s                : 75,
    Conquest_sLongestRunTime_Chap8_s                : 150,
    Main_sEasy_Hero1_Position                       : 3,
    Main_sEasy_Hero2_Position                       : 5,
    Main_sEasy_Hero3_Position                       : 8,
    Main_sEasy_Hero4_Position                       : 22,
    Main_sHard_Hero1_Position                       : 1,
    Main_sHard_Hero2_Position                       : 3,
    Main_sHard_Hero3_Position                       : 5,
    Main_sHard_Hero4_Position                       : 8
}

UpperDungeon = {
    UpperDungeon_sHighestClearedChapter             : 8,
    UpperDungeon_sHardContent_StartsFrom            : 8,
    UpperDungeon_sHardContent_NoOfTimesToRetry      : 9,
    UpperDungeon_sLongestRunTime_Chap1_s            : 45,       #secs
    UpperDungeon_sLongestRunTime_Chap2_s            : 50,
    UpperDungeon_sLongestRunTime_Chap3_s            : 50,
    UpperDungeon_sLongestRunTime_Chap4_s            : 50,
    UpperDungeon_sLongestRunTime_Chap5_s            : 50,
    UpperDungeon_sLongestRunTime_Chap6_s            : 55,
    UpperDungeon_sLongestRunTime_Chap7_s            : 85,
    UpperDungeon_sLongestRunTime_Chap8_s            : 175,
    Main_sEasy_Hero1_Position                       : 3,
    Main_sEasy_Hero2_Position                       : 5,
    Main_sEasy_Hero3_Position                       : 8,
    Main_sEasy_Hero4_Position                       : 22,
    Main_sHard_Hero1_Position                       : 1,
    Main_sHard_Hero2_Position                       : 3,
    Main_sHard_Hero3_Position                       : 5,
    Main_sHard_Hero4_Position                       : 8
}


# Dragon Raid hero selection:
# The numbering goes like this
# 1, 2, 3
# 4, 5, 6
# 7, 8 ...
# 10 ...
DragonRaidConfig = {
    DragonRaidConfig_sSelectDragonToAuto            : 'Fire_DragonRaid',    # Fire_DragonRaid, Frost_DragonRaid, Poison_DragonRaid, Black_DragonRaid
    DragonRaidConfig_sHero1_Position                : 1,                    # Please select in ascending order i.e. Hero1_Pos=1, Hero2_Pos=3 and so on
    DragonRaidConfig_sHero2_Position                : 5,                    # Please select in ascending order i.e. Hero1_Pos=1, Hero2_Pos=3 and so on
    DragonRaidConfig_sHero3_Position                : 8,                    # Please select in ascending order i.e. Hero1_Pos=1, Hero2_Pos=3 and so on
    DragonRaidConfig_sHero4_Position                : 9,                    # Please select in ascending order i.e. Hero1_Pos=1, Hero2_Pos=3 and so on
    DragonRaidConfig_sCoopLeaderName                : '',
    DragonRaidConfig_sCoopMemberName1               : '',
    DragonRaidConfig_sCoopMemberName2               : '',
    DragonRaidConfig_sCoopMemberName3               : '',
    DragonRaidConfig_sCoopWaitMemberJoin_s          : 100,                  # 100 secs
    DragonRaidConfig_sCoopHero1_Position            : 1,                    #
    DragonRaidConfig_sCoopHero2_Position            : 5,                    # 
    DragonRaidConfig_sCoopHero3_Position            : 10,                   # 
    DragonRaidConfig_sCoopHero4_Position            : 0,
}

Fire_DragonRaid = {
    DragonRaid_sHighestCleared                      : 91,
    DragonRaid_sAutoAtThisLevel                     : 82,
    DragonRaid_sCoopAutoAtThisLevel                 : 86
}

Frost_DragonRaid = {
    DragonRaid_sHighestCleared                      : 74,
    DragonRaid_sAutoAtThisLevel                     : 74,
    DragonRaid_sCoopAutoAtThisLevel                 : 74
}

Poison_DragonRaid = {
    DragonRaid_sHighestCleared                      : 36,
    DragonRaid_sAutoAtThisLevel                     : 36,
    DragonRaid_sCoopAutoAtThisLevel                 : 36
}

Black_DragonRaid = {
    DragonRaid_sHighestCleared                      : 86,
    DragonRaid_sAutoAtThisLevel                     : 80,
    DragonRaid_sCoopAutoAtThisLevel                 : 80
}

def WriteDefaultSettingsFile () :
    data = {
        DoAllDailies_sDoAllDailies: [],
        Main_sMain: {},
        SpecialEvent_sSpecialEvent: {},
        WorldBoss_sWorldBoss: {},
        Vault_sVault: {},
        Arena_sArena: {},
        Stockade_sStockade: {},
        TowerOfOrdeals_sTowerOfOrdeals: {},
        Story_sStory: {},
        Conquest_sConquest: {},
        UpperDungeon_sUpperDungeon: {},
        DragonRaid_sDragonRaidConfig: {},
        Fire_DragonRaid_sFireDragonRaid: {},
        Frost_DragonRaid_sFrostDragonRaid: {},
        Poison_DragonRaid_sPoisonDragonRaid: {},
        Black_DragonRaid_sBlackDragonRaid: {},
        }

    data_DoAllDailies = data[DoAllDailies_sDoAllDailies]
    for i in DoAllDailiesSequence:
        data_DoAllDailies.append(i)

    data_Main = data[Main_sMain]
    for key in Main:
        data_Main.update({key: Main[key]})

    data_SpecialEvent = data[SpecialEvent_sSpecialEvent]
    for key in SpecialEvent:
        data_SpecialEvent.update({key: SpecialEvent[key]})

    data_WorldBoss = data[WorldBoss_sWorldBoss]
    for key in WorldBoss:
        data_WorldBoss.update({key: WorldBoss[key]})

    data_Vault = data[Vault_sVault]
    for key in Vault:
        data_Vault.update({key: Vault[key]})

    data_Arena = data[Arena_sArena]
    for key in Arena:
        data_Arena.update({key: Arena[key]})

    data_Stockade = data[Stockade_sStockade]
    for key in Stockade:
        data_Stockade.update({key: Stockade[key]})

    data_TowerOfOrdeals = data[TowerOfOrdeals_sTowerOfOrdeals]
    for key in TowerOfOrdeals:
        data_TowerOfOrdeals.update({key: TowerOfOrdeals[key]})

    data_Story = data[Story_sStory]
    for key in Story:
        data_Story.update({key: Story[key]})

    data_Conquest = data[Conquest_sConquest]
    for key in Conquest:
        data_Conquest.update({key: Conquest[key]})

    data_UpperDungeon = data[UpperDungeon_sUpperDungeon]
    for key in UpperDungeon:
        data_UpperDungeon.update({key: UpperDungeon[key]})

    data_DragonRaidConfig = data[DragonRaid_sDragonRaidConfig]
    for key in DragonRaidConfig:
        data_DragonRaidConfig.update({key: DragonRaidConfig[key]})

    data_FireDragonRaid = data[Fire_DragonRaid_sFireDragonRaid]
    for key in Fire_DragonRaid:
        data_FireDragonRaid.update({key: Fire_DragonRaid[key]})
        
    data_FrostDragonRaid = data[Frost_DragonRaid_sFrostDragonRaid]
    for key in Frost_DragonRaid:
        data_FrostDragonRaid.update({key: Frost_DragonRaid[key]})

    data_PoisonDragonRaid = data[Poison_DragonRaid_sPoisonDragonRaid]
    for key in Poison_DragonRaid:
        data_PoisonDragonRaid.update({key: Poison_DragonRaid[key]})

    data_BlackDragonRaid = data[Black_DragonRaid_sBlackDragonRaid]
    for key in Black_DragonRaid:
        data_BlackDragonRaid.update({key: Black_DragonRaid[key]})

    # write to file 
    WriteJsonDataToFile(data, SETTINGS_FILENAME)

def ReadFromFile (i_bPrintToScreen = True) :
    
    curDirpath = os.curdir
    settingsFile = os.path.join(curDirpath, SETTINGS_FILENAME)

    fp = open(settingsFile, 'r')
    json_obj = json.load(fp)
    
    if len(json_obj) == 0:
        error('Cannot find settings.json file.')
    index = 0
    keys = list(json_obj.keys())

    # Loops through all to populate global arrays    
    for key in json_obj :
        if key == DoAllDailies_sDoAllDailies :
            # reset our defaults
            DoAllDailiesSequence.clear()
            nDoAllDailiesSeq_Count = 0
            for value in json_obj[key]:
                DoAllDailiesSequence.append(value)
                nDoAllDailiesSeq_Count += 1
        elif key == Main_sMain :
            for value in json_obj[key] :
                Main[value] = json_obj[Main_sMain][value]
        elif key == SpecialEvent_sSpecialEvent :
            for value in json_obj[key] :
                SpecialEvent[value] = json_obj[SpecialEvent_sSpecialEvent][value]
        elif key == WorldBoss_sWorldBoss :
            for value in json_obj[key] :
                WorldBoss[value] = json_obj[WorldBoss_sWorldBoss][value]
        elif key == Vault_sVault :
            for value in json_obj[key] :
                Vault[value] = json_obj[Vault_sVault][value]
        elif key == Arena_sArena :
            for value in json_obj[key] :
                Arena[value] = json_obj[Arena_sArena][value]
        elif key == Stockade_sStockade :
            for value in json_obj[key] :
                Stockade[value] = json_obj[Stockade_sStockade][value]
        elif key == TowerOfOrdeals_sTowerOfOrdeals :
            for value in json_obj[key] :
                TowerOfOrdeals[value] = json_obj[TowerOfOrdeals_sTowerOfOrdeals][value]
        elif key == Story_sStory:
            for value in json_obj[key] :
                Story[value] = json_obj[Story_sStory][value]
        elif key == Conquest_sConquest :
            for value in json_obj[key] :
                Conquest[value] = json_obj[Conquest_sConquest][value]
        elif key == UpperDungeon_sUpperDungeon :
            for value in json_obj[key] :
                UpperDungeon[value] = json_obj[UpperDungeon_sUpperDungeon][value]
        elif key == DragonRaid_sDragonRaidConfig :
            for value in json_obj[key] :
                DragonRaidConfig[value] = json_obj[DragonRaid_sDragonRaidConfig][value]
        elif key == Fire_DragonRaid_sFireDragonRaid :
            for value in json_obj[key] :
                Fire_DragonRaid[value] = json_obj[Fire_DragonRaid_sFireDragonRaid][value]
        elif key == Frost_DragonRaid_sFrostDragonRaid :
            for value in json_obj[key] :
                Frost_DragonRaid[value] = json_obj[Frost_DragonRaid_sFrostDragonRaid][value]
        elif key == Poison_DragonRaid_sPoisonDragonRaid :
            for value in json_obj[key] :
                Poison_DragonRaid[value] = json_obj[Poison_DragonRaid_sPoisonDragonRaid][value]
        elif key == Black_DragonRaid_sBlackDragonRaid :
            for value in json_obj[key] :
                Black_DragonRaid[value] = json_obj[Black_DragonRaid_sBlackDragonRaid][value]

    # Debugging purpose
    if i_bPrintToScreen:
        PrintToScreen(json_obj)

    fp.close()

def PrintToScreen (i_jsonobject) :
    Manager.TraceHeader1 ()
    Manager.Trace1 ("  Printing settings read from {0}".format(SETTINGS_FILENAME))
    Manager.Trace1 ("  -------------------------------------------------\n")
    for key in i_jsonobject :
        Manager.Trace1 ("{0}".format(key))
        if DoAllDailies_sDoAllDailies == key:
            for i in range(0, len(i_jsonobject[key])):
                Manager.Trace1 ("\t{0} = {1}".format(i, i_jsonobject[key][i]))
        else:
            for value in i_jsonobject[key] :
                Manager.Trace1 ("\t{0} = {1}".format(value, i_jsonobject[key][value]))
    Manager.Trace1 ("*** END Settings.json ***")
    Manager.TraceFooter1 ()

# Unused
def PrintLoadedValuesToScreen () :
    Manager.Trace1 ("\n")
    Manager.Trace1 ("*** Printing settings read from Settings.json ***")
    Manager.Trace1 ("\n")
    for key in Main :
        Manager.Trace1 ("{0}->{1} = {2}".format(Main_sMain, key, Main[key]))
    Manager.Trace1 ("\n")
    for key in Arena :
        Manager.Trace1 ("{0}->{1} = {2}".format(Arena_sArena, key, Arena[key]))
    Manager.Trace1 ("\n")
    Manager.Trace1 ("*** END Settings.json ***")
    Manager.Trace1 ("\n")

# Pretty prints jsondata to file
def WriteJsonDataToFile(data, filename):
    try:
        jsondata = json.dumps(data, indent=2)
        # plus sign = create if not exists
        fd = open(filename, 'w+')
        fd.write(jsondata)
        fd.close()
    except Exception as e:
        Manager.Trace1('ERROR writing {0}    {1}'.format(filename, e))
        pass
