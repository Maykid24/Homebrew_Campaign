"""
Utilizing this page as a main page for python code
"""

import random

# import Main_Page.Backend_Information.Monsters as Mn
# import Main_Page.Backend_Information.Treasure.hoard_treasure as hoard_treasure
# import Main_Page.Backend_Information.Treasure.individual_treasure as individual_treasure
# import Main_Page.Backend_Information.Random_Encounter as Random_Encounter
# import Main_Page.main_page_list as m_list

from Main_Page.Backend_Information import Monsters as Mn
from Main_Page.Backend_Information.Treasure import hoard_treasure as hoard_treasure
from Main_Page.Backend_Information.Treasure import individual_treasure as individual_treasure
from Main_Page.Backend_Information import Random_Encounter as Random_Encounter
from Main_Page import main_page_list as m_list


def number_of_monsters():
    multiplier = 0
    random_number = random.randint(1, 15)
    if random_number == 1:
        multiplier = 1
    elif random_number == 2:
        multiplier = 1.5
    elif 3 <= random_number <= 6:
        multiplier = 2
    elif 7 <= random_number <= 10:
        multiplier = 2.5
    elif 11 <= random_number <= 14:
        multiplier = 3
    elif random_number == 15:
        multiplier = 4
    print("# of Monsters:", random_number)
    print("Multiplier: ", multiplier)


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
    print(*Random_Encounter.environments, sep='|'.center(5))
    environment_encounter = input("What environment is the encounter in? ")
    print(Random_Encounter.level_easy, "|", Random_Encounter.level_medium, "|", Random_Encounter.level_hard, "|",
          Random_Encounter.level_deadly)
    difficulty_encounter = random.choice(Random_Encounter.difficulty)
    print(difficulty_encounter)
    number_of_monsters()
    for i in Mn.monsters_category.keys():
        if i == environment_encounter.lower():
            for y in Mn.monsters_category[i].values():
                cr_xp = y.get('CR').split('XP')[0]
                cr = int(cr_xp)
                if difficulty_encounter == 'easy':
                    if Random_Encounter.level_easy >= cr:
                        print(y.get('Name'))
                        print(cr)
                elif difficulty_encounter == 'medium':
                    if Random_Encounter.level_medium >= cr:
                        print(y.get('Name'))
                        print(cr)
                elif difficulty_encounter == 'hard':
                    if Random_Encounter.level_hard >= cr:
                        print(y.get('Name'))
                        print(cr)
                elif difficulty_encounter == 'deadly':
                    if Random_Encounter.level_deadly >= cr:
                        print(y.get('Name'))
                        print(cr)
