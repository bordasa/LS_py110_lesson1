#Problem Overview:
    #Input: a number (year)
    #Output a number (num of Friday the 13ths in that year)
    #Rules:
        #Can use datetime.date()
        #Assume years > 1752. All dates use Gregorian Cal

#Examples

#Data Structures: variables and tuples from datetime

#Algorithm
    #1. Import datetime
    #2. Iterate through all months 1-12
    #3. Check if the 13th of each month is on a Friday
    #4. If on a friday, add to count.
    #5. Return count at end

#Code
import datetime

def friday_the_13ths(year):
    count = 0

    for month in range(1, 13):
        if datetime.date(year, month, 13).weekday() == 4:
            count += 1
    
    return count

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True