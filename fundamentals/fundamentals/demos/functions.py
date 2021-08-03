"""

# establish as a function to not repeat yourself

# start with def to define the function, colon to show what is part of the function
# parameters go inside the parentheses
def function_name():
    # indentation shows what is part of the code block
    print("Hello there!")


# call functions after defining them
function_name()


# input has specific built in use, do not use as a variable name (def, print, input)
def reverse_string(string):
    # string is the parameter, name is arbitrary

    # define the output variable before returning it
    output = ''

    # for loop to reverse the string
    for char in string:
        output = char + output

    
    alternate for loop:
    for x in range(len(string)-1, -1, -1)
        output = output + string[x]
    

    # return the result
    return output


# pring the output to check if it works
# calling the function enter an argument (called a parameter in the function)
print(reverse_string('hello'))

# default parameters and named arguments
# set defaults when declaring the parameters


# if we don't provide any arguments, it will make these the defaults
def be_cheerful(name='', repeat=2):
    # /n is an escape character for a new line
    print(f"good morning {name}\n" * repeat)


be_cheerful() # output: good morning (repeated on 2 lines)

be_cheerful("tim") # output: good morning tim (repeated on 2 lines)

be_cheerful(name="john") # output: good morning john (repeated on 2 lines)

#explicitly provide just the repeat value/not first parameter by saying the name
be_cheerful(repeat=6) # output: good morning (repeated on 6 lines)

be_cheerful(name="michael", repeat=5) # output: good morning michael (repeated on 5 lines)

# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# output: good morning kb (repeated on 3 lines)
be_cheerful(repeat=3, name="kb")
"""

# dice rolling function
# 3d6, 1d20, 2d4, d6 - number of dice followed by the sides on the dice
# 4, 6, 8, 10, 12, 20
# 3d6 + 2 (modifier)
# input number of dice, sides on dice, modifier

#call the random library so the contents are availalbe to us
#import random

# more specifically,
from random import randint

# set the defaults at the beginning of the function
def roll_dice(number = 1, sides = 20, modifier = 0):
    #start with a result of 0
    result = 0
    
    #roll number of dice
    for x in range(0, number):
        #for each side
        result += randint(1, sides)
    
    #add the modifier
    result += modifier

    return result

# strength, dexterity, constitution, intelligence, wisdom, charisma
# STR, DEX, CON, INT, WIS, CHA

# def generate_gygaxian_character():

#     # define the stats
#     stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

#     #define the character as a dictionary
#     character = {}

#     # for loop to go through each stat
#     for stat in stats:
#         # roll dice for each stat
#         character[stat] = roll_dice(3, 6)

#     # return the stats of the character
#     return character



def generate_gygaxian_character():

    # define the stats
    stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

    #define the character as a dictionary
    character = {'STR': None, 'DEX': None, 'CON': None, 'INT': None, 'WIS': None, 'CHA': None}

    # for loop to go through each stat
    for stat in character:
        # roll dice for each stat
        character[stat] = roll_dice(3, 6)

    # return the stats of the character
    return character
print(generate_gygaxian_character())


# ctrl + c is a kill command to stop infinite loops