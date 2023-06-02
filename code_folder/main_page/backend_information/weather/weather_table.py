# Table file specifically for random weather association

import random


def clear_light_clouds():
    print("Clear Skies / Light Clouds: \n"
          "\n"
          "This is the game as you normally play it. Clear bright light during day time, \n"
          "view of the stars and moon at night. No modifiers are added to play.")
    print()

def heavy_clouds():
    print("Heavy Clouds: \n"
          "\n"
          "The sky is blocked. High flying aerial creatures have total cover, \n" 
          "and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). \n" 
          "Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.")
    print()

def rain():
    print("Rain: \n"
          "\n"
          "Unpleasant to travel in. If you have wagons, your travel pace is slowed by half. \n" 
          "If you attempt to take a long rest without cover, you must make a DC 12 Constitution \n" 
          "saving throw gain the benefits for a long rest. All fire damage rolls have a –2. \n" 
          "Also has the effect of Heavy Clouds.")
    print()

def heavy_rain():
    print("Heavy Rain: \n"
          "\n"
          "Same as rain, but the DC becomes 16 to benefit from a long rest without shelter \n" 
          "and if Heavy Rain occurs two days in a row wagon travel becomes impossible until \n"
          "one day without rain occurs. May cause flooding. All fire damage rolls have a –4. \n"
          "Lightning and Cold damage rolls gain a +2. Also has the effect of Heavy Clouds.")
    print()
    
def freezing_cold():
    print("Freezing Cold: "
          "\n"
          "If you attempt to take a long rest without cover and heat, you must make a \n"
          "DC 15 Constitution saving throw gain the benefits for a long rest. \n"
          "If you fail by 5 or more, you gain an additional level of Exhaustion. \n"
          "All cold damage rolls have a +2.")
    print()
    
def snow():
    print("Snow: \n"
          "\n"
          "Unpleasant to travel in. All travel speed is halved. If snow occurs for \n"
          "two days in row, all terrain is difficult terrain and wagon travel is impossible \n"
          "until one day without snow passes. Also has the the effect of Heavy Clouds and Freezing Cold. \n"
          "Replace with Rain when in climates without snow.")
    print()
    
def scorching_heat():
    print("Scorching Heat: \n"
          "\n"
          "Blistering heat that is unpleasant to travel in. Creatures that attempt to \n"
          "travel during day light hours require twice the ration of water, and creature \n"
          "that travel for 4 or more hours or engage in heavy activity for 1 or more hour during \n"
          "the day and do not immediately take a short or long rest under cover must make a \n"
          "DC 10 Constitution saving throw or gain a level of Exhaustion. All fire damage rolls have a +2. \n"
          "All cold damage rolls have a –2.")
    print()
    
def high_winds():
    print("High Winds: \n"
          "\n"
          "Turbulent gusts sweep across the land. Select a wind direction based on locale or roll \n"
          "a d4 and consult the table. Flying creatures gain +10 movement speed when moving with the wind, \n"
          "and –10 movement speed when moving against it. All ranged weapon attacks have a –2 to attack rolls, \n"
          "and their range is reduced by half when shooting into the wind.")
    print()
    
def thunderstorm():
    print("Thunderstorm: \n"
          "\n"
          "Lightning flashes and thunder crashes. All creatures are partially obscured if they are more \n"
          "than 20 feet from you. If you travel for 4 or more hours during a Thunderstorm, roll a d20. \n"
          "On a 1, you are struck by a lightning bolt dealing 3d12 lightning damage. Lightning and Thunder \n"
          "damage rolls have a +2. Also has the effect of Rain, High Winds, Heavy Clouds.")
    print()
    
def blizzard():
    print("Blizzard: \n"
          "\n"
          "At the end of every hour spend in a Blizzard, make a DC 12 Constitution saving. \n"
          "On failure, you take 3d4 cold damage and gain one level of exhaustion. \n"
          "You make this check with advantage if you have proper gear. All creatures are heavily \n"
          "obscured if they are more than 20 feet from you. All terrain is difficult terrain. \n"
          "Also has the effect of Snow, High Winds, and Freezing Cold. Replace with Thunderstorm when in climates without snow.")
    print()
    
def strange_phenomena():
    print("Strange Phenomena: \n"
          "\n"
          "The world is a magical and weird place. Something odd occurs today, rarely seen. \n"
          "If you have an effect in mind, use that. If not, draw from the following list for \n"
          "some somewhat generic events. Not all of these will be appropriate for your world and setting, \n"
          "select one that fits or roll on the following table.")
    print()
    
def ashfall():
    print("Ashfall: \n"
          "\n"
          "Heavy white clouds of swirling smoke fill the sky, and it rains ash that coats \n"
          "everything in little flecks. A smell of burning wood or sulphur permeates the air. \n"
          "Also has the the effect of Heavy Clouds.")
    print()
    
def solar_eclipse():
    print("Solar Eclipse: \n"
          "\n"
          "For 1 hour during the day, it becomes night. Either select a dramatic \n"
          "time or roll a d12 for the hour. May or may not have prophetic ramifications.")
    print()
    
def strange_lights():
    print("Strange Lights: \n"
          "\n"
          "Strange swirling lights fill the sky, swirls of green, blue, and purple. \n"
          "Night becomes dim (strangely hued) light until the effect ends.")
    print()
    
def meteor_shower():
    print("Meteor Shower: \n"
          "\n"
          "Stars begin to fall from the sky as lumps of stone and metal. \n"
          "All creatures gain 1 luck point as per the Lucky feat, which lasts until used \n"
          "or the weather changes. If you travel 4 or more hours outdoors through this weather, \n"
          "roll a d100. On a 1, a meteor strikes nearby, leaving 40d6 of devastation in it's wake, \n"
          "but perhaps you'll find something cool. Potential consequences: 2d12 damage from the shock wave, \n"
          "difficult terrain, or heavily obscuring dust clouds.")
    print()
    
def malevolent_storm():
    print("Malevolent Storm: \n"
          "\n"
          "Has the effects of a Thunderstorm, but the lightning seems to seek creatures out. \n"
          "While outside during this storm, roll a d20 every 1 hour you outside without shelter. \n"
          "On a 2-5, you are struck by a lightning bolt dealing 3d12 lightning damage. \n"
          "On a 1, you are attacked by an air elemental.")
    print()
    
def wild_magic_storm():
    print("Wild Magic Storm: \n"
          "\n"
          "Fluctuations in the weave drive strange flashing lights and odd phenomena \n"
          "sweeping across the world. Rain falls upwards, plants bloom unseasonable, \n"
          "and people see apparitions of the dead and gone. High chance of encounters \n"
          "with sentient plants, ghosts, and strange illusions. All spells cast are naturally \n"
          "upcast by 1 level, but trigger a Wild Surge as per a Wild Magic Sorcerer class feature \n"
          "until the storm subsides (or a table of similar effects including apparitions, illusions, and magical mishaps).")
    print()


def strange_phenomena_random():
    random_phenomena = random.randint(1, 6)
    if random_phenomena == 1:
        ashfall()
    elif random_phenomena == 2:
        solar_eclipse()
    elif random_phenomena == 3:
        strange_lights()
    elif random_phenomena == 4:
        meteor_shower()
    elif random_phenomena == 5:
        malevolent_storm()
    elif random_phenomena == 6:
        wild_magic_storm()


def winter():
    dice_random = random.randint(1, 100)
    if dice_random == 1:
        blizzard()
        thunderstorm()
    elif 2 <= dice_random <= 20:
        snow()
        rain()
    elif 21 <= dice_random <= 30:
        freezing_cold()
    elif 31 <= dice_random <= 40:
        heavy_clouds()
    elif 41 <= dice_random <= 60:
        clear_light_clouds()
    elif 61 <= dice_random <= 99:
        clear_light_clouds()
    elif dice_random == 100:
        strange_phenomena_random()
        

def spring():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 2:
        thunderstorm()
    elif 3 <= dice_random <= 5:
        heavy_rain()
    elif 6 <= dice_random <= 20:
        rain()
    elif 21 <= dice_random <= 50:
        clear_light_clouds()
    elif 51 <= dice_random <= 80:
        clear_light_clouds()
    elif 81 <= dice_random <= 90:
        high_winds()
    elif 91 <= dice_random <= 99:
        scorching_heat()
    elif dice_random == 100:
        strange_phenomena_random()


def summer():
    dice_random = random.randint(1, 100)
    if dice_random == 1:
        thunderstorm()
    elif 2 <= dice_random <= 5:
        rain()
    elif 6 <= dice_random <= 30:
        clear_light_clouds()
    elif 31 <= dice_random <= 80:
        clear_light_clouds()
    elif 81 <= dice_random <= 85:
        high_winds()
    elif 86 <= dice_random <= 99:
        scorching_heat()
    elif dice_random == 100:
        strange_phenomena_random()


def fall():
    dice_random = random.randint(1, 100)
    if 1 <= dice_random <= 2:
        thunderstorm()
    elif 3 <= dice_random <= 10:
        snow()
        rain()
    elif 11 <= dice_random <= 20:
        heavy_clouds()
    elif 21 <= dice_random <= 50:
        clear_light_clouds()
    elif 51 <= dice_random <= 70:
        clear_light_clouds()
    elif 71 <= dice_random <= 90:
        high_winds()
    elif 91 <= dice_random <= 99:
        scorching_heat()
    elif dice_random == 100:
        strange_phenomena_random()
