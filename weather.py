import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):      
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
   d = datetime.fromisoformat(iso_string) 
   converted = (d.strftime("%A %d %B %Y"))
   return converted

pass


def convert_f_to_c(temp_in_farenheit):
    celsius = ((float(temp_in_farenheit)) - 32) * 5 / 9
    temps = float(round(celsius, 1))
    return temps

pass


def calculate_mean(weather_data):
    weather_data = ([float(x) for x in weather_data])
    data = sum(weather_data) / len(weather_data) 
    return data 

pass



"""Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
"""

# Can't figure out how to remove empty list
    
def load_data_from_csv(csv_file):
    not_empties = []
    with open(csv_file, "r", encoding="utf-8") as file:
        data = csv.reader(file)
        for line in data[1:]: 
            if line != []:
                not_empties.append(line)
        
        return(not_empties)

pass


def find_min(weather_data):
    if len(weather_data) > 0:
        min1 = float(min(weather_data))
        place = max(loc for loc, val in enumerate(weather_data) if val == (min(weather_data)))
        final = min1, place
        return final
    else:
        return ()

pass


def find_max(weather_data):
    if len(weather_data) > 0:
        max1 = float(max(weather_data))
        place = max(loc for loc, val in enumerate(weather_data) if val == (max(weather_data)))
        final = max1, place
        return final
    else: 
        return ()

    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
# low = 
# lowdate = 
# high =
# highdate = 
# wlow = 
# whigh = 

#      The lowest temperature will be low°C, and will occur on lowdate
#     The highest temperature will be high°C, and will occur on highdate.
#     The average low this week is wlow°C.
#     The average high this week is whigh°C.
#     pass



"""Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

# def generate_daily_summary(weather_data):    
#     d= datetime(weather_data)
#     date = (d.strftime("%A %d %B %Y"))
#     mint = (f"Minimum Temperature:"(min(weather_data)))
#     maxt = (f"Maximum Temperature:")
#     final = date, mint, maxt 
#     return final
#     pass
