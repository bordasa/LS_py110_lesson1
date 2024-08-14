#Problem
    #input: list of elements
    #output: print the elements and the number of occurrances
    #Rules: Order of the output doesn't matter
        # - words are case sensitive

#Examples:


#Data Structure: Dictionary

#Algorithm:
    #1. Check an item in the list
    #2. If the item is in the dictionary, add 1 to count
    #3. If item is not in the dictionary, add it to the dictionary then add 1
    #4. Use dictionary values to print the output

#Code

def count_occurrences(list):
    count_dict = {}

    for item in list:
        item = item.casefold()
        # if item not in count_dict:
        #     count_dict[item] = 0
        
        # count_dict[item] += 1

        count_dict[item] = count_dict.get(item, 0) + 1
    
    for key, value in count_dict.items():
        print(f"{key} => {value}")


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck', 'suv']

count_occurrences(vehicles)