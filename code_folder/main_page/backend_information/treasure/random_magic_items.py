"""This page is meant to keep track of all the different magic tables from all the DnD books
    This is in effort to keep the individual/group hordes all in one place and easy to utilize very quickly"""


import random


def magic_item_table_a():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 50:
        print("Potion of healing")
    elif 51 <= dice_random <= 60:
        print("Spell Scroll (cantrip)")
    elif 61 <= dice_random <= 70:
        print("Potion of climbing")
    elif 71 <= dice_random <= 90:
        print("Spell scroll (1st Level)")
    elif 91 <= dice_random <= 94:
        print("Spell scroll (2nd Level)")
    elif 95 <= dice_random <= 98:
        print("Potion of greater healing")
    elif dice_random == 99:
        print("Bag of holding")
    elif dice_random == 100:
        print("Driftglobe")


def magic_item_table_b():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 15:
        print("Potion of greater healing")
    elif 16 <= dice_random <= 22:
        print("Potion of fire breath")
    elif 23 <= dice_random <= 29:
        print("Potion of resistance")
    elif 30 <= dice_random <= 34:
        print("Ammunition, +1")
    elif 35 <= dice_random <= 39:
        print("Potion of animal friendship")
    elif 40 <= dice_random <= 44:
        print("Potion of hill giant strength")
    elif 45 <= dice_random <= 49:
        print("Potion of growth")
    elif 50 <= dice_random <= 54:
        print("Potion of water breathing")
    elif 55 <= dice_random <= 59:
        print("Spell scroll (2nd Level)")
    elif 60 <= dice_random <= 64:
        print("Spell scroll (3rd Level)")
    elif 65 <= dice_random <= 67:
        print("Bag of holding")
    elif 68 <= dice_random <= 70:
        print("Keoghtom's ointment")
    elif 71 <= dice_random <= 73:
        print("Pil of slipperiness")
    elif 74 <= dice_random <= 75:
        print("Dust of disappearance")
    elif 76 <= dice_random <= 77:
        print("Dust of dryness")
    elif 78 <= dice_random <= 79:
        print("Dust of sneezing and choking")
    elif 80 <= dice_random <= 81:
        print("Elemental gem")
    elif 82 <= dice_random <= 83:
        print("Philter of love")
    elif dice_random == 84:
        print("Alchemy just")
    elif dice_random == 85:
        print("Cap of water breathing")
    elif dice_random == 86:
        print("Cloak of the manta ray")
    elif dice_random == 87:
        print("Driftglobe")
    elif dice_random == 88:
        print("Goggles of night")
    elif dice_random == 89:
        print("Helm of comprehending languages")
    elif dice_random == 90:
        print("Immovable rod")
    elif dice_random == 91:
        print("Lantern of revealing")
    elif dice_random == 92:
        print("Mariner's armor")
    elif dice_random == 93:
        print("Mithral armor")
    elif dice_random == 94:
        print("Potion of posion")
    elif dice_random == 95:
        print("Ring of swimming")
    elif dice_random == 96:
        print("Robe of useful items")
    elif dice_random == 97:
        print("Rope of climbing")
    elif dice_random == 98:
        print("Saddle of the cavalier")
    elif dice_random == 99:
        print("Wand of magic detection")
    elif dice_random == 100:
        print("Wand of secrets")


def magic_item_table_c():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 15:
        print("Potion of superior healing")
    elif 16 <= dice_random <= 22:
        print("Spell scroll (4th Level)")
    elif 23 <= dice_random <= 27:
        print("Ammunition, +2")
    elif 28 <= dice_random <= 32:
        print("Potion of clairvoyance")
    elif 33 <= dice_random <= 37:
        print("Potion of diminution")
    elif 38 <= dice_random <= 42:
        print("Potion of gaseous form")
    elif 43 <= dice_random <= 47:
        print("Potion of frost giant strength")
    elif 48 <= dice_random <= 52:
        print("Potion of stone giant strength")
    elif 53 <= dice_random <= 57:
        print("Potion of heroism")
    elif 58 <= dice_random <= 62:
        print("Potion of invulnerability")
    elif 63 <= dice_random <= 67:
        print("Potion of mind reading")
    elif 68 <= dice_random <= 72:
        print("Spell scroll (5th Level)")
    elif 73 <= dice_random <= 75:
        print("Elixir of health")
    elif 76 <= dice_random <= 78:
        print("Oil of etherealness")
    elif 79 <= dice_random <= 81:
        print("Potion of fire giant strength")
    elif 82 <= dice_random <= 84:
        print("Quaal's feather token")
    elif 85 <= dice_random <= 87:
        print("Scroll of protection")
    elif 88 <= dice_random <= 89:
        print("Bag of beans")
    elif 90 <= dice_random <= 91:
        print("Bead of force")
    elif dice_random == 92:
        print("Chime of opening")
    elif dice_random == 93:
        print("Decanter of endless water")
    elif dice_random == 94:
        print("Eyes of minute seeing")
    elif dice_random == 95:
        print("Folding boat")
    elif dice_random == 96:
        print("Heward's handy haversack")
    elif dice_random == 97:
        print("Horseshoes of speed")
    elif dice_random == 98:
        print("Necklace of fireballs")
    elif dice_random == 99:
        print("Periapt of health")
    elif dice_random == 100:
        print("Sending stones")


def magic_item_table_d():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 20:
        print("Potion of supreme healing")
    elif 21 <= dice_random <= 30:
        print("Potion of invisibility")
    elif 31 <= dice_random <= 40:
        print("Potion of speed")
    elif 41 <= dice_random <= 50:
        print("Spell scroll (6th Level)")
    elif 51 <= dice_random <= 57:
        print("Spell scroll (7th Level)")
    elif 58 <= dice_random <= 62:
        print("Ammunition, +3")
    elif 63 <= dice_random <= 67:
        print("Oil of sharpness")
    elif 68 <= dice_random <= 72:
        print("Potion of flying")
    elif 73 <= dice_random <= 77:
        print("Potion of cloud giant strength")
    elif 78 <= dice_random <= 82:
        print("Potion of longevity")
    elif 83 <= dice_random <= 87:
        print("Potion of vitality")
    elif 88 <= dice_random <= 92:
        print("Spell scroll (8th Level)")
    elif 93 <= dice_random <= 95:
        print("Horseshoes of a zephyr")
    elif 96 <= dice_random <= 98:
        print("Nolzur's marvelous pigments")
    elif dice_random == 99:
        print("Bag of devouring")
    elif dice_random == 100:
        print("Portable hole")


def magic_item_table_e():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 30:
        print("Spell scroll (8th Level)")
    elif 31 <= dice_random <= 55:
        print("Potion of storm giant strength")
    elif 56 <= dice_random <= 70:
        print("Potion of supreme healing")
    elif 71 <= dice_random <= 85:
        print("Spell scroll (9th Level)")
    elif 86 <= dice_random <= 93:
        print("Universal solvent")
    elif 94 <= dice_random <= 98:
        print("Arrow of slaying")
    elif 99 <= dice_random <= 100:
        print("Sovereign glue")


def magic_item_table_f():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 15:
        print("Weapon, +1")
    elif 16 <= dice_random <= 18:
        print("Shield, +1")
    elif 19 <= dice_random <= 21:
        print("Sentinel shield")
    elif 22 <= dice_random <= 23:
        print("Amulet of proof against detection and location")
    elif 24 <= dice_random <= 25:
        print("Boots of elvenkind")
    elif 26 <= dice_random <= 27:
        print("Boots of striding and springing")
    elif 28 <= dice_random <= 29:
        print("Bracers of archery")
    elif 30 <= dice_random <= 31:
        print("Brooch of shielding")
    elif 32 <= dice_random <= 33:
        print("Broom of flying")
    elif 34 <= dice_random <= 35:
        print("Cloak of elvenkind")
    elif 36 <= dice_random <= 37:
        print("Cloak of protection")
    elif 38 <= dice_random <= 39:
        print("Gauntlets of ogre power")
    elif 40 <= dice_random <= 41:
        print("Hat of disguise")
    elif 42 <= dice_random <= 43:
        print("Javelin of lightning")
    elif 44 <= dice_random <= 45:
        print("Pearl of power")
    elif 46 <= dice_random <= 47:
        print("Rod of the pact keeper, +1")
    elif 48 <= dice_random <= 49:
        print("Slippers of spider climbing")
    elif 50 <= dice_random <= 51:
        print("Staff of the adder")
    elif 52 <= dice_random <= 53:
        print("Staff of the python")
    elif 54 <= dice_random <= 55:
        print("Sword of vengeance")
    elif 56 <= dice_random <= 57:
        print("Trident of fish command")
    elif 58 <= dice_random <= 59:
        print("Wand of magic missiles")
    elif 60 <= dice_random <= 61:
        print("Wand of the war mage, +1")
    elif 62 <= dice_random <= 63:
        print("Wand of web")
    elif 64 <= dice_random <= 65:
        print("Weapon of warning")
    elif dice_random == 66:
        print("Adamantine armor (chain mail)")
    elif dice_random == 67:
        print("Adamantine armor (chain shirt)")
    elif dice_random == 68:
        print("Adamantine armor (scale mail)")
    elif dice_random == 69:
        print("Bag of tricks (gray)")
    elif dice_random == 70:
        print("Bag of tricks (rust)")
    elif dice_random == 71:
        print("Bag of tricks (tan)")
    elif dice_random == 72:
        print("Boots of the winterlands")
    elif dice_random == 73:
        print("Circlet of blasting")
    elif dice_random == 74:
        print("Deck of illusions")
    elif dice_random == 75:
        print("Eversmoking bottle")
    elif dice_random == 76:
        print("Eyes of charming")
    elif dice_random == 77:
        print("Eyes of the eagle")
    elif dice_random == 78:
        print("Figurine of wondrous power (silver raven)")
    elif dice_random == 79:
        print("Gem of brightness")
    elif dice_random == 80:
        print("Gloves of missile snaring")
    elif dice_random == 81:
        print("Gloves of swimming and climbing")
    elif dice_random == 82:
        print("Gloves of thievery")
    elif dice_random == 83:
        print("Headband of intellect")
    elif dice_random == 84:
        print("Helm of telepathy")
    elif dice_random == 85:
        print("Instrument of the bards (Doss lute)")
    elif dice_random == 86:
        print("Instrument of the bards (Fochlucan bandore)")
    elif dice_random == 87:
        print("Instrument of the bards (Mack-Fuimidh cittern)")
    elif dice_random == 88:
        print("Medallion of thoughts")
    elif dice_random == 89:
        print("Necklace of adaption")
    elif dice_random == 90:
        print("Periapt of wound closure")
    elif dice_random == 91:
        print("Pipes of haunting")
    elif dice_random == 92:
        print("Pipes of the sewers")
    elif dice_random == 93:
        print("Ring of jumping")
    elif dice_random == 94:
        print("Ring of mind shielding")
    elif dice_random == 95:
        print("Ring of warmth")
    elif dice_random == 96:
        print("Ring of water walking")
    elif dice_random == 97:
        print("Quiver of Ehlonna")
    elif dice_random == 98:
        print("Stone of good luck")
    elif dice_random == 99:
        print("Wind fan")
    elif dice_random == 100:
        print("Winged Boots")


def magic_item_table_g():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 11:
        print("Weapon, +2")
    elif 12 <= dice_random <= 14:
        print("Figurine of wondrous power (roll d8)")
        d8_random = random.randint(1, 8)
        if d8_random == 1:
            print("Bronze Griffon")
        elif d8_random == 2:
            print("Ebony Fly")
        elif d8_random == 3:
            print("Golden Lions")
        elif d8_random == 4:
            print("Ivory Goats")
        elif d8_random == 5:
            print("Marble Elephant")
        elif 6 <= d8_random <= 7:
            print("Onyx Dog")
        elif d8_random == 8:
            print("Serpentine Owl")
    elif dice_random == 15:
        print("Adamantine armor (breastplate)")
    elif dice_random == 16:
        print("Adamantine armor (splint)")
    elif dice_random == 17:
        print("Amulet of health")
    elif dice_random == 18:
        print("Armor of vulnerability")
    elif dice_random == 19:
        print("Arrow-catching shield")
    elif dice_random == 20:
        print("Belt of dwarvenkind")
    elif dice_random == 21:
        print("Belt of hill giant strength")
    elif dice_random == 22:
        print("Berserker axe")
    elif dice_random == 23:
        print("Boots of levitation")
    elif dice_random == 24:
        print("Boots of speed")
    elif dice_random == 25:
        print("Bowl of commanding water elementals")
    elif dice_random == 26:
        print("Bracers of defense")
    elif dice_random == 27:
        print("Brazier of commanding fire elementals")
    elif dice_random == 28:
        print("Cape of the mountebank")
    elif dice_random == 29:
        print("Censer of controlling air elementals")
    elif dice_random == 30:
        print("Armor, +1 chain mail")
    elif dice_random == 31:
        print("Armor of resistance (chain mail)")
    elif dice_random == 32:
        print("Armor of resistance (chain shirt)")
    elif dice_random == 33:
        print("Armor,+ 1 chain shirt")
    elif dice_random == 34:
        print("Cloak of displacement")
    elif dice_random == 35:
        print("Cloak of the bat")
    elif dice_random == 36:
        print("Cube of force")
    elif dice_random == 37:
        print("Daern's instant fortress")
    elif dice_random == 38:
        print("Dagger of venom")
    elif dice_random == 39:
        print("Dimensional shackles")
    elif dice_random == 40:
        print("Dragon slayer")
    elif dice_random == 41:
        print("Elven chain")
    elif dice_random == 42:
        print("Flame tongue")
    elif dice_random == 43:
        print("Gem of seeing")
    elif dice_random == 44:
        print("Giant slayer")
    elif dice_random == 45:
        print("Clamoured studded leather")
    elif dice_random == 46:
        print("Helm of teleportation")
    elif dice_random == 47:
        print("Horn of blasting")
    elif dice_random == 48:
        print("Horn of Valhalla (silver or brass)")
    elif dice_random == 49:
        print("Instrument of the bards (Canaithmandolin)")
    elif dice_random == 50:
        print("Instrument ofthe bards (Cii lyre)")
    elif dice_random == 51:
        print("loun stone (awareness)")
    elif dice_random == 52:
        print("loun stone (protection)")
    elif dice_random == 53:
        print("loun stone (reserve)")
    elif dice_random == 54:
        print("loun stone (sustenance)")
    elif dice_random == 55:
        print("Iron bands of Bilarro")
    elif dice_random == 56:
        print("Armor, + 1 leather")
    elif dice_random == 57:
        print("Armor of resistance (leather)")
    elif dice_random == 58:
        print("Mace of disruption")
    elif dice_random == 59:
        print("Mace of smiting")
    elif dice_random == 60:
        print("Mace of terror")
    elif dice_random == 61:
        print("Mantle of spell resistance")
    elif dice_random == 62:
        print("Necklace of prayer beads")
    elif dice_random == 63:
        print("Periapt of proof against poison")
    elif dice_random == 64:
        print("Ring of animal influence")
    elif dice_random == 65:
        print("Ring of evasion")
    elif dice_random == 66:
        print("Ring of feather falling")
    elif dice_random == 67:
        print("Ring of free action")
    elif dice_random == 68:
        print("Ring of protection")
    elif dice_random == 69:
        print("Ring of resistance")
    elif dice_random == 70:
        print("Ring of spell storing")
    elif dice_random == 71:
        print("Ring of the ram")
    elif dice_random == 72:
        print("Ring of X-ray vision")
    elif dice_random == 73:
        print("Robe of eyes")
    elif dice_random == 74:
        print("Rod of rulership")
    elif dice_random == 75:
        print("Rod of the pact keeper, +2")
    elif dice_random == 76:
        print("Rope of entanglement")
    elif dice_random == 77:
        print("Armor, +1 scale mail")
    elif dice_random == 78:
        print("Armor of resistance (scale mail)")
    elif dice_random == 79:
        print("Shield, +2")
    elif dice_random == 80:
        print("Shield of missile attraction")
    elif dice_random == 81:
        print("Staff of charming")
    elif dice_random == 82:
        print("Staff of healing")
    elif dice_random == 83:
        print("Staff of swarming insects")
    elif dice_random == 84:
        print("Staff of the woodlands")
    elif dice_random == 85:
        print("Staff of withering")
    elif dice_random == 86:
        print("Stone of controlling earthelementals")
    elif dice_random == 87:
        print("Sun blade")
    elif dice_random == 88:
        print("Sword of life stealing")
    elif dice_random == 89:
        print("Sword of wounding")
    elif dice_random == 90:
        print("Tentacle rod")
    elif dice_random == 91:
        print("Vicious weapon")
    elif dice_random == 92:
        print("Wand of binding")
    elif dice_random == 93:
        print("Wand of enemy detection")
    elif dice_random == 94:
        print("Wand of fear")
    elif dice_random == 95:
        print("Wand of fireballs")
    elif dice_random == 96:
        print("Wand of lightning bolts")
    elif dice_random == 97:
        print("Wand of paralysis")
    elif dice_random == 98:
        print("Wand of the war mage, +2")
    elif dice_random == 99:
        print("Wand of wonder")
    elif dice_random == 100:
        print("Wings of flying")


def magic_item_table_h():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 10:
        print("Weapon, +3")
    elif 11 <= dice_random <= 12:
        print("Amulet of the planes")
    elif 13 <= dice_random <= 14:
        print("Carpet of flying")
    elif 15 <= dice_random <= 16:
        print("Crystal ball (very rare version)")
    elif 17 <= dice_random <= 18:
        print("Ring of regeneration")
    elif 19 <= dice_random <= 20:
        print("Ring of shooting stars")
    elif 21 <= dice_random <= 22:
        print("Ring of telekinesis")
    elif 23 <= dice_random <= 24:
        print("Robe of scintillating colors")
    elif 25 <= dice_random <= 26:
        print("Robe of stars")
    elif 27 <= dice_random <= 28:
        print("Rod of absorption")
    elif 29 <= dice_random <= 30:
        print("Rod of alertness")
    elif 31 <= dice_random <= 32:
        print("Rod of security")
    elif 33 <= dice_random <= 34:
        print("Rod of the pact keeper, +3")
    elif 35 <= dice_random <= 36:
        print("Scimitar of speed")
    elif 37 <= dice_random <= 38:
        print("Shield, +3")
    elif 39 <= dice_random <= 40:
        print("Staff of fire")
    elif 41 <= dice_random <= 42:
        print("Staff of frost")
    elif 43 <= dice_random <= 44:
        print("Staff of power")
    elif 45 <= dice_random <= 46:
        print("Staff of striking")
    elif 47 <= dice_random <= 48:
        print("Staff of thunder and lightning")
    elif 49 <= dice_random <= 50:
        print("Sword of sharpnes")
    elif 51 <= dice_random <= 52:
        print("Wand of polymorph")
    elif 53 <= dice_random <= 54:
        print("Wand of the war mage, + 3")
    elif dice_random == 55:
        print("Adamantine armor (half plate)")
    elif dice_random == 56:
        print("Adamantine armor (plate)")
    elif dice_random == 57:
        print("Animated shield")
    elif dice_random == 58:
        print("Belt of fire giant strength")
    elif dice_random == 59:
        print("Belt of frost (or stone) giant strength")
    elif dice_random == 60:
        print("Armor, + 1 breastplate")
    elif dice_random == 61:
        print("Armor of resistance (breastplate)")
    elif dice_random == 62:
        print("Candle of invocation")
    elif dice_random == 63:
        print("Armor, +2 chain mail")
    elif dice_random == 64:
        print("Armor, +2 chain shirt")
    elif dice_random == 65:
        print("Cloak of arachnida")
    elif dice_random == 66:
        print("Dancing sword")
    elif dice_random == 67:
        print("Demon armor")
    elif dice_random == 68:
        print("Dragon scale mail")
    elif dice_random == 69:
        print("Dwarven plate")
    elif dice_random == 70:
        print("Dwarven thrower")
    elif dice_random == 71:
        print("Efreeti bottle")
    elif dice_random == 72:
        print("Figurine of wondrous power (obsidian steed)")
    elif dice_random == 73:
        print("Frost brand")
    elif dice_random == 74:
        print("Helm of brilliance")
    elif dice_random == 75:
        print("Horn ofValhalla (bronze)")
    elif dice_random == 76:
        print("Instrument of the bards (Anstruthharp)")
    elif dice_random == 77:
        print("loun stone (absorption)")
    elif dice_random == 78:
        print("loun stone (agility)")
    elif dice_random == 79:
        print("loun stone (fortitude)")
    elif dice_random == 80:
        print("loun stone (insight)")
    elif dice_random == 81:
        print("loun stone (intellect)")
    elif dice_random == 82:
        print("loun stone (leadership)")
    elif dice_random == 83:
        print("loun stone (strength)")
    elif dice_random == 84:
        print("Armor, +2 leather")
    elif dice_random == 85:
        print("Manual of bodily health")
    elif dice_random == 86:
        print("Manual of gainful exercise")
    elif dice_random == 87:
        print("Manual of golems")
    elif dice_random == 88:
        print("Manual of quickness of action")
    elif dice_random == 89:
        print("Mirror of life trapping")
    elif dice_random == 90:
        print("Nine lives stealer")
    elif dice_random == 91:
        print("Oathbow")
    elif dice_random == 92:
        print("Armor, +2 scale mail")
    elif dice_random == 93:
        print("Spellguard shield")
    elif dice_random == 94:
        print("Armor, + 1 splint")
    elif dice_random == 95:
        print("Armor of resistance (splint)")
    elif dice_random == 96:
        print("Armor, + 1 studded leather")
    elif dice_random == 97:
        print("Armor of resistance (studded leather)")
    elif dice_random == 98:
        print("Tome of clear thought")
    elif dice_random == 99:
        print("Tome of leadership and influence")
    elif dice_random == 100:
        print("Tome of understanding")


def magic_item_table_i():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 5:
        print("Defender")
    elif 6 <= dice_random <= 10:
        print("Hammer of thunderbolts")
    elif 11 <= dice_random <= 15:
        print("Luck Blade")
    elif 16 <= dice_random <= 20:
        print("Sword of answering")
    elif 21 <= dice_random <= 23:
        print("Holy avenger")
    elif 24 <= dice_random <= 26:
        print("Ring of djinni summoning")
    elif 27 <= dice_random <= 29:
        print("Ring of invisibility")
    elif 30 <= dice_random <= 32:
        print("Ring of spell turning")
    elif 36 <= dice_random <= 38:
        print("Rod of lordly might")
    elif 39 <= dice_random <= 41:
        print("Vorpal sword")
    elif 42 <= dice_random <= 43:
        print("Belt of cloud giant strength")
    elif 44 <= dice_random <= 45:
        print("Armor, +2 breastplate")
    elif 46 <= dice_random <= 47:
        print("Armor, +3 chain mail")
    elif 48 <= dice_random <= 49:
        print("Armor, +3 chain shirt")
    elif 50 <= dice_random <= 51:
        print("Cloak of invisibility")
    elif 52 <= dice_random <= 53:
        print("Crystal ball (legendary version)")
    elif 54 <= dice_random <= 55:
        print("Armor, + 1 half plate")
    elif 56 <= dice_random <= 57:
        print("Iron flask")
    elif 58 <= dice_random <= 59:
        print("Armor, +3 leather")
    elif 60 <= dice_random <= 61:
        print("Armor, +1 plate")
    elif 62 <= dice_random <= 63:
        print("Robe of the archmagi")
    elif 64 <= dice_random <= 65:
        print("Rod of resurrection")
    elif 66 <= dice_random <= 67:
        print("Armor, +1 scale mail")
    elif 68 <= dice_random <= 69:
        print("Scarab of protection")
    elif 70 <= dice_random <= 71:
        print("Armor, +2 splint")
    elif 72 <= dice_random <= 73:
        print("Armor, +2 studded leather")
    elif 74 <= dice_random <= 75:
        print("Well of many worlds")
    elif dice_random == 76:
        print("Magic armor (roll d12)")
        d12_random = random.randint(1, 12)
        if 1 <= d12_random <= 2:
            print("Armor, +2 Half Plate")
        elif 3 <= d12_random <= 4:
            print("Armor, +2 Place")
        elif 5 <= d12_random <= 6:
            print("Armor, +3 studded leather")
        elif 7 <= d12_random <= 8:
            print("Armor, +3 Breastplate")
        elif 9 <= d12_random <= 10:
            print("Armor, +3 Splint")
        elif d12_random == 11:
            print("Armor, +3 Half Plate")
        elif d12_random == 12:
            print("Armor, +3 Plate")
    elif dice_random == 77:
        print("Apparatus of Kwalish")
    elif dice_random == 78:
        print("Armor of invulnerability")
    elif dice_random == 79:
        print("Belt of storm giant strength")
    elif dice_random == 80:
        print("Cubic gate")
    elif dice_random == 81:
        print("Deck of many things")
    elif dice_random == 82:
        print("Efreeti chain")
    elif dice_random == 83:
        print("Armor of resistance (half plate)")
    elif dice_random == 84:
        print("Horn ofValhalla (iron)")
    elif dice_random == 85:
        print("Instrument of the bards (OIIamh harp)")
    elif dice_random == 86:
        print("loun stone (greater absorption)")
    elif dice_random == 87:
        print("loun stone (mastery)")
    elif dice_random == 88:
        print("loun stone (regeneration)")
    elif dice_random == 89:
        print("Plate armor of etherealness")
    elif dice_random == 90:
        print("Plate armor of resistance")
    elif dice_random == 91:
        print("Ring of air elemental command")
    elif dice_random == 92:
        print("Ring of earthelemental command")
    elif dice_random == 93:
        print("Ring of fire elemental command")
    elif dice_random == 94:
        print("Ring of three wishes")
    elif dice_random == 95:
        print("Ring of water elemental command")
    elif dice_random == 96:
        print("Sphere of annihilation")
    elif dice_random == 97:
        print("Talisman of pure good")
    elif dice_random == 98:
        print("Talisman of the sphere")
    elif dice_random == 99:
        print("Talisman of ultimate evil")
    elif dice_random == 100:
        print("Tome of the stilled tongue")