#input
    #floating point number representing an angle between 0 and 360 deg
#output
    #a string representing the angle in degrees, minutes, and seconds.
#Rules:
    #use degree symbol for degree, ' for minutes, and " for seconds
    # 60 mins in a degree, 60 seconds in a minute

#Data Structures:
    #Strings should be enough

#Algorithm
    #1. Get the number to the right of the decimal point
    #2. Convert that decimal number into minutes and seconds
        #a. how many digits? * 10 for denominator
        #b. number / denominator = minutes / 60 == decimal * 60
        #c. repeat for minutes decimal
        #d. minutes/denominator = seconds / 60 == decimal * 60
    #3. Insert into a string and return the string

#Code
def dms(num):
    DEGREE = "\u00B0"

    minutes = num % 1 * 60

    seconds = minutes % 1 * 60

    return f"{int(num)}{DEGREE}{int(minutes):02d}'{int(seconds):02d}\""



# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")