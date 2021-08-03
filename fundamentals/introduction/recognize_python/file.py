num1 = 42 # variable declaration, integer
num2 = 2.3 # variable declaration, float
boolean = True # variable declaration, boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, access list value
pizza_toppings.append('Mushrooms') # add list value
print(person['name']) # log statement, access list value
person['name'] = 'George' # change list value
person['eye_color'] = 'blue' # change list value
print(fruit[2]) # log statement, access list value

if num1 > 45: # conditional if statement
    print("It's greater") # log statement
else: # conditional else statment
    print("It's lower") # log statement

if len(string) < 5: # conditional if statement
    print("It's a short word!") # log statement
elif len(string) > 15: # conditional else if statement
    print("It's a long word!") # log statement
else: # conditional else statement
    print("Just right!") # log statement

for x in range(5): # for loop end 5
    print(x) # for loop sequence, log statement
for x in range(2,5): # for loop start 2, end 5
    print(x) # for loop sequence, log statement
for x in range(2,10,3): # for loop start 2, end 10, increment 3
    print(x) # log statment
x = 0 # variable declaration
while(x < 5): # while loop condition less than 5
    print(x) # log statement
    x += 1 # while loop increment

pizza_toppings.pop() # 
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) - NameError: name <variable name> is not defined

# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)