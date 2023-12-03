"""This sheet is to do the d100 rolls for variety of things for Magic Items and Gold Coins"""

import random


def d100_dice_roll():
    die = 100
    roll = random.randint(1, die)
    print(roll)


def random_gem_roll(gem):
    gem_sum_roll = 0
    if gem != "":
        for i in range(int(gem[0])):
            roll = random.randint(1, int(gem[2]))
            gem_sum_roll = gem_sum_roll + roll
        print("Gems:", gem_sum_roll)
    else:
        print("Nothing")


class RollRandomMoney:

    def __init__(self,
                 copper,
                 copper_multiplier,
                 silver,
                 silver_multiplier,
                 gold,
                 gold_multiplier,
                 platinum,
                 platinum_multiplier):
        self.copper = copper
        self.copper_multiplier = copper_multiplier
        self.silver = silver
        self.silver_multiplier = silver_multiplier
        self.gold = gold
        self.gold_multiplier = gold_multiplier
        self.platinum = platinum
        self.platinum_multiplier = platinum_multiplier

    def money_roll(self):
        copper_sum_roll = 0
        final_copper = 0
        silver_sum_roll = 0
        final_silver = 0
        gold_sum_roll = 0
        final_gold = 0
        platinum_sum_roll = 0
        final_platinum = 0
        if self.copper != "":
            for i in range(int(self.copper[0])):
                roll = random.randint(1, int(self.copper[2]))
                copper_sum_roll = copper_sum_roll + roll
                if self.copper_multiplier == 0:
                    final_copper = copper_sum_roll
                else:
                    final_copper = copper_sum_roll * self.copper_multiplier
            print("Copper:", final_copper)
        if self.silver != "":
            for i in range(int(self.silver[0])):
                roll = random.randint(1, int(self.silver[2]))
                silver_sum_roll = silver_sum_roll + roll
                if self.silver_multiplier == 0:
                    final_silver = silver_sum_roll
                else:
                    final_silver = silver_sum_roll * self.silver_multiplier
            print("Silver:", final_silver)
        if self.gold != "":
            for i in range(int(self.gold[0])):
                roll = random.randint(1, int(self.gold[2]))
                gold_sum_roll = gold_sum_roll + roll
                if self.gold_multiplier == 0:
                    final_gold = gold_sum_roll
                else:
                    final_gold = gold_sum_roll * self.gold_multiplier
            print("Gold:", final_gold)
        if self.platinum != "":
            for i in range(int(self.platinum[0])):
                roll = random.randint(1, int(self.platinum[2]))
                platinum_sum_roll = platinum_sum_roll + roll
                if self.platinum_multiplier == 0:
                    final_platinum = platinum_sum_roll
                else:
                    final_platinum = platinum_sum_roll * self.platinum_multiplier
            print("Platinum:", final_platinum)
