import nox
import Settings
import KRCommon

##############
# Macro total run time
##############
TotalRunTime = 0 # millisecs

##############
# NRG, gold
##############
sClaim_1stEXP_1stGold           = 'Claim_1stEXP_1stGold'
sClaim_BonusStamina_BonusGold   = 'Claim_BonusStamina_BonusGold'
sClaim_3rdEXP_3rdGold           = 'Claim_3rdEXP_3rdGold'
sClaim_4thEXP_4thGold           = 'Claim_4thEXP_4thGold'
ClaimEXPGoldStepsList = {
    sClaim_1stEXP_1stGold : 0,
    sClaim_BonusStamina_BonusGold : 1,       # (i.e Claiming "Today's Bonus Stamina" and "Today's Bonus Gold")
    sClaim_3rdEXP_3rdGold : 2,
    sClaim_4thEXP_4thGold : 3
    }

##############
# Macro total run time - functions
##############
def PrintTotalRunTime():
    global TotalRunTime
    nTotalRunTime_Secs = TotalRunTime/1000
    nTotalRunTime_Mins = nTotalRunTime_Secs/60

    if (60 >= nTotalRunTime_Secs):
        print ("Current Total runtime = {0} secs".format(nTotalRunTime_Secs))
    else:
        print ("Current Total runtime = {0} mins".format(nTotalRunTime_Mins))

def AddTotalRunTime (i_nTimeMillisecs):
    global TotalRunTime
    TotalRunTime += i_nTimeMillisecs

# keypress -----------------
def keypress_msecs(i_bButton, i_nWaitMilliseconds, i_bAddTransitionDelay=True):
    nWaitFinal_ms = i_nWaitMilliseconds
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    keypress(i_bButton, nWaitFinal_ms)

def keypress_secs(i_bButton, i_nWaitSeconds, i_bAddTransitionDelay=True):
    nWaitFinal_ms = _SecsToMsecs(i_nWaitSeconds)
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    keypress(i_bButton, nWaitFinal_ms)

def keypress(i_bButton, i_nWaitMilliseconds):
    AddTotalRunTime(i_nWaitMilliseconds)
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
    nWaitFinal_ms = _SecsToMsecs(i_nWaitSeconds)
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    return mouse_drag(fromposition, toposition, nWaitFinal_ms, speed, max_generated_interpolation_points)

def mouse_drag(fromposition, toposition, i_nWaitMilliseconds, speed=0.2, max_generated_interpolation_points=20):
    AddTotalRunTime(i_nWaitMilliseconds)
    nox.mouse_drag(fromposition, toposition, i_nWaitMilliseconds, speed, max_generated_interpolation_points)
# end mouse drags -----------------

# click_loc -----------------
def click_loc_msecs(loc, i_nWaitMilliseconds, i_bAddTransitionDelay = True):
    nWaitFinal_ms = i_nWaitMilliseconds
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    click_loc(loc, nWaitFinal_ms)

def click_loc_secs(loc, i_nWaitSeconds, i_bAddTransitionDelay = True):
    nWaitFinal_ms = _SecsToMsecs(i_nWaitSeconds)
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    click_loc(loc, nWaitFinal_ms)

def click_loc(loc, i_nWaitMilliseconds):
    AddTotalRunTime(i_nWaitMilliseconds)
    nox.click_loc(loc, i_nWaitMilliseconds)
# end click_loc -----------------

# click button -----------------
def click_button_msecs(button, i_nWaitMilliseconds, i_bAddTransitionDelay = True):
    nWaitFinal_ms = i_nWaitMilliseconds
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    return click_button(button, nWaitFinal_ms)

def click_button_secs(button, i_nWaitSeconds, i_bAddTransitionDelay = True):
    nWaitFinal_ms = _SecsToMsecs(i_nWaitSeconds)
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    return click_button(button, nWaitFinal_ms)

def click_button(button, i_nWaitMilliseconds):
    AddTotalRunTime(i_nWaitMilliseconds)
    return nox.click_button(button, i_nWaitMilliseconds)
# end click -----------------

# wait -----------------
def wait_secs(i_nWaitSeconds, i_bAddTransitionDelay = True):
    nWaitFinal_ms = _SecsToMsecs(i_nWaitSeconds)
    if i_bAddTransitionDelay:
        nWaitFinal_ms += Settings.Main[Settings.Main_sTransitionDuration_ms]
    return wait(nWaitFinal_ms)

def wait(i_nWaitMilliseconds):
    AddTotalRunTime(i_nWaitMilliseconds)
    return nox.wait(i_nWaitMilliseconds)
# end wait -----------------

def _SecsToMsecs(i_nSeconds):
    return i_nSeconds * 1000

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
    elif ClaimEXPGoldStepsList[sClaim_BonusStamina_BonusGold] == i_nClaimEventCounter:
        # Claim Today's Bonus Stamina
        click_button_msecs('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Today's Bonus Gold
        click_button_msecs('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Full of Stamina! 1/5
        click_button_msecs('mission_claim_position3', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Stamina Rush! 1/5
        click_button_msecs('mission_claim_position4', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Use EXP hot time (2/3)
        click_button_msecs('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Use Gold hot time (2/3)
        click_button_msecs('mission_claim_position2', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    elif ClaimEXPGoldStepsList[sClaim_3rdEXP_3rdGold] <= i_nClaimEventCounter:
        # Doesn't how much we claim, we just want to expanse it away
        for i in range (0, 3) :
            # Claim Full of Stamina! 2-4/5
            click_button_msecs('mission_claim_position3', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            # Claim Stamina Rush! 2-4/5
            click_button_msecs('mission_claim_position4', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Use EXP hot time (3/3)
        click_button_msecs('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Claim Use Gold hot time (3/3)
        click_button_msecs('mission_claim_position2', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])        
    elif ClaimEXPGoldStepsList[sClaim_4thEXP_4thdGold] <= i_nClaimEventCounter:
        # Doesn't how much we claim, we just want to expanse it away
        for i in range (0, 3) :
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
