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
    

    summary ="{} Day Overview \nThe lowest temperature will be {}°C, and will occur on {}. \nThe highest temperature will be {}°C, and will occur on {}. \nThe average low this week is {}°C. \nThe average high this week is {}°C.".format(number,low,converted_dl, high, converted_dh, wlow_round, whigh_round)
    return summary

# # pass


"""Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

def generate_daily_summary(weather_data):    

# Make a loop that shows the date and min and max until loop is exhausted

# Pulls all converted dates
    d_list = [item[0] for item in weather_data]
    con_dlist = []
    for d_list in d_list: 
        d_l = datetime.fromisoformat(d_list) 
        converted_dl = (d_l.strftime("%A %d %B %Y"))
        con_dlist.append(converted_dl)

# List of lows in c
    min_list = [item[1] for item in weather_data]
    c_lows = []
    for f in min_list: 
        cl =((f - 32) * 5 / 9)
        cl_round = round(cl, 1)
        c_lows.append(cl_round)


# List of highs in c
    max_list = [item[2] for item in weather_data]
    c_highs= []
    for f in max_list: 
        ch =((f - 32) * 5 / 9)
        ch_round = round(ch, 1)
        c_highs.append(ch_round)


# summarize

    all_lists = con_dlist + c_lows + c_highs
    res = list(zip(con_dlist, c_lows, c_highs[3:]))

    numbers = len(all_lists)
    divide = numbers / 3 
    text = "{} \nMinimum Temperature: {}°C \nMaximum Temperature: {}°C".format(res[0][0], res[0][1], res[0][2])

    # for x in all_lists:
    #     for y in x:
    #         print(y)
    
 
    # # while 
    # # # # while the 
    # #     return text
    
    print(text)

    pass
