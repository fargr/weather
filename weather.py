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



def load_data_from_csv(csv_file):
    not_empties = []
    with open(csv_file, "r", encoding="utf-8") as file:
        data = list(csv.reader(file))
        for line in data[1:]: 
            if line != []:
                line1 = int(line[1])
                line2 = int(line[2])      
                not_empties.append([line[0], line1, line2])          
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

"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

def generate_summary(weather_data):
        
# convert_f_to_c
        
# # Correct number of days
#         number = len(weather_data)
#         print(number)
        

# # low and high are pulling the correct numbers in F 
#         low = min(map(lambda x: x[1], cweather_data))

#         high = max(map(lambda x: x[2], cweather_data))
#         print(low,high)


#         # lowdate =    
#         d = datetime.fromisoformat(weather_data) 
#         converted = (d.strftime("%A %d %B %Y"))
#         lowdate = (lowlist[1])

#         highdate = 
#         d = datetime.fromisoformat(weather_data) 
#         converted = (d.strftime("%A %d %B %Y"))

         
        # wlow
        # whigh = 
#         summary = "{} day overview \nThe lowest temperature will be {}°C, and will occur on {}\nThe highest temperature will be {}°C, and will occur on {}.\nThe average low this week is {}°C.\nThe average high this week is {}°C.".format(number,low,lowdate, high, highdate, wlow, whigh)
#         return(summary)

# pass


# """Outputs a daily summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """

# # def generate_daily_summary(weather_data):    

# #     date = 
# #     min = "Minimum Temperature:"
# #     max = "Maximum Temperature:"

# #     pass
