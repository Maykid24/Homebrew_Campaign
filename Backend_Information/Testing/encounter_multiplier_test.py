import random

import Backend_Information.Random_Encounter as Random_encounter
import Backend_Information.Monsters as Mn

# multiplier = 0
# random_number = 0
#
# for i in Random_encounter.encounter_multipliers.values():
#     random_number = random.randint(1, 15)
#     if random_number == 1:
#         multiplier = 1
#     elif random_number == 2:
#         multiplier = 1.5
#     elif 3 <= random_number <= 6:
#         multiplier = 2
#     elif 7 <= random_number <= 10:
#         multiplier = 2.5
#     elif 11 <= random_number <= 14:
#         multiplier = 3
#     elif random_number == 15:
#         multiplier = 4
#
# print(random_number)
# print(multiplier)


environment_encounter = 'artic'
difficulty_encounter = random.choice(Random_encounter.difficulty)


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


for i in Mn.monsters_category.keys():
    if i == environment_encounter.lower():
        for y in Mn.monsters_category[i].values():
            cr_xp = y.get('CR').split('XP')[0]
            cr = int(cr_xp)
            if difficulty_encounter == 'easy':
                if Random_encounter.level_easy >= cr:
                    print(y.get('Name'))
                    print(cr)
            elif difficulty_encounter == 'medium':
                if Random_encounter.level_medium >= cr:
                    print(y.get('Name'))
                    print(cr)
            elif difficulty_encounter == 'hard':
                if Random_encounter.level_hard >= cr:
                    print(y.get('Name'))
                    print(cr)
            elif difficulty_encounter == 'deadly':
                if Random_encounter.level_deadly >= cr:
                    print(y.get('Name'))
                    print(cr)
