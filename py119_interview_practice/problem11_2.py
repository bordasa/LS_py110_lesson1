#Problem Overview
    #Input: non-empty string 's'
    #Output: tuple (string, integer) (t, k)
    #Rules: s == t * k
        #Assume string is all lower

#Examples:

#Data Structures: use string slicing

#Algorithm:
    #1. iterate through each index
    #2. Slice the string from start to index + 1. This is substring
    #3. get count of substring in main_string
    #4. multiply substring * count. if == main_string, we have our answer

#Code
def repeated_substring(main_string):
    for index in range(len(main_string)):
        substring = main_string[: index + 1]
        count = main_string.count(substring)

        if substring * count == main_string:
            return (substring, count)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))
