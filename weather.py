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
        
# convert_f_to_c. Lows. Highs
    f_lows = [item[1] for item in weather_data]
    c_lows = []
    for f in f_lows: 
        cl =((f - 32) * 5 / 9)
        cl_round = round(cl, 1)
        c_lows.append(cl_round)

    f_highs = [item[2] for item in weather_data]
    c_highs = []
    for f in f_highs: 
        ch =((f - 32) * 5 / 9)
        ch_round = round(ch, 1)
        c_highs.append(ch_round)


# Correct number of days
    number = len(weather_data)
    

# low and high are pulling the correct numbers in C.
    low = min(c_lows)

    high = max(c_highs)


# find the number in the list of the lowest f number
# use that number and pull the same number for the isodata
    
    l_index = c_lows.index(low)
    l_iso = weather_data[l_index][0]
    d_l = datetime.fromisoformat(l_iso) 
    converted_dl = (d_l.strftime("%A %d %B %Y"))
        
        
    h_index = c_highs.index(high)
    h_iso = weather_data[h_index][0]
    d_h = datetime.fromisoformat(h_iso) 
    converted_dh = (d_h.strftime("%A %d %B %Y"))
    

# Weekly average low and high
    wlow = sum(c_lows) / len(c_lows) 
    wlow_round = round(wlow, 1)
    
    
    whigh = sum(c_highs) / len(c_highs) 
    whigh_round = round(whigh, 1)
    

    summary =("{} Day Overview\n  The lowest temperature will be {}°C, and will occur on {}.\n  The highest temperature will be {}°C, and will occur on {}.\n  The average low this week is {}°C.\n  The average high this week is {}°C.\n".format(number,low,converted_dl,high, converted_dh,wlow_round,whigh_round))
    return summary

pass


def generate_daily_summary(weather_data):    
    summary = ''    
    for row in weather_data:
        date = convert_date(row[0])
        low = convert_f_to_c(row[1])
        c_low = format_temperature(low)
        high = convert_f_to_c(row[2])
        c_high = format_temperature(high)
        summary += ("---- {} ----\n  Minimum Temperature: {}\n  Maximum Temperature: {}\n\n".format(date, c_low, c_high))    
    
    return summary
 

    pass
