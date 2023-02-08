"""
Will create a list of Monsters and the CR state along with Page Numbers
May contain initial stats as well along with Initiative rolls (Dex Stats)

CR to XP
0 - 10XP
1/8 - 25XP
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

artic = {
    1: {'Name': 'Commoner, Owl', 'CR': '10XP'},
    2: {'Name': 'Bandit, Blood Hawk, Kobold, Tribal Warrior', 'CR': '25XP'},
    3: {'Name': 'Giant Owl, Winged Kobold', 'CR': '50XP'},
    4: {'Name': 'Ice Mephit, Orc, Scout', 'CR': '100XP'},
    5: {'Name': 'Brown Bear, Half-Ogre', 'CR': '200XP'},
    6: {'Name': 'Bandit Captain, Berserker, Druid, Griffon, Ogre, Orce Ey of Gruumsh, Orog, Polar Bear, '
                'Saber-Toothed Tiger', 'CR': '450XP'},
    7: {'Name': 'Manitcore, Veteran, Winter Wolf, Yeti', 'CR': '700XP'},
    8: {'Name': 'Revenant, Troll, Werebear, Young Remorhaz', 'CR': '1800XP'},
    9: {'Name': 'Mammoth, Young White Dragon', 'CR': '2300XP'},
    10: {'Name': 'Frost Giant', 'CR': '3900XP'},
    11: {'Name': 'Abominable Yeti', 'CR': '5000XP'},
    12: {'Name': 'Remorhaz, Roc', 'CR': '7200XP'},
    13: {'Name': 'Adult White Dragon', 'CR': '10000XP'},
    14: {'Name': 'Ancient White Dragon', 'CR': '25000XP'}
}

coastal = {
    1: {'Name': 'Commoner, Crab, Eagle', 'CR': '10XP'},
    2: {'Name': 'Bandit, Blood Hawk, Giant Crab, Guard, Kobold, Merfolk, Poisonous Snake, Stirge, '
                'Tribal Warrior', 'CR': '25XP'},
    3: {'Name': 'Giant Lizard, Giant Wolf Spider, Pseudodragon, Pteranodon, Winged Kobold', 'CR': '50XP'},
    4: {'Name': 'Sahuagin, Scout', 'CR': '100XP'},
    5: {'Name': 'Giant Eagel, Giant Toad, Harpy', 'CR': 'XP'},
    6: {'Name': 'Bandit Captain, Berserker, Druid, Griffon, Ogre, Merrow, Plesiosaurus, Sahuagin Priestess,'
                'Sea Hag', 'CR': '450XP'},
    7: {'Name': 'Manticore, Veteran', 'CR': '700XP'},
    8: {'Name': 'Banshee', 'CR': '1100XP'},
    9: {'Name': 'Sahuagin Baron, Water Elemental', 'CR': '1800XP'},
    10: {'Name': 'Cyclops', 'CR': '2300XP'},
    11: {'Name': 'Young Bronze Dragon', 'CR': '3900XP'},
    12: {'Name': 'Young Blue Dragon', 'CR': '5000XP'},
    13: {'Name': 'Djinni, Marid, Roc', 'CR': '7200XP'},
    14: {'Name': 'Storm Giant', 'CR': '10000XP'},
    15: {'Name': 'Adult Bronze Dragon', 'CR': '13000XP'},
    16: {'Name': 'Adult Blue Dragon', 'CR': '15000XP'},
    17: {'Name': 'Dragon Turtle', 'CR': '18000XP'},
    18: {'Name': 'Ancient Bronze Dragon', 'CR': '41000XP'},
    19: {'Name': 'Ancient Blue Dragon', 'CR': '50000XP'},
}

desert = {
    1: {'Name': 'Cat, Commoner, Hyena, Jackal, Scorpion, Vulture', 'CR': '10XP'},
    2: {'Name': 'Bandit, Camel, Flying Snake, Guard, Kobold, Mule, Poisonous Snake, Stirge,'
                'Tribal Warrior', 'CR': '25XP'},
    3: {'Name': 'Constrictor Snake, Giant Lizard, Giant Poisonous Snake, Giant Wolf Spider, Pseudodragon, Winged Kobold'
        , 'CR': '50XP'},
    4: {'Name': 'Dust Mephit, Gnoll, Hobgoblin, Jackalwere, Scout, Swarm of Insects', 'CR': '100XP'},
    5: {'Name': 'Death Dog, Giant Hyena, Giant Spider, Giant Toad, Giant Vulture, Half-Ogre, Lion,'
                'Thri-kreen, Yuan-ti Pureblood', 'CR': '200XP'},
    6: {'Name': 'Bandit Captain, Berserker, Druid, Giant Constrictor, Snake, Gnoll Pack Lord, Ogre', 'CR': '450XP'},
    7: {'Name': 'Giant Scorpion, Hobgoblin Captain, Mummy, Phase Spider, Wight, Yuan-ti Malison', 'CR': '700XP'},
    8: {'Name': 'Couatl, Gnoll Fang of Yeenoghu, Lamia, Weretiger', 'CR': '1100XP'},
    9: {'Name': 'Air Elemental, Fire Elemental, Revenant', 'CR': '1800XP'},
    10: {'Name': 'Cyclops, Medusa, Young Brass Dragon', 'CR': '2300XP'},
    11: {'Name': 'Yuan-ti Abomination', 'CR': '2900XP'},
    12: {'Name': 'Young Blue Dragon', 'CR': '5000XP'},
    13: {'Name': 'Guardian Naga', 'CR': '5900XP'},
    14: {'Name': 'Efreeti, Gynosphinx, Roc', 'CR': '7200XP'},
    15: {'Name': 'Adult Brass Dragon', 'CR': '10000XP'},
    16: {'Name': 'Mummy Lord, Purple Worm', 'CR': '13000XP'},
    17: {'Name': 'Adult Blue Dragon', 'CR': '15000XP'},
    18: {'Name': 'Adult Blue Dracolish, Androsphinx', 'CR': '18000XP'},
    19: {'Name': 'Ancient Brass Dragon', 'CR': '25000XP'},
    20: {'Name': 'Ancient Blue Dragon', 'CR': '50000XP'},
}

forest = {
    1: {'Name': 'Awakened Shrub, Baboon, Badger, Cat, Commoner, Deer, Hyena, Owl', 'CR': '10XP'},
    2: {'Name': 'Bandit, Blood Hawk, Flying Snake, Giant Rat, Giant Weasel, Guard, Kobold, Mastiff, Poisonous Snake,'
                'Stirge, Tribal Warrior, Twig Blight', 'CR': '25XP'},
    3: {'Name': 'Blink Dog, Boar, Constrictor Snake, Elk, Giant Badger, Giant Bat, Giant Frog, Giant Lizard, Giant Owl,'
                'Giant Poisonous Snake, Giant Wolf Spider, Gobline, Kenku, Needle Blight, Panther, Pixie,'
                'Pseudodragon, Sprite, Swarm of Ravens, Winged Kobold, Wolf', 'CR': '50XP'},
    4: {'Name': 'Ape, Black Bear, Giant Wasp, Gnoll, Hobgoblin, Lizardfolk, Ord, Satyr, Scout, Swarm of Insects, '
                'Vine Blight, Worg', 'CR': '100XP'},
    5: {'Name': 'Brown Bear, Bugbear, Dire Wolf, Dryad, Faerie Dragon (Yellow or Younger), Giant Hyena,'
                'Giant Spider, Giant Toad, Goblin Boss, Half-Ogre, Harpy, Tiger, Yuan-ti Pureblood', 'CR': '200XP'},
    6: {'Name': 'Ankheg, Awakened Tree, Bandit Captain, Berserker, Centaur, Druid, Ettercap, Faerie Dragon '
                '(Green or Older), Giant Boar, Giant Constrictor Snake, Giant Elk, Gnoll Pack Lord, Grick,'
                'Lizardfolk Shaman, Ogre, Orc, Eye of Gruumsh, Orog, Pegasus, Swarm of Poisonous Snakes,'
                'Wererat, Will-o-Wisp', 'CR': '450XP'},
    7: {'Name': 'Displacer Beast, Green Hag, Hobgoblin Captain, Owlbear, Phase Spider, Veteran, Werewolf, '
                'Yuan-ti Malison', 'CR': '700XP'},
    8: {'Name': 'Banshee, Couatl, Gnoll Fang of Yeenoghu, Wereboar, Weretiger', 'CR': '1100XP'},
    9: {'Name': 'Gogon, Revenant, Shambling Mound, Troll, Unicorn, Werebear', 'CR': '1800XP'},
    10: {'Name': 'Giant Ape, Grick Alpha, Oni, Yuan-ti Abomination', 'CR': '2900XP'},
    11: {'Name': 'Young Green Dragon', 'CR': '3900XP'},
    12: {'Name': 'Treant', 'CR': '5000XP'},
    13: {'Name': 'Guardian Naga, Young Gold Dragon', 'CR': '5900XP'},
    14: {'Name': 'Adult Green Dragon', 'CR': '13000XP'},
    15: {'Name': 'Adult Gold Dragon', 'CR': '18000XP'},
    16: {'Name': 'Ancient Green Dragon', 'CR': '41000XP'},
    17: {'Name': 'Ancient Gold Dragon', 'CR': '62000XP'},
}

grassland = {
    1: {'Name': 'Cat, Commoner, Deer, Eagle, Goat, Hyena, Jackal, Vulture', 'CR': '10XP'},
    2: {'Name': 'Blood Hawk, Flying Snake, Giant Weasel, Guard, Poisonous Snake, Stirge, Tribal Warrior', 'CR': '25XP'},
    3: {'Name': 'Axe Beak, Boar, Elk, Giant Poisonous Snake, Giant Wolf Spider, Goblin, Panther (Leopard),'
                'Pteranodon, Riding Horse, Wolf', 'CR': '50XP'},
    4: {'Name': 'Cockatrice, Giant Goat, Giant Wasp, Gnoll, Hobgoblin, Jackalwere, Orc, Scout, Swarm of Insects,'
                'Worg', 'CR': '100XP'},
    5: {'Name': 'Bugbear, Giant Eagle, Giant Hyena, Giant Vulture, Goblin Boss, Hippogriff, Lion, Scarecrow, '
                'Thri-Kreen, Tiger', 'CR': '200XP'},
    6: {'Name': 'Allosaurus, Ankheg, Centaur, Druid, Giant Boar, Giant Elk, Gnoll Pack Lord, Griffon, Ogre, '
                'Orc Eye of Gruumsh, Orog, Pegasus, Rhinoceros', 'CR': '450XP'},
    7: {'Name': 'Ankylosaurus, Hobgoblin Captain, Manticore, Phase Spider, Veteran', 'CR': '700XP'},
    8: {'Name': 'Coutl, Elephant, Gnoll Fang of Yeenoghu, Wereboar, Weretiger', 'CR': '1100XP'},
    9: {'Name': 'Bulette, Gorgon, Triceratops', 'CR': '1800XP'},
    10: {'Name': 'Chimera, Cyclops', 'CR': '2300XP'},
    11: {'Name': 'Tyrannosaurus Rex', 'CR': '3900XP'},
    12: {'Name': 'Young Gold Dragon', 'CR': '5900XP'},
    13: {'Name': 'Adult Gold Dragon', 'CR': '18000XP'},
    14: {'Name': 'Ancient Gold Dragon', 'CR': '62000XP'},
}

hill = {
    1: {'Name': 'Baboon, Commoner, Eagle, Goat, Hyena, Raven, Vulture', 'CR': '10XP'},
    2: {'Name': 'Bandit, Blood Hawk, Giant Weasel, Guard, Kobold, Mastiff, Mule, Poisonous Snake, Stirge,'
                'Tribal Warrior', 'CR': '25XP'},
    3: {'Name': 'Axe Beak, Boar, Elk, Giant Owl, Giant Wolf Spider, Goblin, Panther (Cougar), Pseudodragon,'
                'Swarm of Bats, Swarm of Ravens, Winged Kobold, Wolf', 'CR': '50XP'},
    4: {'Name': 'Giant Goat, Gnoll, Hobgoblin, Orc, Scout, Swarm of Insects, Worg', 'CR': '100XP'},
    5: {'Name': 'Brown Bear, Dire Wolf, Giant Eagle, Giant Hyena, Goblin Boss, Half-Ogre, Garpy, Hippogriff,'
                'Lion', 'CR': '200XP'},
    6: {'Name': 'Bandit Captain, Berserker, Druid, Giant Boar, Giant Elk, Gnoll Pack Lord, Griffon, Orge, '
                'Orc Eye of Gruumsh, Orog, Pegasus, Peryton', 'CR': '450XP'},
    7: {'Name': 'Green Hag, Hobgoblin Captain, Manticore, Phase Spider, Veteran, Werewolf', 'CR': '700XP'},
    8: {'Name': 'Ettin, Gnoll Fang of Yeenoghu, Wereboar', 'CR': '1100XP'},
    9: {'Name': 'Bulette, Gorgon, Hill Giant, Revenant, Troll, Werebear', 'CR': '1800XP'},
    10: {'Name': 'Chimera, Cyclops, Galeb Duhr, Wyvern', 'CR': '2300XP'},
    11: {'Name': 'Stone Giant, Young Copper Dragon', 'CR': '2900XP'},
    12: {'Name': 'Young Red Dragon', 'CR': '5900XP'},
    13: {'Name': 'Roc', 'CR': '7200XP'},
    14: {'Name': 'Adult Copper Dragon', 'CR': '11500XP'},
    15: {'Name': 'Adult Red Dragon', 'CR': '18000XP'},
    16: {'Name': 'Ancient Copper Dragon', 'CR': '33000XP'},
    17: {'Name': 'Ancient Red Dragon', 'CR': '62000XP'},
}

mountain = {
    1: {'Name': 'Eagle, Goat', 'CR': '10XP'},
    2: {'Name': 'Blood Hawk, Guard, Kobold, Stirge, Tribal Warrior', 'CR': '25XP'},
    3: {'Name': 'Aarokacra, Pseudodragon, Pteranodon, Swarm of Bats, Winged Kobold', 'CR': '50XP'},
    4: {'Name': 'Giant Goat, Orc, Scout', 'CR': '100XP'},
    5: {'Name': 'Giant Eagle, Half-Ogre, Harpy, Hippogriff, Lion', 'CR': '200XP'},
    6: {'Name': 'Berserker, Druid, Giant Elk, Griffon, Ogre, Orc Eye of Gruumsh, Orog, Peryton, Saber-Toothed Tiger',
        'CR': '450XP'},
    7: {'Name': 'Basilisk, Hell Hound, Manticore, Veteran', 'CR': '700XP'},
    8: {'Name': 'Ettin', 'CR': '1100XP'},
    9: {'Name': 'Air Elemental, Bulette, Troll', 'CR': '1800XP'},
    10: {'Name': 'Chimera, Cyclops, Galeb Duhr, Wyvern', 'CR': '2300XP'},
    11: {'Name': 'Stone Giant', 'CR': '2900XP'},
    12: {'Name': 'Frost Giant', 'CR': '3900XP'},
    13: {'Name': 'Cloud Giant, Fire Giant, Young Silver Dragon', 'CR': '5000XP'},
    14: {'Name': 'Young Red Dragon', 'CR': '5900XP'},
    15: {'Name': 'Roc', 'CR': '7200XP'},
    16: {'Name': 'Adult Silver Dragon', 'CR': '15000XP'},
    17: {'Name': 'Adult Red Dragon', 'CR': '18000XP'},
    18: {'Name': 'Ancient Silver Dragon', 'CR': '50000XP'},
    19: {'Name': 'Ancient Red Dragon', 'CR': '62000XP'},
}

swamp = {
    1: {'Name': 'Rat, Raven', 'CR': '10XP'},
    2: {'Name': 'Giant Rat, Kobold, Poisonous Snake, Stirge, Tribal Warrior', 'CR': '25XP'},
    3: {'Name': 'Bullywug, Constrictor Snake, Giant Frog, Giant Lizard, Giant Poisonous Snake, Mud Mephit,'
                'Swarm of Rats, Swarm of Ravens, Winged Kobold', 'CR': '50XP'},
    4: {'Name': 'Crocodile, Lizardfolk, Orc, Scout, Swarm of Insects', 'CR': '100XP'},
    5: {'Name': 'Ghoul, Giant Spider, Giant Toad, Yuan-ti Pureblood', 'CR': '200XP'},
    6: {'Name': 'Druid, Ghast, Giant Constrictor Snake, Lizardfolk Shaman, Ogre, Orc Eye of Gruumsh,'
                'Swarm of Poisonous Sankes, Will-o-Wisp', 'CR': '450XP'},
    7: {'Name': 'Green Hag, Wight, Yuan-ti Malison', 'CR': '700XP'},
    8: {'Name': 'Giant Crocodile, Revenant, Shambling Mound, Troll, Water Elemental', 'CR': '1800XP'},
    9: {'Name': 'Young Black Dragon, Yuan-ti Abomination', 'CR': '2900XP'},
    10: {'Name': 'Hydra', 'CR': '3900XP'},
    11: {'Name': 'Adult Black Dragon', 'CR': '11500XP'},
    12: {'Name': 'Ancient Black Dragon', 'CR': '33000XP'},
}

underdark = {
    1: {'Name': 'Giant Fire Beetle, Shrieker, Myconid Sprout', 'CR': '10XP'},
    2: {'Name': 'Flumph, Giant Rat, Kobold, Stirge, Tribal Warrior', 'CR': '25XP'},
    3: {'Name': 'Drow, Giant Bat, Giant Centipede, Giant Lizard, Giant Poisonous Snake, Goblin, Girmlock, Kuo-Toa, '
                'Swarm of Bats, Troglodyte, Violet Fungus, Winged Kobold', 'CR': '50XP'},
    4: {'Name': 'Darkmantle, Deep Gnome, Gas Spore, Gray Ooze, Hobgoblin, Magma Mephit, Myconid Adult, Orc,'
                'Piercer, Rust Monster, Scout, Shadow, Swarm of Insects', 'CR': '100XP'},
    5: {'Name': 'Bugbear, Duergar, Fire Snake, Ghoul, Giant Spider, Giant Toad, Goblin Boss, Half-Ogre, Kuo-Toa Whip, '
                'Quaggoth Spore Servant, Specter', 'CR': '200XP'},
    6: {'Name': 'Carrion Crawler, Druid, Gargoyle, Gelatinous Cube, Ghast, Giant Constrictor Snake, '
                'Gibbering Mouther, Girck, Intellect Devourer, Mimic, Minotaur Skeleton, Nothic, Ochre Jelly, '
                'Ogre, Orc Eye of Gruumsh, Orog, Polar Bear (Cave Bear), Quaggoth', 'CR': '450XP'},
    7: {'Name': 'Doppleganger, Grell, Hobgoblin, Captain, Hell Hound, Hook Horror, Kuo-Toa Monitor, Minotaur, ' 
                'Quaggoth Thonot, Phase Spider, Spectator, Veteran, Water Weird, Wight', 'CR': '700XP'},
    8: {'Name': 'Black Pudding, Bone Naga, Chuul, Ettin, Flameskull, Ghost', 'CR': '1100XP'},
    9: {'Name': 'Beholder Zombie, Drow Elite Warrior, Earth Elemental, Otyugh, Roper, Salamander, Troll, Umber Hulk, '
                'Vampire Spawn, Wraith, Xorn', 'CR': '1800XP'},
    10: {'Name': 'Chimera, Cyclops, Drider', 'CR': '2300XP'},
    11: {'Name': 'Drow Mage, Grick Alpha, Mind Flayer, Stone Giant', 'CR': '2900XP'},
    12: {'Name': 'Cloaker, Fomorian, Mind Flayer Arcanist, Spirit Naga', 'CR': '3900XP'},
    13: {'Name': 'Fire Giant', 'CR': '5000XP'},
    14: {'Name': 'Aboleth', 'CR': '5900XP'},
    15: {'Name': 'Behir, Dao', 'CR': '7200XP'},
    16: {'Name': 'Beholder, Young Red Shadow Dragon', 'CR': '10000XP'},
    17: {'Name': 'Death Tyrant', 'CR': '11500XP'},
    18: {'Name': 'Purple Worm', 'CR': '13000XP'},
}

underwater = {
    1: {'Name': 'Quipper', 'CR': '10XP'},
    2: {'Name': 'Merfolk', 'CR': '25XP'},
    3: {'Name': 'Constrictor Snake, Steam Mephit', 'CR': '50XP'},
    4: {'Name': 'Giant Sea Horse, Reef Shark, Sahuagin', 'CR': '100XP'},
    5: {'Name': 'Giant Octopus, Swarm of Quippers', 'CR': '200XP'},
    6: {'Name': 'Giant Constrictor Snake, Hunter Shark, Merrow, Plesiosaurus, Sahuagin Priestess, Sea Hag', 'CR':
        '450XP'},
    7: {'Name': 'Killer Whale', 'CR': '700XP'},
    8: {'Name': 'Giant Shark, Sahuagin Baron, Water Elemental', 'CR': '1800XP'},
    9: {'Name': 'Marid', 'CR': '7200XP'},
    10: {'Name': 'Storm Giant', 'CR': '10000XP'},
    11: {'Name': 'Dragon Turtle', 'CR': '18000XP'},
    12: {'Name': 'Kraken', 'CR': '50000XP'},
}

urban = {
    1: {'Name': 'Cat, Commoner, Goat, Rat, Raven', 'CR': '10XP'},
    2: {'Name': 'Bandit, Cultist, Flying Snake, Giant Rat, Guard, Kobold, Mastiff, Mule, Noble, Pony, Stirge',
        'CR': '25XP'},
    3: {'Name': 'Acolyte, Draft Horse, Giant Centipede, Giant Poisonous Snake, Kenku, Pseudodragon, Riding Horse, '
                'Skeleton, Smoke Mephit, Swarm of Bats, Swarm of Rats, Swarm of Ravens, Winged Kobold, Zombie',
        'CR': '50XP'},
    4: {'Name': 'Crocodile, Giant Wasp, Shadow, Swarm of Insects, Thug, Warhorse', 'CR': '100XP'},
    5: {'Name': 'Ghoul, Giant Spider, Half-Ogre, Specter, Spy, Yuan-ti Pureblood', 'CR': '200XP'},
    6: {'Name': 'Bandit Captain, Cult Fanatic, Gargoyle, Ghast, Mimic, Priest, Wererat, Will-o-Wasp', 'CR': '450XP'},
    7: {'Name': 'Doppelganger, Knight, Phase Spider, Veteran, Water Weird, Wight', 'CR': '700XP'},
    8: {'Name': 'Couatl, Ghost, Succubus or Incubus', 'CR': '1100XP'},
    9: {'Name': 'Cambion, Gladiator, Revenant, Vampire Spawn', 'CR': '1800XP'},
    10: {'Name': 'Invisible Stalker, Mage', 'CR': '2300XP'},
    11: {'Name': 'Oni, Shield Guardian', 'CR': '2900XP'},
    12: {'Name': 'Assassin', 'CR': '3900XP'},
    13: {'Name': 'Gray Sladd, Young Silver Dragon', 'CR': '5000XP'},
    14: {'Name': 'Archmage', 'CR': '8400XP'},
    15: {'Name': 'Rakshasa, Vampire', 'CR': '10000XP'},
    16: {'Name': 'Spellcaster or Warrior Vampire', 'CR': '13000XP'},
    17: {'Name': 'Adult Silver Dragon', 'CR': '15000XP'},
    18: {'Name': 'Ancient Silver Dragon', 'CR': '50000XP'},
    19: {'Name': 'Tarrasque', 'CR': '155000XP'},
}

