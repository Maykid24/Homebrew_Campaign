# Bringing everything together from weather aspects
from weather_table import spring, summer, fall, winter



season_list = ["Spring", "Summer", "Fall", "Winter"]


def random_weather():
    print(*season_list, sep='|'.center(14))
    user_input = input("Which would you like to choose: ")
    while user_input.lower() not in [x.lower() for x in season_list]:
        print("Please select one item from the list: ")
        print(*season_list, sep='|'.center(14))
        user_input = input("What season would you like to pick? ")
    if user_input.lower() == "spring":
        spring()
    elif user_input.lower() == "summer":
        summer()
    elif user_input.lower() == "fall":
        fall()
    elif user_input.lower() == "winter":
        winter()


random_weather()
