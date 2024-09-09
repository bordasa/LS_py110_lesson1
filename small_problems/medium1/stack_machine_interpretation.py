"""
-n : Place an integer value, n, in the register. Do not modify the stack.
-PUSH: Push the current register value onto the stack. Leave the value in the register.
ADD: Pop a value from the stack and add it to the register value, storing the result in the register.
SUB: POP a value from the stack and substract it from the register value, storing the result in the register.
MULT: POP a value from the stack and multiply it by the register value, storing the rsult in the register.
DIV: POP a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.
REMAINDER: POP a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.
POP: Remove the topmost item from the stack and place it in the register.
-PRINT: print the register value
"""

def minilang(string_command):
    tokens = string_command.split()
    stack = []
    register = 0

    for token in tokens:
        if token[-1].isnumeric():
            register = int(token)

        elif token.casefold() == 'print':
            print(register)

        elif token.casefold() == 'push':
            stack.append(register)

        elif stack:
            if token.casefold() == 'add':
                register += stack.pop()
            
            elif token.casefold() == 'sub':
                register -= stack.pop()
            
            elif token.casefold() == 'mult':
                register *= stack.pop()
            
            elif token.casefold() == 'div':
                register = register // stack.pop()
            
            elif token.casefold() == 'remainder':
                register = register % stack.pop()
            
            elif token.casefold() == 'pop':
                register = stack.pop()
        else:
            print('Error: Invalid token or Empty Stack')


minilang('PRINT')
print()
minilang('5 PUSH 3 MULT PRINT')
print()
minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
print()
minilang('5 PUSH POP PRINT')
print()
minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
print()
minilang('3 PUSH PUSH 7 DIV MULT PRINT')
print()
minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
print()
minilang('-3 PUSH 5 SUB PRINT')
print()
minilang('6 PUSH')
print('done')
minilang('add')