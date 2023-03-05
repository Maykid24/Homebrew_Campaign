"""
Random Encounter program
- Will determine what kind of encounter the group faces if an encounter happens
- Will provide monsters that will be dealt with in correlation to which country the group is in
- Also will provide page numbers for the monsters for ease of use
"""

import random
import Homebrew_Campaign.Backend_Information.Monsters as mn

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
    1: {'number_of_monsters': '1', 'multiplier': '1'},
    2: {'number_of_monsters': '2', 'multiplier': '1.5'},
    3: {'number_of_monsters': '3-6', 'multiplier': '2'},
    4: {'number_of_monsters': '7-10', 'multiplier': '2.5'},
    5: {'number_of_monsters': '11-14', 'multiplier': '3'},
    6: {'number_of_monsters': '15', 'multiplier': '4'}
}

# n_of_monsters = encounter_multipliers[5]['number_of_monsters'].split('-')
# print(n_of_monsters[0])
# print(n_of_monsters[1])

number_of_character = 5
character_level = 3

difficulty = ['easy', 'medium', 'hard', 'deadly']

easy_mode = xp_thresholds[character_level]['Easy']
medium_mode = xp_thresholds[character_level]['Medium']
hard_mode = xp_thresholds[character_level]['Hard']
deadly_mode = xp_thresholds[character_level]['Deadly']

level_easy = number_of_character * easy_mode
level_medium = number_of_character * medium_mode
level_hard = number_of_character * hard_mode
level_deadly = number_of_character * deadly_mode

print(level_easy, "|", level_medium, "|", level_hard, "|", level_deadly)
print(', '.join(environments))
difficulty_choice = random.choice(difficulty)
print(difficulty_choice)
print(random.choice(encounter_multipliers))
print()


def diff_choice():
    if difficulty_choice == 'easy':
        print(level_easy)

    elif difficulty_choice == 'medium':
        print(level_medium)
    elif difficulty_choice == 'hard':
        print(level_hard)
    elif difficulty_choice == 'deadly':
        print(level_deadly)


diff_choice()

