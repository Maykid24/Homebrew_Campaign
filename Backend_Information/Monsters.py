"""
Will create a list of Monsters and the CR state along with Page Numbers
May contain initial stats as well along with Initiative rolls (Dex Stats)

CR to XP
0 - 10XP, 0
1/8 - 25XP, 1/8
1/4 - 50XP
1/2 - 100XP
1 - 200XP
2 - 450XP
3 - 700XP
4 - 1100XP
5 - 1800XP
6 - 2300XP
7 - 2900XP
8 - 3900XP
9 - 5000XP
10 - 5900XP
11 - 7200XP
12 - 8400XP
13 - 10000XP
14 - 11500XP
15 - 13000XP
16 - 15000XP
17 - 18000XP
18 - 20000XP
19 - 22000XP
20 - 25000XP
21 - 33000XP
22 - 41000XP
23 - 50000XP
24 - 62000XP
25 - 75000XP
26 - 90000XP

"""

monsters_category = {
    'artic': {
        1: {'Name': 'Commoner, Owl', 'CR': '10XP, 0'},
        2: {'Name': 'Bandit, Blood Hawk, Kobold, Tribal Warrior', 'CR': '25XP, 1/8'},
        3: {'Name': 'Giant Owl, Winged Kobold, Gnoll Witherling', 'CR': '50XP, 1/4'},
        4: {'Name': 'Ice Mephit, Orc, Scout, Gnoll Hunter', 'CR': '100XP, 1/2'},
        5: {'Name': 'Brown Bear, Half-Ogre, Gnoll Flesh Gnawer', 'CR': '200XP, 1'},
        6: {'Name': 'Bandit Captain, Berserker, Druid, Griffon, Ogre, Orce Ey of Gruumsh, Orog, Polar Bear, '
                    'Saber-Toothed Tiger, Guard Drake', 'CR': '450XP, 2'},
        7: {'Name': 'Manitcore, Veteran, Winter Wolf, Yeti, Vampiric Mist', 'CR': '700XP, 3'},
        8: {'Name': 'Revenant, Troll, Werebear, Young Remorhaz, Warlock of the Archfey', 'CR': '1800XP, 5'},
        9: {'Name': 'Mammoth, Young White Dragon, Warlock of the Great Old One', 'CR': '2300XP, 6'},
        10: {'Name': 'Bheur Hag, Lost Sorrowsworn, Warlock of the Fiend', 'CR': '2900XP, 7'},
        11: {'Name': 'Frost Giant', 'CR': '3900XP, 8'},
        12: {'Name': 'Abominable Yeti, Frost Salamander', 'CR': '5000XP, 9'},
        13: {'Name': 'Winter Eladrin', 'CR': '5900XP, 10'},
        14: {'Name': 'Remorhaz, Roc', 'CR': '7200XP, 11'},
        15: {'Name': 'Boneclaw', 'CR': '8400XP, 12'},
        16: {'Name': 'Adult White Dragon, Dire Troll', 'CR': '10000XP, 13'},
        17: {'Name': 'Ancient White Dragon, Nightwalker', 'CR': '25000XP, 20'},
        18: {'Name': 'Eder Tempest', 'CR': '50000XP, 23'}
    },
    'coastal': {
        1: {'Name': 'Commoner, Crab, Eagle', 'CR': '10XP, 0'},
        2: {'Name': 'Bandit, Blood Hawk, Giant Crab, Guard, Kobold, Merfolk, Poisonous Snake, Stirge, '
                    'Tribal Warrior, Dolphin', 'CR': '25XP, 1/8'},
        3: {'Name': 'Giant Lizard, Giant Wolf Spider, Pseudodragon, Pteranodon, Winged Kobold, Dimetrodon, '
                    'Tortle', 'CR': '50XP, 1/4'},
        4: {'Name': 'Sahuagin, Scout, Skulk', 'CR': '100XP, 1/2'},
        5: {'Name': 'Giant Eagel, Giant Toad, Harpy, Sea Spawn', 'CR': '200XP, 1'},
        6: {'Name': 'Bandit Captain, Berserker, Druid, Griffon, Ogre, Merrow, Plesiosaurus, Sahuagin Priestess,'
                    'Sea Hag, Quetzalcoatlus, Tortle Druid', 'CR': '450XP, 2'},
        7: {'Name': 'Manticore, Veteran, Deep Scion, Dolphin Delighter, Merrenoloth, Swashbuckler, Vampiric Mist',
            'CR': '700XP, 3'},
        8: {'Name': 'Banshee', 'CR': '1100XP, 4'},
        9: {'Name': 'Sahuagin Baron, Water Elemental, Kraken Priest', 'CR': '1800XP, 5'},
        10: {'Name': 'Cyclops', 'CR': '2300XP, 6'},
        11: {'Name': 'Young Bronze Dragon, Canoloth, Shoosuva', 'CR': '3900XP, 8'},
        12: {'Name': 'Young Blue Dragon, Flind, Lonely Sorrowsworn', 'CR': '5000XP, 9'},
        13: {'Name': 'Stone Giant Dreamwalker', 'CR': '5900XP, 10'},
        14: {'Name': 'Djinni, Marid, Roc, Balhannoth, Morkoth, Spirit Troll', 'CR': '7200XP, 11'},
        15: {'Name': 'Eidolon, Frost Giant Everlasting One, Ki-Rin', 'CR': '8400XP, 12'},
        16: {'Name': 'Storm Giant, Wastrilith', 'CR': '10000XP, 13'},
        17: {'Name': 'Adult Bronze Dragon', 'CR': '13000XP, 15'},
        18: {'Name': 'Adult Blue Dragon, Storm Giant Quintessent', 'CR': '15000XP, 16'},
        19: {'Name': 'Dragon Turtle, Blue Abishai, Nagpa', 'CR': '18000XP, 17'},
        20: {'Name': 'Leviathan', 'CR': '25000XP, 20'},
        21: {'Name': 'Ancient Bronze Dragon', 'CR': '41000XP, 22'},
        22: {'Name': 'Ancient Blue Dragon, Elder Tempest', 'CR': '50000XP, 23'}
    },
    'desert': {
        1: {'Name': 'Cat, Commoner, Hyena, Jackal, Scorpion, Vulture', 'CR': '10XP, 0'},
        2: {'Name': 'Bandit, Camel, Flying Snake, Guard, Kobold, Mule, Poisonous Snake, Stirge,'
                    'Tribal Warrior, Young Kruthik', 'CR': '25XP, 1/8'},
        3: {'Name': 'Constrictor Snake, Giant Lizard, Giant Poisonous Snake, Giant Wolf Spider, Pseudodragon, '
                    'Winged Kobold', 'CR': '50XP, 1/4'},
        4: {'Name': 'Dust Mephit, Gnoll, Hobgoblin, Jackalwere, Scout, Swarm of Insects, Firenewt Warrior',
            'CR': '100XP, 1/2'},
        5: {'Name': 'Death Dog, Giant Hyena, Giant Spider, Giant Toad, Giant Vulture, Half-Ogre, Lion,'
                    'Thri-kreen, Yuan-ti Pureblood, Meazel, Stone Cursed, Vargouille', 'CR': '200XP, 1'},
        6: {'Name': 'Bandit Captain, Berserker, Druid, Giant Constrictor, Snake, Gnoll Pack Lord, Ogre, Adult Kruthik, '
                    'Berbalang, Guard Drake, Yuan-Ti, Broodguard', 'CR': '450XP, 2'},
        7: {'Name': 'Giant Scorpion, Hobgoblin Captain, Mummy, Phase Spider, Wight, Yuan-ti Malison, Leucrotta',
            'CR': '700XP, 3'},
        8: {'Name': 'Couatl, Gnoll Fang of Yeenoghu, Lamia, Weretiger, Dybbuk, Yuan-Ti Mind Whisperer, '
                    'Yuan-Ti Nightmare Speaker', 'CR': '1100XP, 4'},
        9: {'Name': 'Air Elemental, Fire Elemental, Revenant, Kruthik Hive Lord, Spawn of Kyuss, Tlincalli, '
                    'Yuan-Ti Pit Master', 'CR': '1800XP, 5'},
        10: {'Name': 'Cyclops, Medusa, Young Brass Dragon', 'CR': '2300XP, 6'},
        11: {'Name': 'Yuan-ti Abomination, Lost Sorrowsworn, Warlock of the Fiend', 'CR': '2900XP, 7'},
        12: {'Name': 'Howler', 'CR': '3900XP, 8'},
        13: {'Name': 'Young Blue Dragon, Champion, Lonely Sorrwsworn, Necromancer Wizard, Rot Troll, War Priest',
             'CR': '5000XP, 9'},
        14: {'Name': 'Guardian Naga, Githyanki Gish, Githzerai Enlightened, Orthon, Summer Eladrin', 'CR': '5900XP, 10'},
        15: {'Name': 'Efreeti, Gynosphinx, Roc', 'CR': '7200XP, 11'},
        16: {'Name': 'Boneclaw, Eidolon, Githyanki Kith"rak, ki-rin, Oinoloth, Yuan-Ti Anathema', 'CR': '8400XP, 12'},
        17: {'Name': 'Adult Brass Dragon', 'CR': '10000XP, 13'},
        18: {'Name': 'Githyanki Supreme Commander, Retriever', 'CR': '11500XP, 14'},
        19: {'Name': 'Mummy Lord, Purple Worm, Skull Lord', 'CR': '13000XP, 15'},
        20: {'Name': 'Adult Blue Dragon, Phoenix, Storm Giant Quintessent', 'CR': '15000XP, 16'},
        21: {'Name': 'Adult Blue Dracolish, Androsphinx, Nagpa', 'CR': '18000XP, 17'},
        22: {'Name': 'Ancient Brass Dragon, Nightwalker', 'CR': '25000XP, 20'},
        23: {'Name': 'Zaratan', 'CR': '41000XP, 22'},
        24: {'Name': 'Ancient Blue Dragon', 'CR': '50000XP, 23'},
    },
    'forest': {
        1: {'Name': 'Awakened Shrub, Baboon, Badger, Cat, Commoner, Deer, Hyena, Owl', 'CR': '10XP, 0'},
        2: {'Name': 'Bandit, Blood Hawk, Flying Snake, Giant Rat, Giant Weasel, Guard, Kobold, Mastiff, Poisonous Snake,'
                    'Stirge, Tribal Warrior, Twig Blight, Boggle', 'CR': '25XP, 1/8'},
        3: {'Name': 'Blink Dog, Boar, Constrictor Snake, Elk, Giant Badger, Giant Bat, Giant Frog, Giant Lizard, Giant Owl,'
                    'Giant Poisonous Snake, Giant Wolf Spider, Gobline, Kenku, Needle Blight, Panther, Pixie,'
                    'Pseudodragon, Sprite, Swarm of Ravens, Winged Kobold, Wolf, Gnoll Witherling, Grung, '
                    'Kobold Inventor, Vegepygmy, Velociraptor', 'CR': '50XP, 1/4'},
        4: {'Name': 'Ape, Black Bear, Giant Wasp, Gnoll, Hobgoblin, Lizardfolk, Ord, Satyr, Scout, Swarm of Insects, '
                    'Vine Blight, Worg, Darkling, Gnoll Hunter, Skulk', 'CR': '100XP, 1/2'},
        5: {'Name': 'Brown Bear, Bugbear, Dire Wolf, Dryad, Faerie Dragon (Yellow or Younger), Giant Hyena,'
                    'Giant Spider, Giant Toad, Goblin Boss, Half-Ogre, Harpy, Tiger, Yuan-ti Pureblood, Choker, '
                    'Clockwork Bronze Scout, Deinonychus, Gnoll Flesh Gnawer, Grung Wildling, Kobold Dragonshield, '
                    'Kobold Scale Sorcerer, Meazel, Nilbog, Quickling, Thorny Vegepygmy', 'CR': '200XP, 1'},
        6: {'Name': 'Ankheg, Awakened Tree, Bandit Captain, Berserker, Centaur, Druid, Ettercap, Faerie Dragon '
                    '(Green or Older), Giant Boar, Giant Constrictor Snake, Giant Elk, Gnoll Pack Lord, Grick,'
                    'Lizardfolk Shaman, Ogre, Orc, Eye of Gruumsh, Orog, Pegasus, Swarm of Poisonous Snakes,'
                    'Wererat, Will-o-Wisp, Darkling Elder, Grung Elite Warrior, Guard Drake, Hobgoblin Iron Shadow,'
                    'Meenlock, Shadow Mastiff, Vegepygmy Chief, Yuan-Ti Broodguard', 'CR': '450XP, 2'},
        7: {'Name': 'Displacer Beast, Green Hag, Hobgoblin Captain, Owlbear, Phase Spider, Veteran, Werewolf, '
                    'Yuan-ti Malison, Archer, Flail Snail, Redcap, Shadow Mastiff Alpha, Vampiric Mist', 'CR': '700XP, 3'},
        8: {'Name': 'Banshee, Couatl, Gnoll Fang of Yeenoghu, Wereboar, Weretiger, Barghest, Clockwork Iron Cobra, '
                    'Clockwork Stone Defender, Girallon, Hobgoblin Devastator, Stegosaurus, Warlock of the Archfey, '
                    'Yeth Hound, Yuan-Ti Mind Whisperer, Yuan-Ti Nightmare Speaker', 'CR': '1100XP, 4'},
        9: {'Name': 'Gogon, Revenant, Shambling Mound, Troll, Unicorn, Werebear, Brontosaurus, Clockwork Oaken Bolter, '
                    'Wood Woad, Yuan-Ti Pit Master', 'CR': '1800XP, 5'},
        10: {'Name': 'Giant Ape, Grick Alpha, Oni, Yuan-ti Abomination, Korred, Lost Sorrowsworn, '
                     'Shadar-Kai Shadow Dancer, Venom Troll', 'CR': '2900XP, 7'},
        11: {'Name': 'Young Green Dragon, Corpse Flower, Shoosuva', 'CR': '3900XP, 8'},
        12: {'Name': 'Treant, Flind, Rot Troll', 'CR': '5000XP, 9'},
        13: {'Name': 'Guardian Naga, Young Gold Dragon, Autumn Eladrin, Spring Eladrin, Summer Eladrin, Winter Eladrin',
             'CR': '5900XP, 10'},
        14: {'Name': 'Hungry Sorrowsworn, Spirit Troll', 'CR': '7200XP, 11'},
        15: {'Name': 'Archdruid, Eidolon, Gray Render, Yuan-Ti Anathema', 'CR': '8400XP, 12'},
        16: {'Name': 'Dire Troll', 'CR': '10000XP, 13'},
        17: {'Name': 'Retriever', 'CR': '11500XP, 14'},
        18: {'Name': 'Adult Green Dragon', 'CR': '13000XP, 15'},
        19: {'Name': 'Adult Gold Dragon, Nagpa', 'CR': '18000XP, 17'},
        20: {'Name': 'Ancient Green Dragon, Zaratan', 'CR': '41000XP, 22'},
        21: {'Name': 'Ancient Gold Dragon', 'CR': '62000XP, 24'},
    },
    'grassland': {
        1: {'Name': 'Cat, Commoner, Deer, Eagle, Goat, Hyena, Jackal, Vulture', 'CR': '10XP, 0'},
        2: {'Name': 'Blood Hawk, Flying Snake, Giant Weasel, Guard, Poisonous Snake, Stirge, Tribal Warrior',
            'CR': '25XP, 1/8'},
        3: {'Name': 'Axe Beak, Boar, Elk, Giant Poisonous Snake, Giant Wolf Spider, Goblin, Panther (Leopard),'
                    'Pteranodon, Riding Horse, Wolf, Gnoll Witherling, Hadrosaurus, Ox, Velociraptor', 'CR': '50XP, 1/4'},
        4: {'Name': 'Cockatrice, Giant Goat, Giant Wasp, Gnoll, Hobgoblin, Jackalwere, Orc, Scout, Swarm of Insects,'
                    'Worg, Gnoll Hunter, Stench Kow', 'CR': '100XP, 1/2'},
        5: {'Name': 'Bugbear, Giant Eagle, Giant Hyena, Giant Vulture, Goblin Boss, Hippogriff, Lion, Scarecrow, '
                    'Thri-Kreen, Tiger, Clockwork Bronze Scout, Deinonychus, Gnoll Flesh Gnawer, Meazel', 'CR': '200XP, 1'},
        6: {'Name': 'Allosaurus, Ankheg, Centaur, Druid, Giant Boar, Giant Elk, Gnoll Pack Lord, Griffon, Ogre, '
                    'Orc Eye of Gruumsh, Orog, Pegasus, Rhinoceros, Aurochs, Hobgoblin Iron Shadow, Ogre Bolt Launcher, '
                    'Ogre Howdah', 'CR': '450XP, 2'},
        7: {'Name': 'Ankylosaurus, Hobgoblin Captain, Manticore, Phase Spider, Veteran, Leucrotta, Ogre Chain Brute, '
                    'Sword Wraith Warrior, Vampiric Mist', 'CR': '700XP, 3'},
        8: {'Name': 'Coutl, Elephant, Gnoll Fang of Yeenoghu, Wereboar, Weretiger, Barghest, Clockwork Iron Cobra, '
                    'Clockwork Stone Defender, Hobgoblin Devastator, Ogre Battering Ram, Stegosaurus, Yeth Hound',
            'CR': '1100XP, 4'},
        9: {'Name': 'Bulette, Gorgon, Triceratops, Brontosaurus, Clockwork Oaken Bolter', 'CR': '1800XP, 5'},
        10: {'Name': 'Chimera, Cyclops, Mouth of Grolantor', 'CR': '2300XP, 6'},
        11: {'Name': 'Tyrannosaurus Rex, Howler, Shoosuva, Sword Wraith Commander', 'CR': '3900XP, 8'},
        12: {'Name': 'Flind', 'CR': '5000XP, 9'},
        13: {'Name': 'Young Gold Dragon, Spring Eladrin', 'CR': '5900XP, 10'},
        14: {'Name': 'Eidolon, Ki-Rin', 'CR': '8400XP, 12'},
        15: {'Name': 'Cadaver Collector', 'CR': '11500XP, 14'},
        16: {'Name': 'Adult Gold Dragon', 'CR': '18000XP, 17'},
        17: {'Name': 'Zaratan', 'CR': '41000XP, 22'},
        18: {'Name': 'Elder Tempest', 'CR': '50000XP, 23'},
        19: {'Name': 'Ancient Gold Dragon', 'CR': '62000XP, 24'},
    },
    'hill': {
        1: {'Name': 'Baboon, Commoner, Eagle, Goat, Hyena, Raven, Vulture', 'CR': '10XP, 0'},
        2: {'Name': 'Bandit, Blood Hawk, Giant Weasel, Guard, Kobold, Mastiff, Mule, Poisonous Snake, Stirge,'
                    'Tribal Warrior, Boggle, Neogi Hatchling, Xvart', 'CR': '25XP, 1/8'},
        3: {'Name': 'Axe Beak, Boar, Elk, Giant Owl, Giant Wolf Spider, Goblin, Panther (Cougar), Pseudodragon,'
                    'Swarm of Bats, Swarm of Ravens, Winged Kobold, Wolf, Gnoll Witherling, '
                    'Kobold Inventor', 'CR': '50XP, 1/4'},
        4: {'Name': 'Giant Goat, Gnoll, Hobgoblin, Orc, Scout, Swarm of Insects, Worg, Firenewt Warrior, '
                    'Gnoll Hunter', 'CR': '100XP, 1/2'},
        5: {'Name': 'Brown Bear, Dire Wolf, Giant Eagle, Giant Hyena, Goblin Boss, Half-Ogre, Garpy, Hippogriff,'
                    'Lion, Clockwork Bronze Scout, Deinonychus, Firenewt Warlock of Imix, Giant Strider, '
                    'Gnoll Flesh Gnawer, Kobold Dragonshield, Kobold Scale Sorcerer, Meazel, Nilbog, '
                    'Xvart Warlock of Raxivort', 'CR': '200XP, 1'},
        6: {'Name': 'Bandit Captain, Berserker, Druid, Giant Boar, Giant Elk, Gnoll Pack Lord, Griffon, Orge, '
                    'Orc Eye of Gruumsh, Orog, Pegasus, Peryton, Aurochs, Hobgoblin Iron Shadow, Ogre Bolt Launcher, '
                    'Ogre Howdah, Quetzalcoatlus, Shadow Mastiff', 'CR': '450XP, 2'},
        7: {'Name': 'Green Hag, Hobgoblin Captain, Manticore, Phase Spider, Veteran, Werewolf, Neogi, Ogre Chain Brute, '
                    'Redcap, Shadow Mastiff Alpha', 'CR': '700XP, 3'},
        8: {'Name': 'Ettin, Gnoll Fang of Yeenoghu, Wereboar, Barghest, Clockwork Iron Cobra, Clockwork Stone Defender, '
                    'Hobgoblin Devastator, Neogi Master, Ogre Battering Ram, Yeth Hound', 'CR': '1100XP, 4'},
        9: {'Name': 'Bulette, Gorgon, Hill Giant, Revenant, Troll, Werebear, Clockwork Oaken Boter, Tanarukk',
            'CR': '1800XP, 5'},
        10: {'Name': 'Chimera, Cyclops, Galeb Duhr, Wyvern, Annis Hag, Mouth of Grolantor, '
                     'Warlock of the Great Old One', 'CR': '2300XP, 6'},
        11: {'Name': 'Stone Giant, Young Copper Dragon', 'CR': '2900XP, 7'},
        12: {'Name': 'Howler, Shoosuva', 'CR': '3900XP, 8'},
        13: {'Name': 'Flind', 'CR': '5000XP, 9'},
        14: {'Name': 'Young Red Dragon, Stone Giant Dreamwalker', 'CR': '5900XP, 10'},
        15: {'Name': 'Roc', 'CR': '7200XP, 11'},
        16: {'Name': 'Gray Render', 'CR': '8400XP, 12'},
        17: {'Name': 'Dire Troll', 'CR': '10000XP, 13'},
        18: {'Name': 'Adult Copper Dragon', 'CR': '11500XP, 14'},
        19: {'Name': 'Adult Red Dragon', 'CR': '18000XP, 17'},
        20: {'Name': 'Ancient Copper Dragon', 'CR': '33000XP, 21'},
        21: {'Name': 'Zaratan', 'CR': '41000XP, 22'},
        22: {'Name': 'Elder Tempest', 'CR': '50000XP, 23'},
        23: {'Name': 'Ancient Red Dragon', 'CR': '62000XP, 24'},
    },
    'mountain': {
        1: {'Name': 'Eagle, Goat', 'CR': '10XP, 0'},
        2: {'Name': 'Blood Hawk, Guard, Kobold, Stirge, Tribal Warrior, Young Kruthik', 'CR': '25XP, 1/8'},
        3: {'Name': 'Aarokacra, Pseudodragon, Pteranodon, Swarm of Bats, Winged Kobold, Derro, '
                    'Kobold Inventor, Star Spawn Grue', 'CR': '50XP, 1/4'},
        4: {'Name': 'Giant Goat, Orc, Scout, Firenewt Warrior', 'CR': '100XP, 1/2'},
        5: {'Name': 'Giant Eagle, Half-Ogre, Harpy, Hippogriff, Lion, Clockwork Bronze Scout, Choker, Duergar, Soulblade, '
                    'Firenewt Warlock of Imix, Giant Strider, Kobold Dragonshield, Kobold Scale Sorcerer, Meazel, '
                    'Stone Cursed', 'CR': '200XP, 1'},
        6: {'Name': 'Berserker, Druid, Giant Elk, Griffon, Ogre, Orc Eye of Gruumsh, Orog, Peryton, Saber-Toothed Tiger, '
                    'Adult Kruthik, Aurochs, Duergar Hammerer, Duergar Kavalrachni, Duergar Mind Master, '
                    'Duergar Stone Guard, Duergar Xarrorn, Guard Drake, Ogre Bolt Launcher, Ogre Howdah, Quetzalcoatlus',
            'CR': '450XP, 2'},
        7: {'Name': 'Basilisk, Hell Hound, Manticore, Veteran, Duergar Screamer, Ogre Chain Brute, Vampiric Mist',
            'CR': '700XP, 3'},
        8: {'Name': 'Ettin, Barghest, Clockwork Iron Cobra, Clockwork Stone Defender, Ogre Battering Ram, '
                    'Warlock of the Archfey', 'CR': '1100XP, 4'},
        9: {'Name': 'Air Elemental, Bulette, Troll, Clockwork Oaken Bolter, Kruthik Hive Lord, Tanarukk',
            'CR': '1800XP, 5'},
        10: {'Name': 'Chimera, Cyclops, Galeb Duhr, Wyvern, Annis Hag, Duergar Warlord, Warlock of the Great Old One',
             'CR': '2300XP, 6'},
        11: {'Name': 'Stone Giant, Lost Sorrwsworn', 'CR': '2900XP, 7'},
        12: {'Name': 'Frost Giant', 'CR': '3900XP, 8'},
        13: {'Name': 'Cloud Giant, Fire Giant, Young Silver Dragon, Lonely Sorrowsworn', 'CR': '5000XP, 9'},
        14: {'Name': 'Young Red Dragon, Githyanki Gish, Githzerai Enlightened, Stone Giant Dreamwalker',
             'CR': '5900XP, 10'},
        15: {'Name': 'Roc, Balhannoth, Cloud Giant Smiling Once', 'CR': '7200XP, 11'},
        16: {'Name': 'Archdruid, Duergar Despot, Eidolon, Githyanki Kith-rak, Ki-Rin', 'CR': '8400XP, 12'},
        17: {'Name': 'Dire Troll, Star Spawn Seer', 'CR': '10000XP, 13'},
        18: {'Name': 'Fire Giant Dreadnought, Githyanki Supreme Commander', 'CR': '11500XP, 14'},
        19: {'Name': 'Adult Silver Dragon, Phoenix, Star Spawn Larva Mage, Storm Giant Quintessent', 'CR': '15000XP, 16'},
        20: {'Name': 'Adult Red Dragon', 'CR': '18000XP, 17'},
        21: {'Name': 'Red Abishai', 'CR': '22000XP, 19'},
        22: {'Name': 'Zaratan', 'CR': '41000XP, 22'},
        23: {'Name': 'Ancient Silver Dragon, Elder Tempest', 'CR': '50000XP, 23'},
        24: {'Name': 'Ancient Red Dragon', 'CR': '62000XP, 24'},
    },
    'swamp': {
        1: {'Name': 'Rat, Raven', 'CR': '10XP, 0'},
        2: {'Name': 'Giant Rat, Kobold, Poisonous Snake, Stirge, Tribal Warrior', 'CR': '25XP, 1/8'},
        3: {'Name': 'Bullywug, Constrictor Snake, Giant Frog, Giant Lizard, Giant Poisonous Snake, Mud Mephit,'
                    'Swarm of Rats, Swarm of Ravens, Winged Kobold, Dimetrodon, Hadrosaurus, Oblex Spawn, '
                    'Star Spawn Grue, Vegepygmy, Wretched Sorrwsworn', 'CR': '50XP, 1/4'},
        4: {'Name': 'Crocodile, Lizardfolk, Orc, Scout, Swarm of Insects, Darkling, Skulk, Swarm of Rot Grubs',
            'CR': '100XP, 1/2'},
        5: {'Name': 'Ghoul, Giant Spider, Giant Toad, Yuan-ti Pureblood, Meazel, Vargouille, Thorny Vegepygmy',
            'CR': '200XP, 1'},
        6: {'Name': 'Druid, Ghast, Giant Constrictor Snake, Lizardfolk Shaman, Ogre, Orc Eye of Gruumsh,'
                    'Swarm of Poisonous Sankes, Will-o-Wisp, Darkling Elder, Guard Drake, Meenlock, Shadow Mastiff, '
                    'Vegepygmy Chief', 'CR': '450XP, 2'},
        7: {'Name': 'Green Hag, Wight, Yuan-ti Malison, Flail Snail, Redcap, Shadow Mastiff Alpha, Sword Waith Warrior, '
                    'Vampiric Mist', 'CR': '700XP, 3'},
        8: {'Name': 'Warlock of the Archfey', 'CR': '1100XP, 4'},
        9: {'Name': 'Giant Crocodile, Revenant, Shambling Mound, Troll, Water Elemental, Adult Oblex, Allip, Catoblepas',
            'CR': '1800XP, 5'},
        10: {'Name': 'Bodak', 'CR': '2300XP, 6'},
        11: {'Name': 'Young Black Dragon, Yuan-ti Abomination, Lost Sorrowsworn, Maurezhi, Venom Troll', 'CR': '2900XP, 7'},
        12: {'Name': 'Hydra, Corpse Flower', 'CR': '3900XP, 8'},
        13: {'Name': 'Rot Troll', 'CR': '5000XP, 9'},
        14: {'Name': 'Elder Oblex, Froghemoth, Sword Wraith Commander', 'CR': '5900XP, 10'},
        15: {'Name': 'Spirit Troll', 'CR': '7200XP, 11'},
        16: {'Name': 'Archdruid', 'CR': '8400XP, 12'},
        17: {'Name': 'Star Spawn Seer, Wastrilith', 'CR': '10000XP, 13'},
        18: {'Name': 'Adult Black Dragon', 'CR': '11500XP, 14'},
        19: {'Name': 'Nabassu, Skull Lord', 'CR': '13000XP, 15'},
        20: {'Name': 'Nagpa', 'CR': '18000XP, 17'},
        21: {'Name': 'Nightwalker', 'CR': '25000XP, 20'},
        22: {'Name': 'Ancient Black Dragon', 'CR': '33000XP, 21'},
    },
    'underdark': {
        1: {'Name': 'Giant Fire Beetle, Shrieker, Myconid Sprout, Cranium Rat', 'CR': '10XP, 0'},
        2: {'Name': 'Flumph, Giant Rat, Kobold, Stirge, Tribal Warrior, Boggle, Neogi Hatchling, Xvart, Young Kruthik',
            'CR': '25XP, 1/8'},
        3: {'Name': 'Drow, Giant Bat, Giant Centipede, Giant Lizard, Giant Poisonous Snake, Goblin, Girmlock, Kuo-Toa, '
                    'Swarm of Bats, Troglodyte, Violet Fungus, Winged Kobold, Deep Rothe, Derro, Kobold Inventor, '
                    'Males Steeder, Oblex Spawn, Wretched Sorrwsworn', 'CR': '50XP, 1/4'},
        4: {'Name': 'Darkmantle, Deep Gnome, Gas Spore, Gray Ooze, Hobgoblin, Magma Mephit, Myconid Adult, Orc,'
                    'Piercer, Rust Monster, Scout, Shadow, Swarm of Insects, Chitine, Darkling, Firenewt Warrior, Gazer, '
                    'Skulk Swarm of Rot Grubs', 'CR': '100XP, 1/2'},
        5: {'Name': 'Bugbear, Duergar, Fire Snake, Ghoul, Giant Spider, Giant Toad, Goblin Boss, Half-Ogre, Kuo-Toa Whip, '
                    'Quaggoth Spore Servant, Specter, Choker, Duergar Soulblade, Female Steeder, firenewt Warlock of '
                    'Imix, Giant Strider, Kobold Dragonshield, Kobold Scale Sorcerer, Maw Demon, Meazel, Nilbog, '
                    'Vargouille, Xvart Warlock of Raxivort', 'CR': '200XP, 1'},
        6: {'Name': 'Carrion Crawler, Druid, Gargoyle, Gelatinous Cube, Ghast, Giant Constrictor Snake, '
                    'Gibbering Mouther, Girck, Intellect Devourer, Mimic, Minotaur Skeleton, Nothic, Ochre Jelly, '
                    'Ogre, Orc Eye of Gruumsh, Orog, Polar Bear (Cave Bear), Quaggoth, Adult Kruthik, Darkling Elder, '
                    'Duergar Hammerer, Duergar Kavalrachni, Duergar Mind Master, Duergar Stone Guard, Duergar Xarrorn, '
                    'Guard Drake, Yuan-Ti Broodguard', 'CR': '450XP, 2'},
        7: {'Name': 'Doppleganger, Grell, Hobgoblin, Captain, Hell Hound, Hook Horror, Kuo-Toa Monitor, Minotaur, '
                    'Quaggoth Thonot, Phase Spider, Spectator, Veteran, Water Weird, Wight, Cave Fisher, Choldrith, '
                    'Derro Savant, Duergar Screamer, Flail Snail, Neogi, Slithering Tracker, Trapper, Vampiric Mist',
            'CR': '700XP, 3'},
        8: {'Name': 'Black Pudding, Bone Naga, Chuul, Ettin, Flameskull, Ghost, Babau, Barghest, Neogi Master, '
                    'Yuan-ti Mind Whisperer, Yuan-ti Nightmare Speaker', 'CR': '1100XP, 4'},
        9: {'Name': 'Beholder Zombie, Drow Elite Warrior, Earth Elemental, Otyugh, Roper, Salamander, Troll, Umber Hulk, '
                    'Vampire Spawn, Wraith, Xorn, Adult Oblex, Kruthik Hive Lord, Mindwitness, Spawn of Kyuss, '
                    'Swarm of Cranium Rats, Tanarukk, Yuan-ti Pit Master', 'CR': '1800XP, 5'},
        10: {'Name': 'Chimera, Cyclops, Drider, Bodak, Duergar Warlord, Gauth, Warlock of the Great Old One',
             'CR': '2300XP, 6'},
        11: {'Name': 'Drow Mage, Grick Alpha, Mind Flayer, Stone Giant, Armanite, Dhergoloth, Draegloth, Lost Sorrowsworn, '
                     'Shadar-kai Shadow Dancer, Venom Troll, Warlock of the Fiend', 'CR': '2900XP, 7'},
        12: {'Name': 'Cloaker, Fomorian, Mind Flayer Arcanist, Spirit Naga, Blackguard, Canoloth, Howler',
             'CR': '3900XP, 8'},
        13: {'Name': 'Fire Giant, Drow House Captain, Shadar-Kai Gloom Weaver, Lonely Sorrowsworn, Rot Troll, Ulitharid',
             'CR': '5000XP, 9'},
        14: {'Name': 'Aboleth, Alhoon, Death Kiss, Elder Oblex, Froghemoth, Orthon', 'CR': '5900XP, 10'},
        15: {'Name': 'Behir, Dao, Alkilith, Balhannoth, Drow Shadowblade, Hungry Sorrowsworn, Shadar-Kai Soul Monger, '
                     'Spirit Troll', 'CR': '7200XP, 11'},
        16: {'Name': 'Duergar Despot, Oinoloth, Yuan-ti Anathema', 'CR': '8400XP, 12'},
        17: {'Name': 'Beholder, Young Red Shadow Dragon, Angry Sorrowsworn, Devourer, Dire Troll, Drow Arachnomancer, '
                     'Neothelid, Wastrilith', 'CR': '10000XP, 13'},
        18: {'Name': 'Death Tyrant, Drow Inquisitor, Elder Brain, Fire Giant Dreadnought, Retriever', 'CR': '11500XP, 14'},
        19: {'Name': 'Purple Worm, Nabassu, Skull Lord', 'CR': '13000XP, 15'},
        20: {'Name': 'Nagpa', 'CR': '18000XP, 17'},
        21: {'Name': 'Drow Favored Consort, Sibriex', 'CR': '20000XP, 18'},
        22: {'Name': 'Drow Matron Mother, Nightwalker', 'CR': '25000XP, 20'},
        23: {'Name': 'Zaratan', 'CR': '41000XP, 22'},
    },
    'underwater': {
        1: {'Name': 'Quipper', 'CR': '10XP, 0'},
        2: {'Name': 'Merfolk, Dolphin', 'CR': '25XP, 1/8'},
        3: {'Name': 'Constrictor Snake, Steam Mephit', 'CR': '50XP, 1/4'},
        4: {'Name': 'Giant Sea Horse, Reef Shark, Sahuagin', 'CR': '100XP, 1/2'},
        5: {'Name': 'Giant Octopus, Swarm of Quippers, Sea Spawn', 'CR': '200XP, 1'},
        6: {'Name': 'Giant Constrictor Snake, Hunter Shark, Merrow, Plesiosaurus, Sahuagin Priestess, Sea Hag', 'CR':
            '450XP, 2'},
        7: {'Name': 'Killer Whale, Deep Scion, Dolphin Delighter', 'CR': '700XP, 3'},
        8: {'Name': 'Giant Shark, Sahuagin Baron, Water Elemental, Kraken Priest', 'CR': '1800XP, 5'},
        9: {'Name': 'Marid, Morkoth', 'CR': '7200XP, 11'},
        10: {'Name': 'Archdruid', 'CR': '8400XP, 12'},
        11: {'Name': 'Storm Giant, Wastrilith', 'CR': '10000XP, 13'},
        12: {'Name': 'Storm Giant Quintessent', 'CR': '15000XP, 16'},
        13: {'Name': 'Dragon Turtle', 'CR': '18000XP, 17'},
        14: {'Name': 'Leviathan', 'CR': '25000XP, 20'},
        15: {'Name': 'Kraken', 'CR': '50000XP, 23'},
    },
    'urban': {
        1: {'Name': 'Cat, Commoner, Goat, Rat, Raven, Cranium Rat', 'CR': '10XP, 0'},
        2: {'Name': 'Bandit, Cultist, Flying Snake, Giant Rat, Guard, Kobold, Mastiff, Mule, Noble, Pony, Stirge, Boggle',
            'CR': '25XP, 1/8'},
        3: {'Name': 'Acolyte, Draft Horse, Giant Centipede, Giant Poisonous Snake, Kenku, Pseudodragon, Riding Horse, '
                    'Skeleton, Smoke Mephit, Swarm of Bats, Swarm of Rats, Swarm of Ravens, Winged Kobold, Zombie, '
                    'Apprentice Wizard, Kobold Inventor, Oblex Spawn, Ox, Wretched Sorrowsworn', 'CR': '50XP, 1/4'},
        4: {'Name': 'Crocodile, Giant Wasp, Shadow, Swarm of Insects, Thug, Warhorse, Darkling, Skulk, Stench Kow',
            'CR': '100XP, 1/2'},
        5: {'Name': 'Ghoul, Giant Spider, Half-Ogre, Specter, Spy, Yuan-ti Pureblood, Kobold Scale Sorcerer, '
                    'Meazel, Stone Cursed', 'CR': '200XP, 1'},
        6: {'Name': 'Bandit Captain, Cult Fanatic, Gargoyle, Ghast, Mimic, Priest, Wererat, Will-o-Wasp, Bard, '
                    'Darkling Elder, Guard Drake, Meenlock', 'CR': '450XP, 2'},
        7: {'Name': 'Doppelganger, Knight, Phase Spider, Veteran, Water Weird, Wight, Archer, Giff, Illusionist Wizard, '
                    'Martial Arts Adept, Slithering Tracker, Swashbuckler, Vampiric Mist', 'CR': '700XP, 3'},
        8: {'Name': 'Couatl, Ghost, Succubus or Incubus, Babau, Deathlock, Dybbuk, Warlock of the Archfey',
            'CR': '1100XP, 4'},
        9: {'Name': 'Cambion, Gladiator, Revenant, Vampire Spawn, Adult Oblex, Allip, Banderhobb, Enchanter Wizard, '
                    'Master Thief, Swarm of Cranium Rats, Transmuter Wizard', 'CR': '1800XP, 5'},
        10: {'Name': 'Invisible Stalker, Mage, Bodak, Conjurer Wizard, Warlock of the Great Old One, White Abishai',
             'CR': '2300XP, 6'},
        11: {'Name': 'Oni, Shield Guardian, Black Abishai, Lost Sorrowsworn, Maurezhi, Shadar-Kai Dancer, '
                     'Warlock of the Fiend', 'CR': '2900XP, 7'},
        12: {'Name': 'Assassin, Blackguard, Canoloth, Corpse Flower, Deathlock Mastermind, Diviner Wizard',
             'CR': '3900XP, 8'},
        13: {'Name': 'Gray Sladd, Young Silver Dragon, Abjurer Wizard, Champion, Evoker Wizard, Lonely Sorrowsworn, '
                     'Necromancer Wizard, Shadar-Kai Gloom Weaver, War Priest', 'CR': '5000XP, 9'},
        14: {'Name': 'Elder Oblex, Githyanki Gish, Githzerai Enlightened, Orthon', 'CR': '5900XP, 10'},
        15: {'Name': 'Alkilith, Hungry Sorrowsworn, Shadar-Kai Soul Monger, Yagnoloth', 'CR': '7200XP, 11'},
        16: {'Name': 'Archmage, Boneclaw, Eidolon, Githyanki Kith-rak, Warlord', 'CR': '8400XP, 12'},
        17: {'Name': 'Rakshasa, Vampire, Angry Sorrowsworn, Star Spawn Seer', 'CR': '10000XP, 13'},
        18: {'Name': 'Githyanki Supreme Commander', 'CR': '11500XP, 14'},
        19: {'Name': 'Spellcaster or Warrior Vampire, Green Abishai, Nabassu', 'CR': '13000XP, 15'},
        20: {'Name': 'Adult Silver Dragon, Steel Predator', 'CR': '15000XP, 16'},
        21: {'Name': 'Blue Abishai, Nagpa', 'CR': '18000XP, 17'},
        22: {'Name': 'Red Abishai', 'CR': '22000XP, 19'},
        23: {'Name': 'Ancient Silver Dragon', 'CR': '50000XP, 23'},
        24: {'Name': 'Tarrasque', 'CR': '155000XP'},
    }
}

# test = monsters_category.get('artic')[1]['CR'].split(','[0])
# print(test[0].split('XP')[0])
# test = urban[1]['CR'].split(',')[0]
# print(urban[1]['CR'].split(',')[0])
# print()
# print(test.split('XP')[0])

# for x in artic:
#     print(artic[x])

