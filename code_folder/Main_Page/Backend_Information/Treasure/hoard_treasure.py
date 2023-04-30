"""This page is used for horde treasures specifically and overall group payout"""

import random

from Main_Page.Backend_Information.Treasure.random_dice_roll import RollRandomMoney
from Main_Page.Backend_Information.Treasure.random_dice_roll import random_gem_roll
from Main_Page.Backend_Information.Treasure.Random_Magic_Items import magic_item_table_a, magic_item_table_b, \
    magic_item_table_c, magic_item_table_d, magic_item_table_e, magic_item_table_f, magic_item_table_g, \
    magic_item_table_h, magic_item_table_i


d4 = random.randint(1, 4)
d6 = random.randint(1, 6)
d8 = random.randint(1, 8)
gp_1 = "Gem Price: 10 gp"
gp_2 = "Gem Price: 25 gp"
gp_3 = "Gem Price: 50 gp"
gp_4 = "Gem Price: 100 gp"
gp_5 = "Gem Price: 250 gp"
gp_6 = "Gem Price: 500 gp"
gp_7 = "Gem Price: 750 gp"
gp_8 = "Gem Price: 1000 gp"
gp_9 = "Gem Price: 2500 gp"
gp_10 = "Gem Price: 5000 gp"
gp_11 = "Gem Price: 7500 gp"


def hoard_challenge04():
    dice_random = random.randint(1, 100)
    results = RollRandomMoney(copper='6d6', copper_multiplier=100, silver='3d6', silver_multiplier=100,
                              gold='2d6', gold_multiplier=10, platinum='', platinum_multiplier=None)
    results.money_roll()
    if 1 <= dice_random <= 6:
        print("Gems: Nothing")
        print("Magic Items: Nothing")
    elif 7 <= dice_random <= 16:
        random_gem_roll("2d6")
        print(f"{gp_1}")
        print("Magic Items: Nothing")
    elif 17 <= dice_random <= 26:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("Magic Items: Nothing")
    elif 27 <= dice_random <= 36:
        random_gem_roll("2d6")
        print(f"{gp_3}")
        print("Magic Items: Nothing")
    elif 37 <= dice_random <= 44:
        random_gem_roll("2d6")
        print(f"{gp_1}")
        print("Magic Items:")
        for i in range(d6):
            magic_item_table_a()
    elif 45 <= dice_random <= 52:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("Magic Items:")
        for i in range(d6):
            magic_item_table_a()
    elif 53 <= dice_random <= 60:
        random_gem_roll("2d6")
        print(f"{gp_3}")
        print("Magic Items:")
        for i in range(d6):
            magic_item_table_a()
    elif 61 <= dice_random <= 65:
        random_gem_roll("2d6")
        print(f"{gp_1}")
        print("Magic Items:")
        for i in range(d4):
            magic_item_table_b()
    elif 66 <= dice_random <= 70:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("Magic Items:")
        for i in range(d4):
            magic_item_table_b()
    elif 71 <= dice_random <= 75:
        random_gem_roll("2d6")
        print(f"{gp_3}")
        print("Magic Items:")
        for i in range(d4):
            magic_item_table_b()
    elif 76 <= dice_random <= 78:
        random_gem_roll("2d6")
        print(f"{gp_1}")
        print("Magic Items:")
        for i in range(d4):
            magic_item_table_c()
    elif 79 <= dice_random <= 80:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("Magic Items:")
        for i in range(d4):
            magic_item_table_c()
    elif 81 <= dice_random <= 85:
        random_gem_roll("2d6")
        print(f"{gp_3}")
        print("Magic Items:")
        for i in range(d4):
            magic_item_table_c()
    elif 86 <= dice_random <= 92:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("Magic Items:")
        for i in range(d4):
            magic_item_table_f()
    elif 93 <= dice_random <= 97:
        random_gem_roll("2d6")
        print(f"{gp_3}")
        print("Magic Items:")
        for i in range(d4):
            magic_item_table_f()
    elif 98 <= dice_random <= 99:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("Magic Items")
        magic_item_table_g()
    elif dice_random == 100:
        random_gem_roll("2d6")
        print(f"{gp_3}")
        print("Magic Items")
        magic_item_table_g()


def hoard_challenge510():
    dice_random = random.randint(1, 100)
    results = RollRandomMoney(copper='2d6', copper_multiplier=100, silver='2d6', silver_multiplier=1000,
                              gold='6d6', gold_multiplier=100, platinum='3d6', platinum_multiplier=10)
    results.money_roll()
    if 1 <= dice_random <= 4:
        print("\nNothing")
    elif 5 <= dice_random <= 10:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("\nMagic Items: Nothing")
    elif 11 <= dice_random <= 16:
        random_gem_roll("3d6")
        print(f"{gp_3}")
        print("\nMagic Items: Nothing")
    elif 17 <= dice_random <= 22:
        random_gem_roll("3d6")
        print(f"{gp_4}")
        print("\nMagic Items: Nothing")
    elif 23 <= dice_random <= 28:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items: Nothing")
    elif 29 <= dice_random <= 32:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_a()
    elif 33 <= dice_random <= 36:
        random_gem_roll("3d6")
        print(f"{gp_3}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_a()
    elif 37 <= dice_random <= 40:
        random_gem_roll("3d6")
        print(f"{gp_5}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_a()
    elif 41 <= dice_random <= 44:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_a()
    elif 45 <= dice_random <= 49:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_b()
    elif 50 <= dice_random <= 54:
        random_gem_roll("3d6")
        print(f"{gp_3}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_b()
    elif 55 <= dice_random <= 59:
        random_gem_roll("3d6")
        print(f"{gp_4}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_b()
    elif 60 <= dice_random <= 63:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_b()
    elif 64 <= dice_random <= 66:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_c()
    elif 67 <= dice_random <= 69:
        random_gem_roll("3d6")
        print(f"{gp_3}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_c()
    elif 70 <= dice_random <= 72:
        random_gem_roll("3d6")
        print(f"{gp_4}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_c()
    elif 73 <= dice_random <= 74:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_c()
    elif 75 <= dice_random <= 76:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("\nMagic Items:")
        magic_item_table_d()
    elif 77 <= dice_random <= 78:
        random_gem_roll("3d6")
        print(f"{gp_3}")
        print("\nMagic Items:")
        magic_item_table_d()
    elif dice_random == 79:
        random_gem_roll("3d6")
        print(f"{gp_4}")
        print("\nMagic Items:")
        magic_item_table_d()
    elif dice_random == 80:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        magic_item_table_d()
    elif 81 <= dice_random <= 84:
        random_gem_roll("2d4")
        print(f"{gp_2}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_f()
    elif 85 <= dice_random <= 88:
        random_gem_roll("3d6")
        print(f"{gp_3}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_f()
    elif 89 <= dice_random <= 91:
        random_gem_roll("3d6")
        print(f"{gp_4}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_f()
    elif 92 <= dice_random <= 94:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_f()
    elif 95 <= dice_random <= 96:
        random_gem_roll("3d6")
        print(f"{gp_4}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_g()
    elif 97 <= dice_random <= 98:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_g()
    elif dice_random == 99:
        random_gem_roll("3d6")
        print(f"{gp_4}")
        print("\nMagic Items:")
        magic_item_table_h()
    elif dice_random == 100:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        magic_item_table_h()


def hoard_challenge1116():
    dice_random = random.randint(1, 100)
    results = RollRandomMoney(copper='', copper_multiplier=None, silver='', silver_multiplier=None,
                              gold='4d6', gold_multiplier=1000, platinum='5d6', platinum_multiplier=100)
    results.money_roll()
    if 1 <= dice_random <= 3:
        print("Nothing")
    elif 4 <= dice_random <= 6:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items: Nothing")
    elif 7 <= dice_random <= 9:
        random_gem_roll("2d4")
        print(f"{gp_7}")
        print("\nMagic Items: Nothing")
    elif 10 <= dice_random <= 12:
        random_gem_roll("3d6")
        print(f"{gp_6}")
        print("\nMagic Items: Nothing")
    elif 13 <= dice_random <= 15:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items: Nothing")
    elif 16 <= dice_random <= 19:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_a()
        for i in range(d6):
            magic_item_table_b()
    elif 20 <= dice_random <= 23:
        random_gem_roll("2d4")
        print(f"{gp_7}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_a()
        for i in range(d6):
            magic_item_table_b()
    elif 24 <= dice_random <= 26:
        random_gem_roll("3d6")
        print(f"{gp_6}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_a()
        for i in range(d6):
            magic_item_table_b()
    elif 27 <= dice_random <= 29:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_a()
        for i in range(d6):
            magic_item_table_b()
    elif 30 <= dice_random <= 35:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_c()
    elif 36 <= dice_random <= 40:
        random_gem_roll("2d4")
        print(f"{gp_7}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_c()
    elif 41 <= dice_random <= 45:
        random_gem_roll("3d6")
        print(f"{gp_6}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_c()
    elif 46 <= dice_random <= 50:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_c()
    elif 51 <= dice_random <= 54:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_d()
    elif 55 <= dice_random <= 58:
        random_gem_roll("2d4")
        print(f"{gp_7}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_d()
    elif 59 <= dice_random <= 62:
        random_gem_roll("3d6")
        print(f"{gp_6}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_d()
    elif 63 <= dice_random <= 66:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_d()
    elif 67 <= dice_random <= 68:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        magic_item_table_e()
    elif 69 <= dice_random <= 70:
        random_gem_roll("2d4")
        print(f"{gp_7}")
        print("\nMagic Items:")
        magic_item_table_e()
    elif 71 <= dice_random <= 72:
        random_gem_roll("3d6")
        print(f"{gp_6}")
        print("\nMagic Items:")
        magic_item_table_e()
    elif 73 <= dice_random <= 74:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        magic_item_table_e()
    elif 75 <= dice_random <= 76:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        magic_item_table_f()
        for i in range(d4):
            magic_item_table_g()
    elif 77 <= dice_random <= 78:
        random_gem_roll("2d4")
        print(f"{gp_7}")
        print("\nMagic Items:")
        magic_item_table_f()
        for i in range(d4):
            magic_item_table_g()
    elif 79 <= dice_random <= 80:
        random_gem_roll("3d6")
        print(f"{gp_6}")
        print("\nMagic Items:")
        magic_item_table_f()
        for i in range(d4):
            magic_item_table_g()
    elif 81 <= dice_random <= 82:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        magic_item_table_f()
        for i in range(d4):
            magic_item_table_g()
    elif 83 <= dice_random <= 85:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_h()
    elif 86 <= dice_random <= 88:
        random_gem_roll("2d4")
        print(f"{gp_7}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_h()
    elif 89 <= dice_random <= 90:
        random_gem_roll("3d6")
        print(f"{gp_6}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_h()
    elif 91 <= dice_random <= 92:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_h()
    elif 93 <= dice_random <= 94:
        random_gem_roll("2d4")
        print(f"{gp_5}")
        print("\nMagic Items:")
        magic_item_table_i()
    elif 95 <= dice_random <= 96:
        random_gem_roll("2d4")
        print(f"{gp_7}")
        print("\nMagic Items:")
        magic_item_table_i()
    elif 97 <= dice_random <= 98:
        random_gem_roll("3d6")
        print(f"{gp_6}")
        print("\nMagic Items:")
        magic_item_table_i()
    elif 99 <= dice_random <= 100:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        magic_item_table_i()


def hoard_challenge17():
    dice_random = random.randint(1, 100)
    results = RollRandomMoney(copper='', copper_multiplier=None, silver='', silver_multiplier=None,
                              gold='12d6', gold_multiplier=1000, platinum='8d6', platinum_multiplier=1000)
    results.money_roll()
    if 1 <= dice_random <= 2:
        print("Nothing")
    elif 3 <= dice_random <= 5:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items: ")
        for i in range(d8):
            magic_item_table_c()
    elif 6 <= dice_random <= 8:
        random_gem_roll("1d10")
        print(f"{gp_9}")
        print("\nMagic Items: ")
        for i in range(d8):
            magic_item_table_c()
    elif 9 <= dice_random <= 11:
        random_gem_roll("1d4")
        print(f"{gp_11}")
        print("\nMagic Items: ")
        for i in range(d8):
            magic_item_table_c()
    elif 12 <= dice_random <= 14:
        random_gem_roll("1d8")
        print(f"{gp_10}")
        print("\nMagic Items: ")
        for i in range(d8):
            magic_item_table_c()
    elif 15 <= dice_random <= 22:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_d()
    elif 23 <= dice_random <= 30:
        random_gem_roll("1d10")
        print(f"{gp_9}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_d()
    elif 31 <= dice_random <= 38:
        random_gem_roll("1d4")
        print(f"{gp_11}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_d()
    elif 39 <= dice_random <= 46:
        random_gem_roll("1d8")
        print(f"{gp_10}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_d()
    elif 47 <= dice_random <= 52:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_e()
    elif 53 <= dice_random <= 58:
        random_gem_roll("1d10")
        print(f"{gp_9}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_e()
    elif 59 <= dice_random <= 63:
        random_gem_roll("1d4")
        print(f"{gp_11}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_e()
    elif 64 <= dice_random <= 68:
        random_gem_roll("1d8")
        print(f"{gp_10}")
        print("\nMagic Items:")
        for i in range(d6):
            magic_item_table_e()
    elif dice_random == 69:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_g()
    elif dice_random == 70:
        random_gem_roll("1d10")
        print(f"{gp_9}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_g()
    elif dice_random == 71:
        random_gem_roll("1d4")
        print(f"{gp_11}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_g()
    elif dice_random == 72:
        random_gem_roll("1d8")
        print(f"{gp_10}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_g()
    elif 73 <= dice_random <= 74:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_h()
    elif 75 <= dice_random <= 76:
        random_gem_roll("1d10")
        print(f"{gp_9}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_h()
    elif 77 <= dice_random <= 78:
        random_gem_roll("1d4")
        print(f"{gp_11}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_h()
    elif 79 <= dice_random <= 80:
        random_gem_roll("1d8")
        print(f"{gp_10}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_h()
    elif 81 <= dice_random <= 85:
        random_gem_roll("3d6")
        print(f"{gp_8}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_h()
    elif 86 <= dice_random <= 90:
        random_gem_roll("1d10")
        print(f"{gp_9}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_i()
    elif 91 <= dice_random <= 95:
        random_gem_roll("1d4")
        print(f"{gp_11}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_i()
    elif 96 <= dice_random <= 100:
        random_gem_roll("1d8")
        print(f"{gp_10}")
        print("\nMagic Items:")
        for i in range(d4):
            magic_item_table_i()

