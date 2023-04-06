import random

import Backend_Information.Random_Encounter as Random_encounter

multiplier = 0
random_number = 0

for i in Random_encounter.encounter_multipliers.values():
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

print(random_number)
print(multiplier)



