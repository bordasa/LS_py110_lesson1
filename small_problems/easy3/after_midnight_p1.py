#Problem
    #Input: time in minutes before or after midnight (- before, + after)
    #Output: regular time in 24 hour format (hh:mm) string
    #Rules:
        #cannot use python datetime module
        #should work with any integer input

#Examples

#Data Structures

#Algorithms
    #1. convert minutes before/after midnight to hh:mm before or after midnight
    #2. If after midnight, make sure its less than 24
    #3. If negative, add 24 hours until it is positive
    #4. Return result as string

#Code

def time_of_day(minutes2midnight):
    hours, minutes = divmod(minutes2midnight, 60)
    
    while hours < 0:
        hours += 24
    
    while hours > 24:
        hours -= 24
    
    return f"{hours:02}:{minutes:02}"

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True