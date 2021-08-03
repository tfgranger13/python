from random import randint
class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 5
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength + randint(-5, 5)
        return self

