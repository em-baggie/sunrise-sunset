# Please see README.md for how to install additional modules
from tabulate import tabulate

def get_table(entries):
    # define table headers and table path
    headers = ["Country", "City", "Date", "Sunrise (UTC)", "Sunset (UTC)"]
    file_path = 'sunrise_sunset.txt'
    # create table using entries and headers
    table = tabulate(entries, headers, tablefmt="psql") + "\n"

    # write table to sunrise_sunset.txt file and return it
    with open(file_path, 'w+') as text_file:
        text_file.write(table)
    return table