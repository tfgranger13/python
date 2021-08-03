from random import randint

class Card():

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if value == 11:
            self.rank = 'Jack'
        elif value == 12:
            self.rank = 'Queen'
        elif value == 13:
            self.rank = 'King'
        elif value == 1:
            self.rank = 'Ace'
        else:
            self.rank = str(value)

    # code-facing
    def __repr__(self):
        # self.suit[0] returns just the first letter
        return f"{self.value}{self.suit[0]}"

    # user-facing
    def __str__(self):
        return f"{self.rank} of {self.suit}" 


class Deck():

    def __init__(self):

        self.suits = ['hearts', 'spades', 'diamonds', 'clubs']
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        # lists care about order, dictionaries don't necessarily
        self.contents = []
        for suit in self.suits:
            for value in self.values:
                self.contents.append(Card(suit, value))
        self.shuffle()

        # list comprehension
        # self.contents = [Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        for i in range(0, len(self.values)):
            x = randint(0, len(self.contents)-1)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]

    # encapsulation- the deck is responsible for handling its own events
    def deal_card(self):
        if len(self.contents)==0:
            return None
        return self.contents.pop()

    def deal_multiple_cards(self, number_of_cards):
        cards = []
        for i in range(0, len(number_of_cards)):
            cards.append(self.deal_card())
        return cards


new_deck = Deck()

print(new_deck.contents)
print(new_deck.contents[0])

new_deck.shuffle()
print(new_deck.contents)

player1 = []
player2 = []