#Problem
    #Input: time of day in 24 hour format
    #Output: 1 function minutes after midnight
        # Other function minutes before midnight
    #Rules:
        #No datetime module
        #return value in range 0 to 1439

#Examples:


#Data Structures

#Algorithm
    #1. Convert the hours and minutes to separate int values
    #2. Convert hours to minutes
    #3. Translate to minutes before midnight or after midnight

#Code

def after_midnight(clock_time):
    clock_hours = int(clock_time[:2])
    clock_mins = int(clock_time[-2:])
    
    mins_per_hour = 60
    hours_per_day = 24
    mins_per_day = mins_per_hour * hours_per_day

    mins_after_midnight = clock_hours * mins_per_hour + clock_mins

    if mins_after_midnight > 1439:
        mins_after_midnight -= mins_per_day

    return mins_after_midnight

def before_midnight(clock_time):
    
    mins_after_midnight = after_midnight(clock_time)

    mins_per_hour = 60
    hours_per_day = 24
    mins_per_day = mins_per_hour * hours_per_day

    mins_before_midnight = mins_per_day - mins_after_midnight

    if mins_before_midnight > 1439:
        mins_before_midnight -= mins_per_day

    return mins_before_midnight

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
