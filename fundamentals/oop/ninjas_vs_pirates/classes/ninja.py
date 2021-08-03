from random import randint
class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 3
        self.health = 90
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength + randint(-5, 5)
        return self