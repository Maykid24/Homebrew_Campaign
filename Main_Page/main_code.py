"""
Utilizing this page as a main page for python code
"""

import Homebrew_Campaign.Backend_Information.Monsters as Monsters
import Homebrew_Campaign.Backend_Information.Treasure.hoard_treasure as hoard_treasure
import Homebrew_Campaign.Backend_Information.Treasure.individual_treasure as individual_treasure
import Homebrew_Campaign.Main_Page.main_page_list as m_list

# for key, value in Monsters.artic.items():
#     print(key, value)


print(*m_list.main_list, sep='|'.center(14))
user_input = input("What would you like to do? ")
if user_input.lower() == "treasure":
    treasure_input = input("Individual or Hoard? ")
    if treasure_input.lower() == "hoard":
        print(*m_list.difficulty_level, sep='|'.center(14))
        level_difficulty = input("What level difficulty? ")
        if level_difficulty.lower() == "0-4":
            hoard_treasure.hoard_challenge04()
        elif level_difficulty.lower() == "5-10":
            hoard_treasure.hoard_challenge510()
        elif level_difficulty.lower() == "11-16":
            hoard_treasure.hoard_challenge1116()
        elif level_difficulty.lower() == "17+":
            hoard_treasure.hoard_challenge17()
    elif treasure_input.lower() == "individual":
        print(*m_list.difficulty_level, sep='|'.center(14))
        level_difficulty = input("What level difficulty? ")
        if level_difficulty.lower() == "0-4":
            individual_treasure.individual_challenge04()
        elif level_difficulty.lower() == "5-10":
            individual_treasure.individual_challenge510()
        elif level_difficulty.lower() == "11-16":
            individual_treasure.individual_challenge1116()
        elif level_difficulty.lower() == "17+":
            individual_treasure.individual_challenge17()



