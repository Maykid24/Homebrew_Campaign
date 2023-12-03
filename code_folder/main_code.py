"""
Utilizing this page as a main page for python code
"""

import random

import main_page.backend_information.main_page_list as m_list
import main_page.backend_information.random_encounter as Random_Encounter
import main_page.backend_information.traps.travel_traps as trap_encounters
import main_page.backend_information.weather.weather_encounter as weather_encounters
import main_page.backend_information.treasure.random_treasure_choice as r_treasure_choice
import main_page.backend_information.random_mission_maker.mission_maker as m_maker


def front_page():
    print(*m_list.main_list, sep='|'.center(14))
    user_input = input("What would you like to do? ")
    while user_input.lower() not in [x.lower() for x in m_list.main_list]:
        print("Please select one item from the list: ")
        print(*m_list.main_list, sep='|'.center(14))
        user_input = input("What would you like to do? ")
    if user_input.lower() == "treasure":
        treasure_input = input("Individual or Hoard? ")
        if treasure_input.lower() == "hoard":
            r_treasure_choice.hoard_list()
        elif treasure_input.lower() == "individual":
            r_treasure_choice.individual_list()
    elif user_input.lower() == "monsters":
        Random_Encounter.random_monsters()
    elif user_input.lower() == "encounter":
        Random_Encounter.random_encounter_chart()
    elif user_input.lower() == "traps":
        trap_encounters.trap_encounters()
    elif user_input.lower() == "weather":
        weather_encounters.random_weather()
    elif user_input.lower() == "mission":
        mission_maker = m_maker.RandomMissionMaker()

        for _ in range(5):  # Generate 5 random missions for demonstration
            random_mission = mission_maker.generate_random_mission()
            print(f"\nMission: {random_mission.name}")
            print(f"Description: {random_mission.description}")
            print(f"Objectives: {', '.join(random_mission.objectives) if random_mission.objectives else 'None'}")
            print(f"Rewards: {', '.join(random_mission.rewards)}\n")
    while True:
        proceed = input("Would you like to go back or are you done? ")
        if proceed == "back":
            front_page()
            break
        if proceed == "done":
            break
        

front_page()
