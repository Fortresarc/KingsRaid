import nox
import json
import os

SETTINGS_FILENAME                                   = 'settings.json'

# Settings read from file
# Main
Main_sMain                                          = 'Main'
Main_sGameLauch_TapToPlayDuration                   = 'GameLaunch_TapToPlayDuration'
Main_sGameLauch_MainGameScreenDuration              = 'GameLaunch_MainGameScreenDuration'
Main_sNoOfClicksToClearAdvertisement                = 'NoOfClicksToClearAdvertisement'
Main_sTransitionDuration_Alter                      = 'TransitionDuration_Alter'
Main_sDurationAfterClick                            = 'DurationAfterClick'
Main_sDurationAfterClick_Short                      = 'DurationAfterClick_Short'
Main_sDurationAfterClick_Long                       = 'DurationAfterClick_Long'
Main_sAnyGameScreenLoadingTime                      = 'AnyGameScreenLoadingTime'
Main_sReceiveNewHeroDuration                        = 'ReceiveNewHeroDuration'
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

# Conquests
Conquest_sConquest                                  = 'Conquest'

# Upper Dungeons
UpperDungeon_sUpperDungeon                            = 'UpperDungeon'
UpperDungeon_sHighestClearedChapter                   = 'HighestClearedChapter'
UpperDungeon_sHardContentRetryTimes                   = 'HardContentRetryTimes'
UpperDungeon_sLongestRunTime_Chap1                    = 'LongestRunTime_Chap1'
UpperDungeon_sLongestRunTime_Chap2                    = 'LongestRunTime_Chap2'
UpperDungeon_sLongestRunTime_Chap3                    = 'LongestRunTime_Chap3'
UpperDungeon_sLongestRunTime_Chap4                    = 'LongestRunTime_Chap4'
UpperDungeon_sLongestRunTime_Chap5                    = 'LongestRunTime_Chap5'
UpperDungeon_sLongestRunTime_Chap6                    = 'LongestRunTime_Chap6'
UpperDungeon_sLongestRunTime_Chap7                    = 'LongestRunTime_Chap7'
UpperDungeon_sLongestRunTime_Chap8                    = 'LongestRunTime_Chap8'

# Dragon Raid configuration for all
DragonRaidConfig_sHero1_Position                    = 'Hero1_Position'
DragonRaidConfig_sHero2_Position                    = 'Hero2_Position'
DragonRaidConfig_sHero3_Position                    = 'Hero3_Position'
DragonRaidConfig_sHero4_Position                    = 'Hero4_Position'

# Arena
Arena_sArena                                        = 'Arena'
Arena_sNoOfMatches                                  = 'NoOfMatches'
Arena_sMatchDuration                                = 'MatchDuration'

# Stockade
Stockade_sStockade                                  = 'Stockade'
Stockade_sClaimSkillBook                            = 'ClaimSkillBook'
Stockade_sSingleBattleDuration                      = 'SingleBattleDuration'

# Dragon Raid
DragonRaid_sDragonRaidConfig                        = 'DragonRaidConfig'
DragonRaidConfig_sSelectDragonToAuto                = 'SelectDragonToAuto'
DragonRaid_sHighestCleared                          = 'HighestCleared'
DragonRaid_sAutoAtThisLevel                         = 'AutoAtThisLevel'
Fire_DragonRaid_sFireDragonRaid                     = 'Fire_DragonRaid'
Frost_DragonRaid_sFrostDragonRaid                   = 'Frost_DragonRaid'
Poison_DragonRaid_sPoisonDragonRaid                 = 'Poison_DragonRaid'
Black_DragonRaid_sBlackDragonRaid                   = 'Black_DragonRaid'

Main = {
    Main_sGameLauch_TapToPlayDuration               : 50000,    # From game launched to Tap to Play
    Main_sGameLauch_MainGameScreenDuration          : 10000,    # From Press to Enter to Main game screen
    Main_sNoOfClicksToClearAdvertisement            : 5,
    Main_sTransitionDuration_Alter                  : 2000,
    Main_sDurationAfterClick                        : 2000,
    Main_sDurationAfterClick_Short                  : 600,
    Main_sDurationAfterClick_Long                   : 5000,
    Main_sAnyGameScreenLoadingTime                  : 15000,    # E.g. Arena exit can take a long time
    Main_sReceiveNewHeroDuration                    : 12000,    # 12 s
}

Arena = {
    Arena_sNoOfMatches                              : 5,
    Arena_sMatchDuration                            : 95000     #1min 25secs inclusive of "New challenger delay"
}

Stockade = {
    Stockade_sClaimSkillBook                        : 4,        # Claim skill book 1 or 2 or 3 or 4
    Stockade_sSingleBattleDuration                  : 80000
}

Conquest = {
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
    UpperDungeon_sHardContentRetryTimes             : 9,
    UpperDungeon_sLongestRunTime_Chap1              : 50,
    UpperDungeon_sLongestRunTime_Chap2              : 50,
    UpperDungeon_sLongestRunTime_Chap3              : 50,
    UpperDungeon_sLongestRunTime_Chap4              : 50,
    UpperDungeon_sLongestRunTime_Chap5              : 55,
    UpperDungeon_sLongestRunTime_Chap6              : 55,
    UpperDungeon_sLongestRunTime_Chap7              : 95,
    UpperDungeon_sLongestRunTime_Chap8              : 190,
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
    DragonRaidConfig_sHero2_Position                : 3,                    # Please select in ascending order i.e. Hero1_Pos=1, Hero2_Pos=3 and so on
    DragonRaidConfig_sHero3_Position                : 5,                    # Please select in ascending order i.e. Hero1_Pos=1, Hero2_Pos=3 and so on
    DragonRaidConfig_sHero4_Position                : 8                     # Please select in ascending order i.e. Hero1_Pos=1, Hero2_Pos=3 and so on
}

Fire_DragonRaid = {
    DragonRaid_sHighestCleared                      : 86,
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
        Main_sMain : {
            Main_sGameLauch_TapToPlayDuration : Main[Main_sGameLauch_TapToPlayDuration],
            Main_sGameLauch_MainGameScreenDuration : Main[Main_sGameLauch_MainGameScreenDuration],
            Main_sNoOfClicksToClearAdvertisement : Main[Main_sNoOfClicksToClearAdvertisement],
            Main_sTransitionDuration_Alter : Main[Main_sTransitionDuration_Alter],
            Main_sDurationAfterClick : Main[Main_sDurationAfterClick],
            Main_sDurationAfterClick_Short : Main[Main_sDurationAfterClick_Short],
            Main_sDurationAfterClick_Long : Main[Main_sDurationAfterClick_Long],
            Main_sAnyGameScreenLoadingTime : Main[Main_sAnyGameScreenLoadingTime],
            Main_sReceiveNewHeroDuration : Main[Main_sReceiveNewHeroDuration]
            },
        Arena_sArena : {
            Arena_sNoOfMatches : Arena[Arena_sNoOfMatches],
            Arena_sMatchDuration : Arena[Arena_sMatchDuration]
            },
        Stockade_sStockade : {
            Stockade_sClaimSkillBook : Stockade[Stockade_sClaimSkillBook],
            Stockade_sSingleBattleDuration : Stockade[Stockade_sSingleBattleDuration]
            },
        Conquest_sConquest : {
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
            UpperDungeon_sHardContentRetryTimes : UpperDungeon[UpperDungeon_sHardContentRetryTimes],
            UpperDungeon_sLongestRunTime_Chap1 : UpperDungeon[UpperDungeon_sLongestRunTime_Chap1],
            UpperDungeon_sLongestRunTime_Chap2 : UpperDungeon[UpperDungeon_sLongestRunTime_Chap2],
            UpperDungeon_sLongestRunTime_Chap3 : UpperDungeon[UpperDungeon_sLongestRunTime_Chap3],
            UpperDungeon_sLongestRunTime_Chap4 : UpperDungeon[UpperDungeon_sLongestRunTime_Chap4],
            UpperDungeon_sLongestRunTime_Chap5 : UpperDungeon[UpperDungeon_sLongestRunTime_Chap5],
            UpperDungeon_sLongestRunTime_Chap6 : UpperDungeon[UpperDungeon_sLongestRunTime_Chap6],
            UpperDungeon_sLongestRunTime_Chap7 : UpperDungeon[UpperDungeon_sLongestRunTime_Chap7],
            UpperDungeon_sLongestRunTime_Chap8 : UpperDungeon[UpperDungeon_sLongestRunTime_Chap8],
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
            DragonRaidConfig_sHero4_Position : DragonRaidConfig[DragonRaidConfig_sHero4_Position]
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

def ReadFromFile () :
    
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
        if key == Main_sMain :
            for value in json_obj[key] :
                Main[value] = json_obj[Main_sMain][value]
        if key == Arena_sArena :
            for value in json_obj[key] :
                Arena[value] = json_obj[Arena_sArena][value]
        if key == Stockade_sStockade :
            for value in json_obj[key] :
                Stockade[value] = json_obj[Stockade_sStockade][value]
        if key == Conquest_sConquest :
            for value in json_obj[key] :
                Conquest[value] = json_obj[Conquest_sConquest][value]
        if key == UpperDungeon_sUpperDungeon :
            for value in json_obj[key] :
                UpperDungeon[value] = json_obj[UpperDungeon_sUpperDungeon][value]
        if key == DragonRaid_sDragonRaidConfig :
            for value in json_obj[key] :
                DragonRaidConfig[value] = json_obj[DragonRaid_sDragonRaidConfig][value]
        if key == Fire_DragonRaid_sFireDragonRaid :
            for value in json_obj[key] :
                Fire_DragonRaid[value] = json_obj[Fire_DragonRaid_sFireDragonRaid][value]
        if key == Frost_DragonRaid_sFrostDragonRaid :
            for value in json_obj[key] :
                Frost_DragonRaid[value] = json_obj[Frost_DragonRaid_sFrostDragonRaid][value]
        if key == Poison_DragonRaid_sPoisonDragonRaid :
            for value in json_obj[key] :
                Poison_DragonRaid[value] = json_obj[Poison_DragonRaid_sPoisonDragonRaid][value]
        if key == Black_DragonRaid_sBlackDragonRaid :
            for value in json_obj[key] :
                Black_DragonRaid[value] = json_obj[Black_DragonRaid_sBlackDragonRaid][value]

    # Debugging purpose
    PrintToScreen(json_obj)

    fp.close()

def PrintToScreen (i_jsonobject) :
    print ("\n")
    print ("*** Printing settings read from Settings.json ***")
    for key in i_jsonobject :
        print ("{0}".format(key))
        for value in i_jsonobject[key] :
            print ("\t{0} = {1}".format(value, i_jsonobject[key][value]))
    print ("*** END Settings.json ***")
    print ("\n")

# Unused
def PrintLoadedValuesToScreen () :
    print ("\n")
    print ("*** Printing settings read from Settings.json ***")
    print ("\n")
    for key in Main :
        print ("{0}->{1} = {2}".format(Main_sMain, key, Main[key]))
    print ("\n")
    for key in Arena :
        print ("{0}->{1} = {2}".format(Arena_sArena, key, Arena[key]))
    print ("\n")
    print ("*** END Settings.json ***")
    print ("\n")

# Pretty prints jsondata to file
def WriteJsonDataToFile(data, filename):
    try:
        jsondata = json.dumps(data, indent=2)
        fd = open(filename, 'w')
        fd.write(jsondata)
        fd.close()
    except:
        print('ERROR writing {0}'.format(filename))
        pass
