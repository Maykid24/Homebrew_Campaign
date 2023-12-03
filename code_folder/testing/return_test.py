import random

def magic_item_table_a():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 50:
        return "Potion of healing"
    elif 51 <= dice_random <= 60:
        return "Spell Scroll (cantrip)"
    elif 61 <= dice_random <= 70:
        return "Potion of climbing"
    elif 71 <= dice_random <= 90:
        return "Spell scroll (1st Level)"
    elif 91 <= dice_random <= 94:
        return "Spell scroll (2nd Level)"
    elif 95 <= dice_random <= 98:
        return "Potion of greater healing"
    elif dice_random == 99:
        return "Bag of holding"
    elif dice_random == 100:
        return "Driftglobe"

# Example usage:
result = magic_item_table_a()
print(result)
