# def fibonacci(num):
#     if num <= 2:
#         return 1 # by definition
    
    # fib_num_tracker = [1, 1]
    
    # for _ in range(3, num + 1):
    #     fib_num = sum(fib_num_tracker[-2:])
    #     fib_num_tracker.append(fib_num)
        
    # return fib_num_tracker[-1]
    
def fibonacci(nth):
    if nth <= 2:
        return 1 #by definition
    
    previous, current = 1, 1

    for _ in range(3, nth + 1):
        previous, current = current, (previous + current)
    
    return current

print(fibonacci(1) == 1)
print(fibonacci(2) == 1)
print(fibonacci(3) == 2)
print(fibonacci(4) == 3)
print(fibonacci(5) == 5)
print(fibonacci(6) == 8)
print(fibonacci(12) == 144)
print(fibonacci(20) == 6765)
print(fibonacci(50) == 12586269025)
print(fibonacci(75) == 2111485077978050)