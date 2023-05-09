import random

trap_dc = {
    "Normal": 10,
    "Hard": 15,
    "Very Hard": 20,
    "Deadly": 25,
    "Godly": 30
}

road_trap = [
    "Pressure Plate Trap",
    "Down Tree Timers (Consecutive Trees Falling)",
    "Random Arrow Attacks",
    "Net Traps",
    "Fake Floor Trap",
    "Collapsing Trees Coming Together",
    "Magic Traps",
    "Invisible Passage Way"
]

sea_trap = [
    "Magic Traps",
    "Random Sea Bombs",
    "Net Traps",
    "Sand Bar",
    "Water Rifts",
    "Water instantly parts way into a water maze",
    "Air pockets that pop up random debris",
    "Whirlpool"
]

road_trip_magic_traps = [
    "Sleep",
    "Poison Gas",
    "Lightning Strike",
    "Laughing Gas",
    "A Magical Goat - Yeet!",
    "Fire Breathing Statues",
    "Random Chest Trigger",
    "Funny Polymorph",
    "Magnets",
    "Spider Web"
]

sea_trip_magic_traps = [
    "Halucinations",
    "Charmed",
    "Water Web (Spider Web)",
    "Water Tornados",
    "Illusionary Island (Gets group to move right onto an island)",
    "Massive Tsunami",
    "Random Gunpowder Barrels (May explode)",
    "Water Tornado",
    "Poisonous Fog",
    "Lightning Strike"
]


user_input = input("Road or Sea encounter? ")

while True:
    try:  
        if user_input.lower() == "road":
            print("Difficulty:",random.choice(list(trap_dc.items())))
            print("Kind of Trap:", random.choice(road_trap))
            print("Magic:", random.choice(road_trip_magic_traps))
            break
        elif user_input.lower() == "sea":
            print("Difficulty:",random.choice(list(trap_dc.items())))
            print("Kind of Trap:", random.choice(sea_trap))
            print("Magic:", random.choice(sea_trip_magic_traps))
            break
    except ValueError:
        print("Sorry, try entering 'Road' or 'Sea'")
