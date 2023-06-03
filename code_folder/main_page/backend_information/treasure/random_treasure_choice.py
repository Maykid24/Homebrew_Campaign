import main_page.backend_information.treasure.hoard_treasure as hoard_treasure
import main_page.backend_information.treasure.individual_treasure as individual_treasure
import main_page.backend_information.main_page_list as m_list


def hoard_list():
    print(*m_list.difficulty_level, sep='|'.center(14))
    level_difficulty = input("What level difficulty? ")
    if level_difficulty.lower() == "0-4":
        hoard_treasure.hoard_challenge04()
    elif level_difficulty.lower() == "5-10":
        hoard_treasure.hoard_challenge510()
    elif level_difficulty.lower() == "11-16":
        hoard_treasure.hoard_challenge1116()
    elif level_difficulty.lower() == "17+":
        hoard_treasure.hoard_challenge17()


def individual_list():
    print(*m_list.difficulty_level, sep='|'.center(14))
    level_difficulty = input("What level difficulty? ")
    if level_difficulty.lower() == "0-4":
        individual_treasure.individual_challenge04()
    elif level_difficulty.lower() == "5-10":
        individual_treasure.individual_challenge510()
    elif level_difficulty.lower() == "11-16":
        individual_treasure.individual_challenge1116()
    elif level_difficulty.lower() == "17+":
        individual_treasure.individual_challenge17()