## PEDAC Guided Practice: Leftover Blocks

## Input: integer num of available blocks
## Output: integer num of blocks leftover after building tallest possible valid structure

## Rules:

## Explicit
## -Blocks are cubes
## -Structure is built in layers
## -Top layer is 1 block
## -Each upper block needs 4 blocks in lower
## -Each lower block can support multiple upper blocks
## -No Gaps

## Implicit
## - Layer number correlates with blocks in a layer:
## - The number of blocks ina  layer is layer number * layer number


## Questions
## - Is a lower layer valid if it has more blocks than it needs?
## - Will there aways be left-over blocks?



## Step 4: Algorithm
## 1. Create a var to track how many cubes are used
## 2. Build structure layer by layer. Start with layer 1.
## 3. determine how many cubes will be needed for next layer.
## 4. Do we have that many? If yes, subtract from the total. If no, how many are left?
## 5. Output the number of leftover blocks

def calculate_leftover_blocks(starting_amount):
    current_layer = 0
    leftover_blocks = starting_amount
    
    next_layer_blocks = (current_layer + 1)**2

    while next_layer_blocks <= leftover_blocks:
        leftover_blocks -= next_layer_blocks
        current_layer += 1
        next_layer_blocks = (current_layer + 1)**2
    
    return leftover_blocks



print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True