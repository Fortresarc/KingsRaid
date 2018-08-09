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
DoAllDailies_sClaim_3rdEXP_3rdGold                  = 'Claim_3rdEXP_3rdGold'
DoAllDailies_sClaimDailyMission                     = 'ClaimDailyMission'
DoAllDailies_sClaim_4thEXP_4thdGold                 = 'Claim_4thEXP_4thdGold'

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
DragonRaidConfig_sHero1_Position                    = 'Hero1_Position'
DragonRaidConfig_sHero2_Position                    = 'Hero2_Position'
DragonRaidConfig_sHero3_Position                    = 'Hero3_Position'
DragonRaidConfig_sHero4_Position                    = 'Hero4_Position'
DragonRaidConfig_sCoopHero1_Position                = 'CoopHero1_Position'
DragonRaidConfig_sCoopHero2_Position                = 'CoopHero2_Position'
DragonRaidConfig_sCoopHero3_Position                = 'CoopHero3_Position'
DragonRaidConfig_sCoopHero4_Position                = 'CoopHero4_Position'


# Dragon Raid
DragonRaid_sDragonRaidConfig                        = 'DragonRaidConfig'
DragonRaidConfig_sSelectDragonToAuto                = 'SelectDragonToAuto'
DragonRaid_sHighestCleared                          = 'HighestCleared'
DragonRaid_sAutoAtThisLevel                         = 'AutoAtThisLevel'
Fire_DragonRaid_sFireDragonRaid                     = 'Fire_DragonRaid'
Frost_DragonRaid_sFrostDragonRaid                   = 'Frost_DragonRaid'
Poison_DragonRaid_sPoisonDragonRaid                 = 'Poison_DragonRaid'
Black_DragonRaid_sBlackDragonRaid                   = 'Black_DragonRaid'

DoAllDailiesSequence = {           
    0 : DoAllDailies_sLaunchKingsRaidAndGoToMainScreen,
    1 : DoAllDailies_sClaimMailbox,
    2 : DoAllDailies_sExchangeAmity,
    3 : DoAllDailies_sClearInventory,
    4 : DoAllDailies_sStockade,
    5 : DoAllDailies_sHerosInn,
    6 : DoAllDailies_sUpperDungeon,
    7 : DoAllDailies_sArena,
    8 : DoAllDailies_sWorldBoss,
    9 : DoAllDailies_sClaim_1stEXPNGold,
    10 : DoAllDailies_sAncientRoyalVault,
    11 : DoAllDailies_sConquest,
    12 : DoAllDailies_sClaim_2ndEXPNGoldWStamina,
    13 : DoAllDailies_sDoStory_UptoInventoryManagement,
    14 : DoAllDailies_sClaimDailyMission,
    15 : DoAllDailies_sClaim_3rdEXP_3rdGold,
    16 : DoAllDailies_sDoStory_UptoInventoryManagement,
    17 : DoAllDailies_sClaim_4thEXP_4thdGold,
    18 : DoAllDailies_sDoStory_UptoInventoryManagement,
    19 : DoAllDailies_sDoDragonRaid,
    20 : "",
    21 : "",
    22 : ""
}

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
    Stockade_sMaxKeys                               : 10,
    Main_sEasy_Hero1_Position                       : 3,
    Main_sEasy_Hero2_Position                       : 5,
    Main_sEasy_Hero3_Position                       : 8,
    Main_sEasy_Hero4_Position                       : 15
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
    Main_sEasy_Hero4_Position                       : 18,
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
    Main_sEasy_Hero4_Position                       : 18,
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
    DragonRaidConfig_sCoopHero1_Position            : 1,                    # 1
    DragonRaidConfig_sCoopHero2_Position            : 5,                    # 10
    DragonRaidConfig_sCoopHero3_Position            : 15,                   # 13
    DragonRaidConfig_sCoopHero4_Position            : 0,
}

Fire_DragonRaid = {
    DragonRaid_sHighestCleared                      : 91,
    DragonRaid_sAutoAtThisLevel                     : 82
}

Frost_DragonRaid = {
    DragonRaid_sHighestCleared                      : 74,
    DragonRaid_sAutoAtThisLevel                     : 74
}

Poison_DragonRaid = {
    DragonRaid_sHighestCleared                      : 36,
    DragonRaid_sAutoAtThisLevel                     : 36
}

Black_DragonRaid = {
    DragonRaid_sHighestCleared                      : 86,
    DragonRaid_sAutoAtThisLevel                     : 80
}

def WriteDefaultSettingsFile () :
    data = {
        DoAllDailies_sDoAllDailies : {            
            0 : DoAllDailiesSequence[0],
            1 : DoAllDailiesSequence[1],
            2 : DoAllDailiesSequence[2],
            3 : DoAllDailiesSequence[3],
            4 : DoAllDailiesSequence[4],
            5 : DoAllDailiesSequence[5],
            6 : DoAllDailiesSequence[6],
            7 : DoAllDailiesSequence[7],
            8 : DoAllDailiesSequence[8],
            9 : DoAllDailiesSequence[9],
            10 : DoAllDailiesSequence[10],
            11 : DoAllDailiesSequence[11],
            12 : DoAllDailiesSequence[12],
            13 : DoAllDailiesSequence[13],
            14 : DoAllDailiesSequence[14],
            15 : DoAllDailiesSequence[15],
            16 : DoAllDailiesSequence[16],
            17 : DoAllDailiesSequence[17],
            18 : DoAllDailiesSequence[18],
            19 : DoAllDailiesSequence[19],
            20 : DoAllDailiesSequence[20],
            21 : DoAllDailiesSequence[21],
            22 : DoAllDailiesSequence[22]
        },
        Main_sMain : {
            Main_sGameLaunch_TapToPlayDuration_s : Main[Main_sGameLaunch_TapToPlayDuration_s],
            Main_sGameLaunch_MainGameScreenDuration_s : Main[Main_sGameLaunch_MainGameScreenDuration_s],
            Main_sNoOfClicksToClearAdvertisement : Main[Main_sNoOfClicksToClearAdvertisement],
            Main_sTransitionDuration_ms : Main[Main_sTransitionDuration_ms],
            Main_sDurationAfterClick_ms : Main[Main_sDurationAfterClick_ms],
            Main_sDurationAfterClick_Short_ms : Main[Main_sDurationAfterClick_Short_ms],
            Main_sDurationAfterClick_Long_ms : Main[Main_sDurationAfterClick_Long_ms],
            Main_sAnyGameScreenLoadingTime_s : Main[Main_sAnyGameScreenLoadingTime_s],
            Main_sReceiveNewHeroDuration_s : Main[Main_sReceiveNewHeroDuration_s]
        },
        WorldBoss_sWorldBoss : {
            WorldBoss_sNoOfKeys : WorldBoss[WorldBoss_sNoOfKeys],
            WorldBoss_sSingleBattleDuration_s : WorldBoss[WorldBoss_sSingleBattleDuration_s]
            },
        Vault_sVault : {
            Vault_sHighestClearedFloor : Vault[Vault_sHighestClearedFloor],
            Vault_sLongestRunTime_s : Vault[Vault_sLongestRunTime_s],
            Vault_sNumOfKeysToday : Vault[Vault_sNumOfKeysToday]
            },
        Arena_sArena : {
            Arena_sNoOfMatches : Arena[Arena_sNoOfMatches],
            Arena_sMatchDuration_s : Arena[Arena_sMatchDuration_s]
            },
        Stockade_sStockade : {
            Stockade_sClaimSkillBook : Stockade[Stockade_sClaimSkillBook],
            Stockade_sSingleBattleDuration_s : Stockade[Stockade_sSingleBattleDuration_s],
            Stockade_sMaxKeys : Stockade[Stockade_sMaxKeys],
            Main_sEasy_Hero1_Position : Stockade[Main_sEasy_Hero1_Position],
            Main_sEasy_Hero2_Position : Stockade[Main_sEasy_Hero2_Position],
            Main_sEasy_Hero3_Position : Stockade[Main_sEasy_Hero3_Position],
            Main_sEasy_Hero4_Position : Stockade[Main_sEasy_Hero4_Position],
            },
        Story_sStory : {
            Story_sAutoRepeatAtChapter : Story[Story_sAutoRepeatAtChapter],
            Story_sUseStaminaPot : Story[Story_sUseStaminaPot],
            Story_sLongestRunningTime_s : Story[Story_sLongestRunningTime_s],
            Story_sManageInventoryInterval_m : Story[Story_sManageInventoryInterval_m],
            Story_sGrindOrSellInventory : Story[Story_sGrindOrSellInventory]
            },
        Conquest_sConquest : {
            Conquest_sHighestClearedChapter : Conquest[Conquest_sHighestClearedChapter],
            Conquest_sHardContent_StartsFrom : Conquest[Conquest_sHardContent_StartsFrom],
            Conquest_sHardContent_NoOfTimesToRetry : Conquest[Conquest_sHardContent_NoOfTimesToRetry],
            Conquest_sLongestRunTime_Chap2_s : Conquest[Conquest_sLongestRunTime_Chap2_s],
            Conquest_sLongestRunTime_Chap3_s : Conquest[Conquest_sLongestRunTime_Chap3_s],
            Conquest_sLongestRunTime_Chap4_s : Conquest[Conquest_sLongestRunTime_Chap4_s],
            Conquest_sLongestRunTime_Chap5_s : Conquest[Conquest_sLongestRunTime_Chap5_s],
            Conquest_sLongestRunTime_Chap6_s : Conquest[Conquest_sLongestRunTime_Chap6_s],
            Conquest_sLongestRunTime_Chap7_s : Conquest[Conquest_sLongestRunTime_Chap7_s],
            Conquest_sLongestRunTime_Chap8_s : Conquest[Conquest_sLongestRunTime_Chap8_s],
            Main_sEasy_Hero1_Position : Conquest[Main_sEasy_Hero1_Position],
            Main_sEasy_Hero2_Position : Conquest[Main_sEasy_Hero2_Position],
            Main_sEasy_Hero3_Position : Conquest[Main_sEasy_Hero3_Position],
            Main_sEasy_Hero4_Position : Conquest[Main_sEasy_Hero4_Position],
            Main_sHard_Hero1_Position : Conquest[Main_sHard_Hero1_Position],
            Main_sHard_Hero2_Position : Conquest[Main_sHard_Hero2_Position],
            Main_sHard_Hero3_Position : Conquest[Main_sHard_Hero3_Position],
            Main_sHard_Hero4_Position : Conquest[Main_sHard_Hero4_Position]
            },
        UpperDungeon_sUpperDungeon : {
            UpperDungeon_sHighestClearedChapter : UpperDungeon[UpperDungeon_sHighestClearedChapter],
            UpperDungeon_sHardContent_StartsFrom : UpperDungeon[UpperDungeon_sHardContent_StartsFrom],
            UpperDungeon_sHardContent_NoOfTimesToRetry : UpperDungeon[UpperDungeon_sHardContent_NoOfTimesToRetry],
            UpperDungeon_sLongestRunTime_Chap1_s : UpperDungeon[UpperDungeon_sLongestRunTime_Chap1_s],
            UpperDungeon_sLongestRunTime_Chap2_s : UpperDungeon[UpperDungeon_sLongestRunTime_Chap2_s],
            UpperDungeon_sLongestRunTime_Chap3_s : UpperDungeon[UpperDungeon_sLongestRunTime_Chap3_s],
            UpperDungeon_sLongestRunTime_Chap4_s : UpperDungeon[UpperDungeon_sLongestRunTime_Chap4_s],
            UpperDungeon_sLongestRunTime_Chap5_s : UpperDungeon[UpperDungeon_sLongestRunTime_Chap5_s],
            UpperDungeon_sLongestRunTime_Chap6_s : UpperDungeon[UpperDungeon_sLongestRunTime_Chap6_s],
            UpperDungeon_sLongestRunTime_Chap7_s : UpperDungeon[UpperDungeon_sLongestRunTime_Chap7_s],
            UpperDungeon_sLongestRunTime_Chap8_s : UpperDungeon[UpperDungeon_sLongestRunTime_Chap8_s],
            Main_sEasy_Hero1_Position : Conquest[Main_sEasy_Hero1_Position],
            Main_sEasy_Hero2_Position : Conquest[Main_sEasy_Hero2_Position],
            Main_sEasy_Hero3_Position : Conquest[Main_sEasy_Hero3_Position],
            Main_sEasy_Hero4_Position : Conquest[Main_sEasy_Hero4_Position],
            Main_sHard_Hero1_Position : Conquest[Main_sHard_Hero1_Position],
            Main_sHard_Hero2_Position : Conquest[Main_sHard_Hero2_Position],
            Main_sHard_Hero3_Position : Conquest[Main_sHard_Hero3_Position],
            Main_sHard_Hero4_Position : Conquest[Main_sHard_Hero4_Position]
            },
        DragonRaid_sDragonRaidConfig: {
            DragonRaidConfig_sSelectDragonToAuto : DragonRaidConfig[DragonRaidConfig_sSelectDragonToAuto],
            DragonRaidConfig_sHero1_Position : DragonRaidConfig[DragonRaidConfig_sHero1_Position],
            DragonRaidConfig_sHero2_Position : DragonRaidConfig[DragonRaidConfig_sHero2_Position],
            DragonRaidConfig_sHero3_Position : DragonRaidConfig[DragonRaidConfig_sHero3_Position],
            DragonRaidConfig_sHero4_Position : DragonRaidConfig[DragonRaidConfig_sHero4_Position],
            DragonRaidConfig_sCoopHero1_Position : DragonRaidConfig[DragonRaidConfig_sCoopHero1_Position],
            DragonRaidConfig_sCoopHero2_Position : DragonRaidConfig[DragonRaidConfig_sCoopHero2_Position],
            DragonRaidConfig_sCoopHero3_Position : DragonRaidConfig[DragonRaidConfig_sCoopHero3_Position],
            DragonRaidConfig_sCoopHero4_Position : DragonRaidConfig[DragonRaidConfig_sCoopHero4_Position]
            },
        Fire_DragonRaid_sFireDragonRaid : {
            DragonRaid_sHighestCleared : Fire_DragonRaid[DragonRaid_sHighestCleared],
            DragonRaid_sAutoAtThisLevel : Fire_DragonRaid[DragonRaid_sAutoAtThisLevel]
            },
        Frost_DragonRaid_sFrostDragonRaid : {
            DragonRaid_sHighestCleared : Frost_DragonRaid[DragonRaid_sHighestCleared],
            DragonRaid_sAutoAtThisLevel : Frost_DragonRaid[DragonRaid_sAutoAtThisLevel]
            },
        Poison_DragonRaid_sPoisonDragonRaid : {
            DragonRaid_sHighestCleared : Poison_DragonRaid[DragonRaid_sHighestCleared],
            DragonRaid_sAutoAtThisLevel : Poison_DragonRaid[DragonRaid_sAutoAtThisLevel]
            },
        Black_DragonRaid_sBlackDragonRaid : {
            DragonRaid_sHighestCleared : Black_DragonRaid[DragonRaid_sHighestCleared],
            DragonRaid_sAutoAtThisLevel : Black_DragonRaid[DragonRaid_sAutoAtThisLevel]
            }
        }
    
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
            nDoAllDailiesSeq_Count = 0
            for value in json_obj[key]:
                DoAllDailiesSequence[nDoAllDailiesSeq_Count] = json_obj[DoAllDailies_sDoAllDailies][value]
                nDoAllDailiesSeq_Count += 1
        elif key == Main_sMain :
            for value in json_obj[key] :
                Main[value] = json_obj[Main_sMain][value]
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
