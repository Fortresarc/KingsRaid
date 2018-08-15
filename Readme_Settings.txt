How to run DoAllDailies with settings.json

- Select option 1) Generate Default data to selected settings file (You can create as many as you like for different nox accounts)
- Now settings.json will be created, modify the settings to suit your content
- Run krng.py again, and select option 8) Do all dailies
- Done ! (NOTE: A settings_log file will be created for debugging purpose, you can ignore this)


These are all the available actions you can sequence into this data field 'DoAllDailiesSequence'
(e.g. "20": "",        // This means at Step 20, there is no action)

'LaunchKingsRaidAndGoToMainScreen'            // Put King's Raid icon exactly in the middle
'ClaimMailbox'                                // Claims all mails
'ExchangeAmity'                               // Exchange amity and do roulette 
'ClearInventory'                              // "GrindOrSellInventory": "g" means grind
'Stockade'                                    // 
'HerosInn'                                    //
'UpperDungeon'                                // Do all upper dungeons up till the highest cleared level, we can select 2 teams for easy/ hard contents
'Arena'                                       //
'WorldBoss'                                   //    
'Claim_1stEXPNGold'                           //
'AncientRoyalVault'                           // 
'Conquest'                                    // Do all conquests up till the highest cleared level, we can select 2 teams for easy/ hard contents
'Claim_2ndEXPNGoldWStamina'                   //
'DoStory_UptoInventoryManagement'             //
'DoDragonRaid'                                //    
'DoDragonRaid_Leader'                         // Not important to fill in
'DoDragonRaid_Member'                         // Fill in :
                                              // - MemberName'X' with your Coop member names correctly. (NOTE: Up to 3 members). CoopWaitMemberJoin_secs
                                              // - CoopWaitMemberJoin_secs = time for invite members, select heroes, and wait for member to join time
                                              //   (NOTE: CoopWaitMemberJoin_secs must be the same across all Leader and Members settings.json. This ensures
                                              //          Leader and Member(s) scripts will all end at the same time)
'Claim_3rdEXP_3rdGold'                        //
'ClaimDailyMission'                           //
'Claim_4thEXP_4thdGold'                       //
'KillKingsRaid'                               // Kill king's raid app in Nox
'Wait_Xsecs'                                  // Do nothing and wait for 'X' secs (e.g. Wait_60secs will wait for 60 secs and move on to next action)
'DoTowerOfOrdeals'                            // Do Tower of Ordeals