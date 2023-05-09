"""
Utilizing this page as a main page for python code
"""

import random

import main_page.backend_information.monsters as Mn
import main_page.backend_information.treasure.hoard_treasure as hoard_treasure
import main_page.backend_information.treasure.individual_treasure as individual_treasure
import main_page.backend_information.random_encounter as Random_Encounter
import main_page.main_page_list as m_list



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
elif user_input.lower() == "monsters":
    Random_Encounter.random_monsters()
elif user_input.lower() == "encounter":
    Random_Encounter.random_encounter_chart()
