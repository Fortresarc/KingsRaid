import Manager
import Settings
import nox
import KRSelect

# NOTE:     int, string etc are not mutable - cannot be mutated
            # However list is mutable! For now we use list of int with 1 element, to pass by reference
def _MarkCurrentTime_ms(i_lCurrentTime_ms):
    i_lCurrentTime_ms[0] = nox.time

# NOTE:     int, string etc are not mutable - cannot be mutated
            # However list is mutable! For now we use list of int with 1 element, to pass by reference
def _CalculateTimeTaken_ms(i_lMarkedTime_ms):
    tmpList = []
    tmpList.append(nox.time - i_lMarkedTime_ms[0])

    return tmpList

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
    Manager.click_button_msecs(roomSelect, Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
    # Sometimes the icon is greyed out, just click once more
    Manager.click_button_msecs(roomSelect, Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])

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

def _AnalyseTime_DontExecute_ms (i_fFunctionName, *args):
    #name = i_fFunctionName.__name__
    lCurrentTime = [0]   # list is mutable
    lTimeTaken = [0]

    _MarkCurrentTime_ms(lCurrentTime)
    nox.switch_macro_file('test_print_to_nowhere.txt')
    if len(args) == 0:
        i_fFunctionName()
    else:
        Manager.Trace1("ERROR: Not implemented yet")
    lTimeTaken = _CalculateTimeTaken_ms(lCurrentTime)
    nox.restore_macro_file()

    return lTimeTaken[0]

def _GetMemberList():
    lMemberList = []
    if '' != Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopMemberName1]:
        lMemberList.append(Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopMemberName1])
    if '' != Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopMemberName2]:
        lMemberList.append(Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopMemberName2])
    if '' != Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopMemberName3]:
        lMemberList.append(Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopMemberName3])
    return lMemberList

def _Gen_InviteFriend():
    # Create valid member list
    lMemberList = _GetMemberList()

    for sMemberNames in lMemberList:
        # Click SearchID Text box
        Manager.click_button_msecs('raid_select_FriendRequest_SearchID', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])

        # Type out member's name
        nox.userinput(sMemberNames, Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
    
        # Close
        Manager.click_button_msecs('raid_select_FriendRequest_SearchID', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])

        # Find member
        Manager.click_button_msecs('raid_select_FriendRequest_Find', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
        # Invite member
        Manager.click_button_msecs('raid_select_FriendRequest_Invite', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        
        # Just in case, member is offline
        Manager.click_button_msecs('raid_select_FriendRequest_ClickNoWhere', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])

    # Close invite friends dialog box
    Manager.click_button_msecs('raid_select_FriendRequest_Close', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])

def Gen_DoDragonRaid_Leader():
    lMemberList = _GetMemberList()
    lTimeTakenTemp_ms = [0]
    nInvitationToastTime_ms = Manager.ConvertSecsToMsecs(10)
    nTotalTimeLeft_ms = Manager.ConvertSecsToMsecs(Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopWaitMemberJoin_s])
    
    # Enter into Dragon Raid selection screen
    _MarkCurrentTime_ms(lTimeTakenTemp_ms)
    Gen_DoDragonRaid(False)

    bDone = False
    lTimeTakenTemp_ms = _CalculateTimeTaken_ms(lTimeTakenTemp_ms)
    nTotalTimeLeft_ms -= lTimeTakenTemp_ms[0]

    if nTotalTimeLeft_ms < 0:
        Manager.Trace1("WARNING: DoDragonRaid_Leader Failed!!!")
        return
    
    # Invite member and select own heroes
    while nTotalTimeLeft_ms > 0:
        _MarkCurrentTime_ms(lTimeTakenTemp_ms)

        # Find member to connect with
        Manager.click_button_msecs('raid_select_FriendRequest', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        # Close popup in case friend has already joined
        Manager.click_button_msecs('raid_select_CloseAlreadyInvitedPopup', Settings.Main[Settings.Main_sDurationAfterClick_ms])
        
        if 1 < len(lMemberList):
            # Find member to connect with
            Manager.click_button_msecs('raid_select_FriendRequest_2nd', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            # Close popup in case friend has already joined
            Manager.click_button_msecs('raid_select_CloseAlreadyInvitedPopup', Settings.Main[Settings.Main_sDurationAfterClick_ms])

        _Gen_InviteFriend()

        # Select heroes now to save some time
        if False == bDone:
            KRSelect.Gen_DragonRaid_HeroSelect(False)
            Manager.click_button_msecs('raid_select_SetAutoRepeat', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            Manager.click_button_msecs('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick_ms])
            bDone = True

        lTimeTakenTemp_ms = _CalculateTimeTaken_ms(lTimeTakenTemp_ms)
        nTimeTaken_ms = lTimeTakenTemp_ms[0]
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
    lMemberExeTime_ms = [0]
    lTimeTakenTemp_ms = [0]
    nInvitationToastTime_ms = Manager.ConvertSecsToMsecs(10)
    nTotalTimeLeft_ms = Manager.ConvertSecsToMsecs(Settings.DragonRaidConfig[Settings.DragonRaidConfig_sCoopWaitMemberJoin_s])    
     
    # Sync end time with Leader
    _MarkCurrentTime_ms(lMemberExeTime_ms)

    while nTotalTimeLeft_ms > 0:
        _MarkCurrentTime_ms(lTimeTakenTemp_ms)
        Manager.click_button_msecs('raid_select_AcceptInvitation', Settings.Main[Settings.Main_sDurationAfterClick_Long_ms])
        lTimeTakenTemp_ms = _CalculateTimeTaken_ms(lTimeTakenTemp_ms)
        nTimeTaken_ms = lTimeTakenTemp_ms[0]
        nTotalTimeLeft_ms -= nTimeTaken_ms

        # Wait if we still have time left after tasks in current loop
        nWaitTimePerLoop_ms = nInvitationToastTime_ms - nTimeTaken_ms
        if nWaitTimePerLoop_ms > 0:
            Manager.wait_msecs(nWaitTimePerLoop_ms)
    
    KRSelect.Gen_DragonRaid_HeroSelect(False)
    # Click Prepare battle
    Manager.click_button_msecs('raid_select_StartBattle', Settings.Main[Settings.Main_sDurationAfterClick_ms])
    
    # Sync end time with Leader
    nTotalTimeTakenForLeaderToExecute_ms = _AnalyseTime_DontExecute_ms(Gen_DoDragonRaid_Leader)
    lMemberExeTime_ms = _CalculateTimeTaken_ms(lMemberExeTime_ms)
    Manager.wait_msecs(nTotalTimeTakenForLeaderToExecute_ms - lMemberExeTime_ms[0])
    #Manager.click_button_msecs('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Short_ms])
    