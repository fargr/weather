# def generate_daily_summary(weather_data):    
#     d= datetime(weather_data)
#     date = (d.strftime("%A %d %B %Y"))
#     mint = ("Minimum Temperature:"(min(weather_data)))
#     maxt = ("Maximum Temperature:")
#     final = date, mint, maxt 
#     print (final)


# celsius = ((float(77)) - 32) * 5 / 9
# print(celsius)


# summary = "5 day overview \nThe lowest temperature will be {low}°C, and will occur on {low}\nThe highest temperature will be {high}°C, and will occur on {highdate}.\nThe average low this week is {wlow}°C.\nThe average high this week is {whigh}°C."
# print(summary)

# low = 5
# lowdate = "tuesday"
# high = 3
# highdate = "friday"
# wlow = 19
# whigh = 27
# summary = "5 day overview \nThe lowest temperature will be {}°C, and will occur on {}\nThe highest temperature will be {}°C, and will occur on {}.\nThe average low this week is {}°C.\nThe average high this week is {}°C.".format(low,lowdate, high, highdate, wlow, whigh)
# print(summary)

# def generate_summary(weather_data):
#     for line in weather_data[1:]: 
#         lowdata = int(line[1])
#         highdata = int(line[2]) 
#         degrees = lowdata + highdata    
#         return degrees
    
#     celsius = ((int(degrees)) - 32) * 5 / 9
#     print(celsius)
def generate_summary(weather_data):
    high = max(map(lambda x: x[3], weather_data))
    print(high)