#Problem Overview
#Input: non-empty string 's'
#Output: a tuple consisting of a string and an integer ('t', k)
    #Rules:
        #s == t * k
        # t = shortest possible substring
        # k = largest possible repeat count
        # s is entirely lowercase letters

#Examples:

#Data Structure: string, count variable

#Algorithm:
    #1. Start with a count
    #2. index for range 0, len(str)
    #3. Slice string to index
    #4. Check count using find. if >=, replace count and save string slice
    #5. Return slice and count

#Code

def repeated_substring(string):
    final_count = 0
    final_substring = ''

    for index in range(0, len(string)):
        current_substring = string[: index + 1]
        
        current_count = string.count(current_substring)
        
        if current_count >= final_count:
            final_count = current_count
            final_substring = current_substring
    
    return (final_substring, final_count)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))