"""
Random Encounter program
- Will determine what kind of encounter the group faces if an encounter happens
- Will provide monsters that will be dealt with in correlation to which country the group is in
- Also will provide page numbers for the monsters for ease of use
"""

import random
import main_page.backend_information.random_encounter as Random_Encounter
import main_page.backend_information.monsters as Mn


environments = ['artic', 'coastal', 'desert', 'forest', 'grassland', 'hill', 'mountain', 'swamp', 'underdark',
                'underwater', 'urban']

xp_thresholds = {
    1: {'Easy': 25, 'Medium': 50, 'Hard': 75, 'Deadly': 100},
    2: {'Easy': 50, 'Medium': 100, 'Hard': 150, 'Deadly': 200},
    3: {'Easy': 75, 'Medium': 150, 'Hard': 225, 'Deadly': 400},
    4: {'Easy': 125, 'Medium': 250, 'Hard': 375, 'Deadly': 500},
    5: {'Easy': 250, 'Medium': 500, 'Hard': 750, 'Deadly': 1100},
    6: {'Easy': 300, 'Medium': 600, 'Hard': 900, 'Deadly': 1400},
    7: {'Easy': 350, 'Medium': 750, 'Hard': 1100, 'Deadly': 1700},
    8: {'Easy': 450, 'Medium': 900, 'Hard': 1400, 'Deadly': 2100},
    9: {'Easy': 550, 'Medium': 1100, 'Hard': 1600, 'Deadly': 2400},
    10: {'Easy': 600, 'Medium': 1200, 'Hard': 1900, 'Deadly': 2800},
    11: {'Easy': 800, 'Medium': 1600, 'Hard': 2400, 'Deadly': 3600},
    12: {'Easy': 1000, 'Medium': 2000, 'Hard': 3000, 'Deadly': 4500},
    13: {'Easy': 1100, 'Medium': 2200, 'Hard': 3400, 'Deadly': 5100},
    14: {'Easy': 1250, 'Medium': 2500, 'Hard': 3800, 'Deadly': 5700},
    15: {'Easy': 1400, 'Medium': 2800, 'Hard': 4300, 'Deadly': 6400},
    16: {'Easy': 1600, 'Medium': 3200, 'Hard': 4800, 'Deadly': 7200},
    17: {'Easy': 2000, 'Medium': 3900, 'Hard': 5900, 'Deadly': 8800},
    18: {'Easy': 2100, 'Medium': 4200, 'Hard': 6300, 'Deadly': 9500},
    19: {'Easy': 2400, 'Medium': 4900, 'Hard': 7300, 'Deadly': 10900},
    20: {'Easy': 2800, 'Medium': 5700, 'Hard': 8500, 'Deadly': 12700},
}

encounter_multipliers = {
    1: {'number_of_monsters': '1', 'multiplier': 1},
    2: {'number_of_monsters': '2', 'multiplier': 1.5},
    3: {'number_of_monsters': '3-6', 'multiplier': 2},
    4: {'number_of_monsters': '7-10', 'multiplier': 2.5},
    5: {'number_of_monsters': '11-14', 'multiplier': 3},
    6: {'number_of_monsters': '15', 'multiplier': 4}
}

number_of_character = 5
character_level = 4

difficulty = ['easy', 'medium', 'hard', 'deadly']

easy_mode = xp_thresholds[character_level]['Easy']
medium_mode = xp_thresholds[character_level]['Medium']
hard_mode = xp_thresholds[character_level]['Hard']
deadly_mode = xp_thresholds[character_level]['Deadly']

level_easy = number_of_character * easy_mode
level_medium = number_of_character * medium_mode
level_hard = number_of_character * hard_mode
level_deadly = number_of_character * deadly_mode


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



def random_encounter_chart():
    roll = random.randint(1, 20)
    if roll >= 18:
        second_roll = random.randint(1, 20)
        if second_roll >= 11:
            d4_roll = random.randint(1, 4)
            if d4_roll == 1:
                print("Monster Encounter")
                random_monsters()
            elif d4_roll == 2:
                print("Evil Person Encounter")
            elif d4_roll == 3:
                print("Traps")
            elif d4_roll == 4:
                print("Ambush")
                random_monsters()
        if second_roll < 11:
            d4_roll = random.randint(1, 4)
            if d4_roll == 1:
                print("Carriages Passing By")
            elif d4_roll == 2:
                print("Random Trade Wagon")
            elif d4_roll == 3:
                print("Friendly Creatures")
            elif d4_roll == 4:
                print("Group of travelers")
    else:
        print("No encounter")


def random_monsters():
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

