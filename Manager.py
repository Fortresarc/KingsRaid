import os
import datetime
from datetime import timedelta
import nox
import Settings
import KRCommon

##############
# Log file
##############
LogFileName = 'settings_log.txt'
LogFile = None

##############
# NRG, gold
##############
sClaim_1stEXP_1stGold           = 'Claim_1stEXP_1stGold'
sClaim_2ndEXPNGoldWStamina      = 'Claim_2ndEXPNGoldWStamina'
sClaim_3rdEXP_3rdGold           = 'Claim_3rdEXP_3rdGold'
sClaim_4thEXP_4thGold           = 'Claim_4thEXP_4thGold'
ClaimEXPGoldStepsList = {
    sClaim_1stEXP_1stGold : 0,
    sClaim_2ndEXPNGoldWStamina : 1,       # (i.e Claiming "Today's Bonus Stamina" and "Today's Bonus Gold")
    sClaim_3rdEXP_3rdGold : 2,
    sClaim_4thEXP_4thGold : 3
    }

##############
# All functions
##############
def OpenLogFile():
    global LogFile
    
    if os.path.isfile(LogFileName):
        os.remove(LogFileName)

    # plus sign - create a file if it doesn't exist
    LogFile = open(LogFileName, "a+")

def Close():
    global LogFile
    LogFile.close()

# no indentation
def TraceHeader1 ():
    Trace1 ("\n")
    Trace1 ("###################################################")

def TraceSubHeader1 ():
    Trace1 ("/## ******************************************* ##/")

def TraceFooter1():
    Trace1 ("## _____________________________________________ ##")

# no indentation
def Trace1 (i_sLogText):
    global LogFile
    print (i_sLogText)
    LogFile.write(i_sLogText + '\n')
    
# no indentation
def TraceHeader2 ():
    Trace2 ("================================================")

def TraceFooter2():
    Trace2 ("== ------------------------------------------ ==")

# indented 1 tab space
def Trace2 (i_sLogText):
    global LogFile
    sFormattedLogText = "\t" + i_sLogText
    print (sFormattedLogText)
    LogFile.write(sFormattedLogText + '\n')

def GetString_TimeLapsed (i_nFromTime_ms = 0):
    TotalRunTime = nox.time
    fTotalRunTime_Secs = ConvertMsecsToSecs(TotalRunTime - i_nFromTime_ms)
    nTotalRunTime_Mins = int(fTotalRunTime_Secs/60)
    nReturnString = ""

    if (60.0 >= fTotalRunTime_Secs):
        nReturnString = "%02d secs" % int(fTotalRunTime_Secs)
    else:
        nReturnString = "%02d mins" % (nTotalRunTime_Mins)
        
    return nReturnString

# Time format helper
def ConvertTime_HMSFormat (i_nTimeMsecs = 1000):
    nTotalTime_Secs = i_nTimeMsecs/1000
    nTotalTime_Mins = nTotalTime_Secs/60
    
    nConvert_HMS_Hours = int( nTotalTime_Mins/60 )
    nConvert_HMS_Mins  = int( (nTotalTime_Mins%60) )
    nConvert_HMS_Secs  = int( (nTotalTime_Secs%60) )

    return nConvert_HMS_Hours, nConvert_HMS_Mins, nConvert_HMS_Secs

def GetString_SecsFormat(i_nTimeMsecs = 1000):
    return "%02d secs" % int(i_nTimeMsecs/1000)

def GetString_MinsFormat(i_nTimeMsecs = 1000):
    return "%02d mins" % int((i_nTimeMsecs/1000) / 60)

def GetString_HMSFormat(i_nTimeMsecs = 1000):
    nHours, nMins, nSecs = ConvertTime_HMSFormat(i_nTimeMsecs)
    return "%02d:%02d:%02d" % (nHours,
                               nMins,
                               nSecs)

def GetString_AddToTime_HMSFormat(i_DateTime):
    nHours, nMins, nSecs = ConvertTime_HMSFormat(nox.time)
    timeLapsed = timedelta(hours=nHours, minutes=nMins, seconds=nSecs)
    finalTime = i_DateTime + timeLapsed

    return "%02d:%02d:%02d" % (finalTime.hour,
                            finalTime.minute,
                            finalTime.second)

def GetString_TotalRunTime_HMSFormat():
    TotalRunTime = nox.time
    return "{0} ({1})".format( GetString_MinsFormat(TotalRunTime),
                               GetString_HMSFormat(TotalRunTime) )

# keypress -----------------
def keypress_msecs(i_bButton, i_nWaitMilliseconds, i_bAddTransitionDelay=True):
    nWaitFinal_ms = i_nWaitMilliseconds
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    keypress(i_bButton, nWaitFinal_ms)

def keypress_secs(i_bButton, i_nWaitSeconds, i_bAddTransitionDelay=True):
    nWaitFinal_ms = ConvertSecsToMsecs(i_nWaitSeconds)
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    keypress(i_bButton, nWaitFinal_ms)

def keypress(i_bButton, i_nWaitMilliseconds):
    nox.keypress(i_bButton, i_nWaitMilliseconds)
# end keypress -----------------
    
# mouse drags -----------------
def mouse_drag_msecs(fromposition,
                     toposition,
                     i_nWaitMilliseconds,
                     speed=0.2,
                     max_generated_interpolation_points=20,
                     i_bAddTransitionDelay=True):
    nWaitFinal_ms = i_nWaitMilliseconds
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    return mouse_drag(fromposition, toposition, nWaitFinal_ms, speed, max_generated_interpolation_points)

def mouse_drag_secs(fromposition,
                    toposition,
                    i_nWaitSeconds,
                    speed=0.2,
                    max_generated_interpolation_points=20,
                    i_bAddTransitionDelay=True):
    nWaitFinal_ms = ConvertSecsToMsecs(i_nWaitSeconds)
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    return mouse_drag(fromposition, toposition, nWaitFinal_ms, speed, max_generated_interpolation_points)

def mouse_drag(fromposition, toposition, i_nWaitMilliseconds, speed=0.2, max_generated_interpolation_points=20):
    nox.mouse_drag(fromposition, toposition, i_nWaitMilliseconds, speed, max_generated_interpolation_points)
# end mouse drags -----------------

# click_loc -----------------
def click_loc_msecs(loc, i_nWaitMilliseconds, i_bAddTransitionDelay = True):
    nWaitFinal_ms = i_nWaitMilliseconds
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    click_loc(loc, nWaitFinal_ms)

def click_loc_secs(loc, i_nWaitSeconds, i_bAddTransitionDelay = True):
    nWaitFinal_ms = ConvertSecsToMsecs(i_nWaitSeconds)
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    click_loc(loc, nWaitFinal_ms)

def click_loc(loc, i_nWaitMilliseconds):
    nox.click_loc(loc, i_nWaitMilliseconds)
# end click_loc -----------------

# click button -----------------
def click_button_msecs(button, i_nWaitMilliseconds, i_bAddTransitionDelay = True, i_nNegativeYOffset = 0):
    nWaitFinal_ms = i_nWaitMilliseconds
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    return click_button(button, nWaitFinal_ms, i_nNegativeYOffset)

def click_button_secs(button, i_nWaitSeconds, i_bAddTransitionDelay = True):
    nWaitFinal_ms = ConvertSecsToMsecs(i_nWaitSeconds)
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    return click_button(button, nWaitFinal_ms)

def click_button(button, i_nWaitMilliseconds, i_nNegativeYOffset = 0):
    return nox.click_button(button, i_nWaitMilliseconds, i_nNegativeYOffset)
# end click -----------------

# wait -----------------
def wait_secs(i_nWaitSeconds, i_bAddTransitionDelay = True):
    nWaitFinal_ms = ConvertSecsToMsecs(i_nWaitSeconds)
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    return wait_msecs(nWaitFinal_ms)

def wait_msecs(i_nWaitMilliseconds):
    return nox.wait(i_nWaitMilliseconds)
# end wait -----------------

def ConvertSecsToMsecs(i_nSeconds):
    return int(i_nSeconds * 1000)

def ConvertMsecsToSecs(i_nMillisecs):
    return int(i_nMillisecs / 1000)

# Assumes NOTHING is claimed yet when game just restarted a new day
def Gen_ClaimEnergyGoldHotTime(i_nClaimEventCounter) :

    click_button_msecs('main_mission', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
    click_button_msecs('mission_tab_eventmission', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
    if ClaimEXPGoldStepsList[sClaim_1stEXP_1stGold] == i_nClaimEventCounter:
        # Claim Use EXP hot time (1/3)
        click_button_msecs('mission_claim_position3', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Use Gold hot time (1/3)
        click_button_msecs('mission_claim_position4', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    elif ClaimEXPGoldStepsList[sClaim_2ndEXPNGoldWStamina] == i_nClaimEventCounter:
        # Claim Today's Bonus Stamina (Exp)
        click_button_msecs('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Today's Bonus Gold (Gold)
        click_button_msecs('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        
        # NOTE: We are commenting this away because, there are too much Energy to expense for 1 hour
        #       Lets do those in Claim_3rdEXP_3rdGold
        ## Claim Full of Stamina! 1/5 (Gold)
        #click_button_msecs('mission_claim_position3', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        #click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        ## Claim Stamina Rush! 1/5 (Exp)
        #click_button_msecs('mission_claim_position4', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        #click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        
        # Claim Use EXP hot time (2/3)
        click_button_msecs('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Use Gold hot time (2/3)
        click_button_msecs('mission_claim_position2', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    elif ClaimEXPGoldStepsList[sClaim_3rdEXP_3rdGold] <= i_nClaimEventCounter:
        # Claim 1st stamina = 100, 2nd = 200, 3rd = 300
        for i in range (0, 2) :
            # Claim Full of Stamina! 1 - 3/5
            click_button_msecs('mission_claim_position3', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            # Claim Stamina Rush! 1 - 3/5
            click_button_msecs('mission_claim_position4', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Use EXP hot time (3/3)
        click_button_msecs('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Use Gold hot time (3/3)
        click_button_msecs('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])        
    elif ClaimEXPGoldStepsList[sClaim_4thEXP_4thdGold] <= i_nClaimEventCounter:
        # Doesn't how much we claim, we just want to expanse it away
        for i in range (0, 1) :
            # Claim Full of Stamina! ?/5
            click_button_msecs('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            # Claim Stamina Rush! ?/5
            click_button_msecs('mission_claim_position2', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
    # increment counter
    i_nClaimEventCounter += 1
    # Back to main
    KRCommon.Back()
