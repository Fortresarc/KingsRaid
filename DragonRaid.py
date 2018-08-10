import Manager
import Settings
import nox
import KRSelect

nMarkCurrentTime_ms = 0

def _MarkCurrentTime_ms():
    global nMarkCurrentTime_ms
    nMarkCurrentTime_ms = Manager.TotalRunTime

def _CalculateTimeTaken_ms():
    global nMarkCurrentTime_ms
    return (Manager.TotalRunTime - nMarkCurrentTime_ms)

def Gen_DoDragonRaid (i_bIsNotCoop = True) :
    whichDragonRaid = Settings.DragonRaidConfig[Settings.DragonRaidConfig_sSelectDragonToAuto]

    Manager.click_button_msecs('raid_multi', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('raid_select', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])

    # room settings
    # select correct dragon
    roomSelect = 'raid_select_black'
    if Settings.Fire_DragonRaid_sFireDragonRaid == whichDragonRaid :
        roomSelect = 'raid_select_fire'
        DragonSettings = Settings.Fire_DragonRaid.copy()
    elif Settings.Frost_DragonRaid_sFrostDragonRaid == whichDragonRaid :
        roomSelect = 'raid_select_frost'
        DragonSettings = Settings.Frost_DragonRaid.copy()
    elif Settings.Poison_DragonRaid_sPoisonDragonRaid== whichDragonRaid :
        roomSelect = 'raid_select_poison'
        DragonSettings = Settings.Poison_DragonRaid.copy()
    elif Settings.Black_DragonRaid_sBlackDragonRaid == whichDragonRaid :
        DragonSettings = Settings.Black_DragonRaid.copy()
        Manager.mouse_drag_msecs('raid_select_list_bottom', 'raid_select_list_top', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    # Click to select the correct dragon room
    Manager.click_button_msecs(roomSelect, Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # calculate how many levels to decrement
    if i_bIsNotCoop:
        nAutoAtThisLevel = DragonSettings[Settings.DragonRaid_sAutoAtThisLevel]
    else:
        nAutoAtThisLevel = DragonSettings[Settings.DragonRaid_sCoopAutoAtThisLevel]
    differenceFromHighestClearedToAutoLevel = abs(DragonSettings[Settings.DragonRaid_sHighestCleared] - nAutoAtThisLevel)
    for i in range (0, differenceFromHighestClearedToAutoLevel) :
        Manager.click_button_msecs('raid_select_decrementlevel', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms], False)
    # uncheck gather raiders
    Manager.click_button_msecs('raid_select_gatherraiders', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms], False)
    Manager.click_button_msecs('raid_select_enter', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    # Only select solo heroes when we are NOT in coop mode
    if i_bIsNotCoop:
        KRSelect.Gen_DragonRaid_HeroSelect()

    if i_bIsNotCoop :
        Manager.click_button_msecs('raid_select_SetAutoRepeat', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        Manager.click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        Manager.click_button_msecs('raid_select_StartBattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        Manager.click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        #TODO refill nrg or not?

def Gen_DoDragonRaid_Leader():
    nInvitationToastTime_ms = Manager.ConvertSecsToMsecs(10)
    nTotalTimeLeft_ms = Manager.ConvertSecsToMsecs(Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopWaitMemberJoin_s])
    
    # Enter into Dragon Raid selection screen
    _MarkCurrentTime_ms()
    Gen_DoDragonRaid(False)

    bDone = False
    nTotalTimeLeft_ms -= _CalculateTimeTaken_ms()
    if nTotalTimeLeft_ms < 0:
        Manager.Trace1("WARNING: DoDragonRaid_Leader Failed!!!")
        return
    
    # Invite member and select own heroes
    while nTotalTimeLeft_ms > 0:
        _MarkCurrentTime_ms()
        _Gen_InviteFriend()

        # Select heroes now to save some time
        if False == bDone:
            KRSelect.Gen_DragonRaid_HeroSelect(False)
            Manager.click_button_msecs('raid_select_SetAutoRepeat', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            Manager.click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            bDone = True

        nTimeTaken_ms = _CalculateTimeTaken_ms()
        nTotalTimeLeft_ms -= nTimeTaken_ms
        
        # Wait if we still have time left after tasks in current loop
        nWaitTimePerLoop_ms = nInvitationToastTime_ms - nTimeTaken_ms
        if nWaitTimePerLoop_ms > 0:
            Manager.wait_msecs(nWaitTimePerLoop_ms)

    # At this point of time friend would have joined and be selecting his hero
    # Reset total time left so we can wait for member to be ready
    Manager.wait_secs(Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopWaitMemberJoin_s])

    # Start battle
    Manager.click_button_msecs('raid_select_StartBattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    Manager.click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])

def Gen_DoDragonRaid_Member():
    nInvitationToastTime_ms = Manager.ConvertSecsToMsecs(10)
    nTotalTimeLeft_ms = Manager.ConvertSecsToMsecs(Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopWaitMemberJoin_s])

    while nTotalTimeLeft_ms > 0:
        _MarkCurrentTime_ms()
        Manager.click_button_msecs('raid_select_AcceptInvitation', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        nTimeTaken_ms = _CalculateTimeTaken_ms()
        nTotalTimeLeft_ms -= nTimeTaken_ms

        # Wait if we still have time left after tasks in current loop
        nWaitTimePerLoop_ms = nInvitationToastTime_ms - nTimeTaken_ms
        if nWaitTimePerLoop_ms > 0:
            Manager.wait_msecs(nWaitTimePerLoop_ms)
    
    KRSelect.Gen_DragonRaid_HeroSelect(False)
    # Click Prepare battle
    Manager.click_button_msecs('raid_select_StartBattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
def _Gen_InviteFriend():    
    # Find member to connect with
    Manager.click_button_msecs('raid_select_FriendRequest', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # Close popup in case friend has already joined
    Manager.click_button_msecs('raid_select_CloseAlreadyInvitedPopup', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    # Click SearchID Text box
    Manager.click_button_msecs('raid_select_FriendRequest_SearchID', Settings.Main[Settings.Main_sDurationAfterClick_ms])

    # Type out friend's name
    nox.userinput(Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopMemberName], Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
    
    # Close
    Manager.click_button_msecs('raid_select_FriendRequest_SearchID', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])

    # Find friend
    Manager.click_button_msecs('raid_select_FriendRequest_Find', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
    # Invite friend
    Manager.click_button_msecs('raid_select_FriendRequest_Invite', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])

    # Close invite friends dialog box
    Manager.click_button_msecs('raid_select_FriendRequest_Close', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])