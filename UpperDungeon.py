import nox
import KRCommon
import DoAllDailies
import Settings

def gen_upper_dungeon():
    chapterList = {
        1 : 'ch1_upper_dungeon',
        2 : 'ch2_upper_dungeon',
        3 : 'ch3_upper_dungeon',
        4 : 'ch4_upper_dungeon',
        5 : 'ch5_upper_dungeon',
        6 : 'ch6_upper_dungeon',
        7 : 'ch7_upper_dungeon',
        8 : 'ch8_upper_dungeon'
        }
    longestRunTimeList = {
        'ch1_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap1_s],
        'ch2_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap2_s],
        'ch3_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap3_s],
        'ch4_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap4_s],
        'ch5_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap5_s],
        'ch6_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap6_s],
        'ch7_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap7_s],
        'ch8_upper_dungeon' : Settings.UpperDungeon[Settings.UpperDungeon_sLongestRunTime_Chap8_s]
        }

    print('All Upper Dungeons should have set levels.  To do this manually, you can start and then stop a battle on the chosen level per dungeon.  This is also a good way to alter which levels/fragments you want to focus on.')

    nSelectEasyContentHeroesAt = 1  # Select heroes for easy content
    KRCommon.Gen_Conquest_UpperDungeon_Helper(  'upper_dungeon',    # button name.. Portal > UpperDungeon
                                                chapterList,
                                                longestRunTimeList,
                                                Settings.UpperDungeon[Settings.UpperDungeon_sHighestClearedChapter],
                                                Settings.UpperDungeon[Settings.UpperDungeon_sHardContent_NoOfTimesToRetry],
                                                nSelectEasyContentHeroesAt,
                                                Settings.UpperDungeon[Settings.UpperDungeon_sHardContent_StartsFrom], # Select heroes for hard content (Chapter 8)
                                                1)
