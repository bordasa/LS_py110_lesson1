#Input: a string
#Output: True or False
#Rules: True if all '()' are balanced. False otherwise. Can't be backwards.

#Examples


#Algorithm
    #1. Iterate through the string
    #2. Each time '(' is seen, save it.
    #3. Check that the next ')' is there
    #4. If not, return false

# def is_balanced(string):
#     tracking_list = []

#     for char in string:

#         if char == '(':
#             tracking_list.append(char)
            
        
#         if char == ')':
#             if not tracking_list:
#                 return False
            
#             elif tracking_list[-1] == '(':
#                 tracking_list.pop()

#     return len(tracking_list) == 0

def is_balanced(string):
    paren_balancer = 0
    square_brack_balancer = 0
    curly_brace_balancer = 0
    single_quote_balancer = 0
    double_quote_balancer = 0

    for char in string:
        match char:
            case '(':
                paren_balancer += 1
            case ')':
                if paren_balancer <= 0:
                    return False
                paren_balancer -= 1

            case '[':
                square_brack_balancer += 1
            case ']':
                if square_brack_balancer <= 0:
                    return False
                square_brack_balancer -= 1

            case '{':
                curly_brace_balancer += 1
            case '}':
                if curly_brace_balancer <= 0:
                    return False
                curly_brace_balancer -= 1

            case "'":
                single_quote_balancer += 1
            
            case '"':
                double_quote_balancer += 1

    if single_quote_balancer % 2 == 1 or double_quote_balancer % 2 == 1:
        return False
    
    else:
        return (paren_balancer, square_brack_balancer, curly_brace_balancer) == (0, 0, 0)


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("W[hat] (((is))) \"\"''up()"))# == False)      # True