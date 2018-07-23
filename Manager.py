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
sClaim_4thEXP_4thGold          = 'Claim_4thEXP_4thdGold'
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

def keypress(i_bButton, i_nWaitMilliseconds):
    AddTotalRunTime(i_nWaitMilliseconds)
    nox.keypress(i_bButton, i_nWaitMilliseconds)

def mouse_drag(fromposition, toposition, i_nWaitMilliseconds, speed=0.2, max_generated_interpolation_points=20):
    AddTotalRunTime(i_nWaitMilliseconds)
    nox.mouse_drag(fromposition, toposition, i_nWaitMilliseconds, speed, max_generated_interpolation_points)

def click_loc(loc, i_nWaitMilliseconds):
    AddTotalRunTime(i_nWaitMilliseconds)
    nox.click_loc(loc, i_nWaitMilliseconds)

def click_button(button, i_nWaitMilliseconds):
    AddTotalRunTime(i_nWaitMilliseconds)
    return nox.click_button(button, i_nWaitMilliseconds)

def wait(i_nWaitMilliseconds):
    AddTotalRunTime(i_nWaitMilliseconds)
    return nox.wait(i_nWaitMilliseconds)

# Assumes NOTHING is claimed yet when game just restarted a new day
def Gen_ClaimEnergyGoldHotTime(i_nClaimEventCounter) :

    nox.click_button('main_mission', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    nox.click_button('mission_tab_eventmission', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    if ClaimEXPGoldStepsList[sClaim_1stEXP_1stGold] == i_nClaimEventCounter:
        # Claim Use EXP hot time (1/3)
        nox.click_button('mission_claim_position3', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Claim Use Gold hot time (1/3)
        nox.click_button('mission_claim_position4', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    elif ClaimEXPGoldStepsList[sClaim_BonusStamina_BonusGold] == i_nClaimEventCounter:
        # Claim Today's Bonus Stamina
        nox.click_button('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Claim Today's Bonus Gold
        nox.click_button('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Claim Full of Stamina! 1/5
        nox.click_button('mission_claim_position3', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Claim Stamina Rush! 1/5
        nox.click_button('mission_claim_position4', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Claim Use EXP hot time (2/3)
        nox.click_button('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Claim Use Gold hot time (2/3)
        nox.click_button('mission_claim_position2', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    elif ClaimEXPGoldStepsList[sClaim_3rdEXP_3rdGold] <= i_nClaimEventCounter:
        # Doesn't how much we claim, we just want to expanse it away
        for i in range (0, 3) :
            # Claim Full of Stamina! 2-4/5
            nox.click_button('mission_claim_position3', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
            nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
            # Claim Stamina Rush! 2-4/5
            nox.click_button('mission_claim_position4', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
            nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Claim Use EXP hot time (3/3)
        nox.click_button('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # Claim Use Gold hot time (3/3)
        nox.click_button('mission_claim_position2', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])        
    elif ClaimEXPGoldStepsList[sClaim_4thEXP_4thdGold] <= i_nClaimEventCounter:
        # Doesn't how much we claim, we just want to expanse it away
        for i in range (0, 3) :
            # Claim Full of Stamina! ?/5
            nox.click_button('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
            nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
            # Claim Stamina Rush! ?/5
            nox.click_button('mission_claim_position2', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
            nox.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    # increment counter
    i_nClaimEventCounter += 1
    # Back to main
    KRCommon.Back()
