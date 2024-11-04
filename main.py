# import functions from /src files
from src.api import get_coords, get_sun
from src.table import get_table

def main():
    # define empty entries variable
    entries = []
    print("Welcome to the sunrise/sunset table generator!")

    # Loop to control user entering or exiting program
    while True:
        user_action = input("Press 'e' to enter an entry to the table, or press 'q' to quit: ")
        if user_action == 'q':
            break
        elif user_action == 'e':
            # user inputs for country and date
            country_input = input("Enter country name: ") # e.g. "England"
            city_input = input("Enter city name: ") # e.g. "London"
            country = country_input.lower()
            city = city_input.lower()
            date = input("Input date in the format YYYY-MM-DD: ") # e.g. "1999-05-10"

            # use get_coords to obtain latitude/longitude and get_sun to get corresponding sunrise/sunset times in UTC
            coords = get_coords(city, country)
            sun = get_sun(date, coords['longitude'], coords['latitude'])

            # formatting of date using string slicing
            day = date[8:]
            month = date[5:7]
            year = date[:4]
            formatted_date = f"{day}/{month}/{year}"

            # create current table entry variable and append to existing entries
            entry = [f"{country_input}", f"{city_input}", formatted_date, sun["sunrise"], sun["sunset"]]
            entries.append(entry)

            # use get_table function to create table in sunrise_sunset.txt
            table = get_table(entries)

            # print current table so user can easily see it, and then repeat loop
            print(f"Your current table:\n{table}This table is saved within the 'sunrise-sunset.txt' file in the project directory")
        else:
            print("Invalid input. Please try again.")

# if this script is run directly (not imported as a module), then execute the main function
if __name__ == "__main__":
    main()

