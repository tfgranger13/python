# many of the same types; booleans, values, strings

# python interpreter is an environment where the computer can immediately implement code
# use for testing/remembering if something works

# booleans start with capital T and F

#values are split between integers and floats
# floats are imperfect representations

# strings behave relatively the same, can use "" or ''

# do not need to establish variables with var
# automatically handles tedious actions

# lists, tuples, and dictionaries
# tuples are an immutable list (array) but cannot change definitions in it
# tuples use () instead of []
# lists are a lot like arrays in JS (pretty much the same)
# .push() becomes .append()
# dictionaries are pairs of key-value pairs (object has a different meaning in python)

# Loops
# print 1 to 255
for x in range(1,101):
    print(x)
    print(x*x)
# what happens inside a loop is identified by indentation
# this print is outside of the loop
print("Done!")

# careful copying and pasting, check for tabs vs. spaces, they indent differently

# if statements look a lot like for loops


# list of names
names = ["Sarah", 'jack', 'Beth', 'Jort']

# for loop to the length of the array
for x in range(0, len(names)):
    # print the name at index x
    print(names[x])

# gives the same output
# first part is arbitrary
# the second part is important and tells you where to look
for name in names:
    print(name)