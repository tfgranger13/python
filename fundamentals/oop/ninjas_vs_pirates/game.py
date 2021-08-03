from classes.ninja import Ninja
from classes.pirate import Pirate
from random import randint

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

# start the battle
# while both players have health > 0
    # turn counter ticks up
    # check speed to see if they can attack that turn
        # random 1/10 chance to trip
        # if yes, attack opponent
            # randomize dmg
        # if no, wait
    # check health at end of each round if:
        # one or more ppls is ded, end the battle and declare the winner
        # both ded, draw and res

def epic_battle(combatant_1, combatant_2):
    turn = 0
    while (combatant_1.health > 0 and combatant_2.health > 0):
        
        turn += 1
        
        if (turn % combatant_1.speed == 0):
            if randint(1, 10)!=1:
                combatant_1.attack(combatant_2)
        if (turn % combatant_2.speed == 0):
            if randint(1, 10)!=1:
                combatant_2.attack(combatant_1)

        if (combatant_1.health > 0 and combatant_2.health <= 0):
            print(f"The winner is {combatant_1.name}!")
        if (combatant_2.health > 0 and combatant_1.health <= 0):
            print(f"The winner is {combatant_2.name}!")
        if (combatant_1.health <= 0 and combatant_2.health <= 0):
            print("It is a draw! Try again with new combatants.")

epic_battle(michelangelo, jack_sparrow)