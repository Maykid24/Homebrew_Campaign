"""This page is for individual treasure payout for small things
    utilizing the Dungeon Master for majority of the treasures with some added spunk"""

import random
from main_page.backend_information.treasure.random_dice_roll import RollRandomMoney


def individual_challenge04():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 30:
        results = RollRandomMoney(copper='5d6', copper_multiplier=0, silver="", silver_multiplier=None,
                                  gold="", gold_multiplier=None, platinum="", platinum_multiplier=None)
        results.money_roll()
    elif 31 <= dice_random <= 60:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver='4d6', silver_multiplier=0,
                                  gold="", gold_multiplier=None, platinum="", platinum_multiplier=None)
        results.money_roll()
    elif 61 <= dice_random <= 70:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold='3d6', gold_multiplier=0, platinum="", platinum_multiplier=None)
        results.money_roll()
    elif 71 <= dice_random <= 95:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold='6d6', gold_multiplier=0, platinum="", platinum_multiplier=None)
        results.money_roll()
    elif 96 <= dice_random <= 100:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold="", gold_multiplier=None, platinum='3d6', platinum_multiplier=0)
        results.money_roll()


def individual_challenge510():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 30:
        results = RollRandomMoney(copper='4d6', copper_multiplier=100, silver='3d6', silver_multiplier=10,
                                  gold="", gold_multiplier=None, platinum="", platinum_multiplier=None)
        results.money_roll()
    elif 31 <= dice_random <= 60:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver='6d6', silver_multiplier=10,
                                  gold='3d6', gold_multiplier=10, platinum="", platinum_multiplier=None)
        results.money_roll()
    elif 61 <= dice_random <= 70:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold='4d6', gold_multiplier=15, platinum="", platinum_multiplier=None)
        results.money_roll()
    elif 71 <= dice_random <= 95:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold='8d6', gold_multiplier=15, platinum="", platinum_multiplier=None)
        results.money_roll()
    elif 96 <= dice_random <= 100:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold='3d6', gold_multiplier=15, platinum='3d6', platinum_multiplier=15)
        results.money_roll()


def individual_challenge1116():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 20:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver='4d6', silver_multiplier=100,
                                  gold='1d6', gold_multiplier=100, platinum="", platinum_multiplier=None)
        results.money_roll()
    elif 21 <= dice_random <= 35:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold='4d6', gold_multiplier=100, platinum="", platinum_multiplier=None)
        results.money_roll()
    elif 36 <= dice_random <= 75:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold='4d6', gold_multiplier=100, platinum='3d6', platinum_multiplier=10)
        results.money_roll()
    elif 76 <= dice_random <= 100:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold='4d6', gold_multiplier=100, platinum='4d6', platinum_multiplier=10)
        results.money_roll()


def individual_challenge17():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 15:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold='10d6', gold_multiplier=100, platinum="", platinum_multiplier=None)
        results.money_roll()
    elif 16 <= dice_random <= 55:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold='3d6', gold_multiplier=1000, platinum='3d6', platinum_multiplier=100)
        results.money_roll()
    elif 56 <= dice_random <= 100:
        results = RollRandomMoney(copper="", copper_multiplier=None, silver="", silver_multiplier=None,
                                  gold='6d6', gold_multiplier=1000, platinum='6d6', platinum_multiplier=100)
        results.money_roll()
