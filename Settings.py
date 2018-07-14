import nox
import json
import os

SETTINGS_FILENAME                                   = 'settings.json'

# Settings read from file
# Main
Main_sMain                                          = 'main'
Main_sGameLauch_TapToPlayDuration                   = 'GameLaunch_TapToPlayDuration'
Main_sGameLauch_MainGameScreenDuration              = 'GameLaunch_MainGameScreenDuration'
Main_sNoOfClicksToClearAdvertisement                = 'NoOfClicksToClearAdvertisement'
Main_sTransitionDuration_Alter                      = 'TransitionDuration_Alter'
Main_sDurationAfterClick                            = 'DurationAfterClick'
Main_sDurationAfterClick_Short                      = 'DurationAfterClick_Short'
Main_sAnyGameScreenLoadingTime                      = 'AnyGameScreenLoadingTime'
Main_sReceiveNewHeroDuration                        = 'ReceiveNewHeroDuration'

# Arena
Arena_sArena                                        = 'arena'
Arena_sNoOfMatches                                  = 'NoOfMatches'
Arena_sMatchDuration                                = 'MatchDuration'

# Stockade
Stockade_sStockade                                  = 'stockade'
Stockade_sClaimSkillBook                            = 'ClaimSkillBook'
Stockade_sSingleBattleDuration                      = 'SingleBattleDuration'

Main = {
    # Main
    Main_sGameLauch_TapToPlayDuration               : 50000,    # From game launched to Tap to Play
    Main_sGameLauch_MainGameScreenDuration          : 10000,    # From Press to Enter to Main game screen
    Main_sNoOfClicksToClearAdvertisement            : 5,
    Main_sTransitionDuration_Alter                  : 2000,
    Main_sDurationAfterClick                        : 2000,
    Main_sDurationAfterClick_Short                  : 600,
    Main_sAnyGameScreenLoadingTime                  : 15000,    # E.g. Arena exit can take a long time
    Main_sReceiveNewHeroDuration                    : 12000     # 12 s
}

Arena = {
    # Arena
    Arena_sNoOfMatches                              : 5,
    Arena_sMatchDuration                            : 95000     #1min 25secs inclusive of "New challenger delay"
}

Stockade = {
    # Stockade
    Stockade_sClaimSkillBook                        : 4,        # Claim skill book 1 or 2 or 3 or 4
    Stockade_sSingleBattleDuration                  : 80000
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
