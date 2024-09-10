#algorithm
    #1. make 2 pointers and a swap tracker
    #2. Start at the front of the list
    #3. Compare the 2 pointers
        #3a If left > right, swap. Set swap tracker = True 
        #3b Else, do nothing
    #4. Move the pointers + 1 each and repeat Step 3
    #5. Stop when right gets to the end of the list
    #6. Repeat steps 2-5 again until no swaps are made

#Code

# def bubble_sort(list):
    
#     while True:
#         left = 0
#         right = 1
#         did_swap = False

#         while right < len(list):
#             if list[left] > list[right]:
#                 list[left], list[right] = list[right], list[left]
#                 did_swap = True
            
#             left += 1
#             right += 1
        
#         if did_swap == False:
#             break

def bubble_sort(lst):

    while True:
        did_swap = False

        for idx in range(1, len(lst)):
            if lst[idx - 1] > lst[idx]:
                lst[idx - 1], lst[idx] = lst[idx], lst[idx - 1]
                did_swap = True
        
        if not did_swap:
            break


lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True