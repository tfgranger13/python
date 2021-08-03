# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element)
def countdown(number):
    output = []
    for x in range(number, -1, -1):
        output.append(x)
    return output

#print(countdown(9))

# Create a function that will receive a list with two numbers. Print the first value and return the second
def print_and_return(list):
    print(list[0])
    return(list[1])

#print(print_and_return([1, 2]))

# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length
def first_plus_length(list):
    return list[0] + len(list)

# print(first_plus_length([11,2,3,4,12]))

#  Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second(list):
    # return false if the length of the list is less than 2
    if len(list)<2:
        return False
    # set the placeholder variables
    count = 0
    new_list = []
    # run thru the loop for the length of the list
    for x in list:
        if x > list[1]:
            count += 1
            new_list.append(x)
    # print the count of numbers, return the list
    print(count)
    return new_list

# print(values_greater_than_second([3]))

# Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value
def length_and_value(size, value):
    output = []
    for x in range(size):
        output.append(value)
    return output

# print(length_and_value(6, 2))