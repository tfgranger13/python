# Encapsulation is the idea that an instance of the class is responsible for its own data
# I have a bank account, teller verifies account info, makes withdrawal from acct
# I can't just reach over and take money from the drawer

# Inheritance allows us to pass attributes and methods from parents to children
# Vehicles are a class that can carry cargo and passengers
# we wouldn't create vehicles, but we would create classes that inherit from our vehicle class:
# wheeled vehicles with wheels, aquatic vehicle that floats, winged vehicle that flies, living vehicles like a horse
# all require fuel, but it's different for each subclass
# multiple inheritance - a class can inherit from multiple classes

# Polymorphism - many forms, classes that are similar can behave similarly
# can have x = 34, y = 'hello!', z = {'key_a': 2883, 'key_b': 'a word!'}
# can find the length of each; len(x), len(y), len(z)
# each gives us a length, but differs based on the type of info (number of items, number of letters)

# Abstraction: an extension of encapsulation, we can hide things that a class doesn't need to know about
# a class can use methods of another class without needing to know how they work
# we can drive a car, fill tank with gas, might not be able to change oil but can take it somewhere to get oil changed
# can't make a car out of raw materials, but still know how to drive it

