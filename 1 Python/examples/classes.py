from random import shuffle

# global constants are defined in the global scope
# by convention they use all caps names, and will never be changed in the code
SUITS = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
FACE_CARDS = ['K', 'Q', 'J', 'A']

# define class using class keyword and capital class name


class Card:
    is_card = True

    # overwrite the __init__ method if there is anything
    # that will make instances of this class distinct from each other
    # both positional and keyword arguments can be passed to __init__
    def __init__(self, value, suit) -> None:
        if suit in SUITS:
            self.suit = suit
        else:
            raise TypeError(f'{suit} is not a valid suit')

        self.value = value

        if value in FACE_CARDS:
            self.value = value
        else:
            try:
                if 10 >= int(value) >= 2:
                    self.value = value
                else:
                    raise TypeError(f'{value} is not a valid value')
            except ValueError:
                raise TypeError(f'{value} is not a valid value')

    def show(self):
        print(self)

    def __eq__(self, __o: object) -> bool:
        if self.suit == __o.suit and self.value == __o.value:
            return True
        else:
            return False

    # overwrite the "string method" to determine what will display
    # when you print (or string cast) an instance of this class
    def __str__(self) -> str:
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self) -> None:
        # in the init method you can define attributes, call methods,
        # or execute code
        self.cards = []
        self.build()

    def build(self):
        for suit in SUITS:
            for i in range(2, 11):
                card = Card(str(i), suit)
                self.cards.append(card)
            for val in FACE_CARDS:
                card = Card(val, suit)
                self.cards.append(card)

    def shuffle(self):
        shuffle(self.cards)

    def deal_hands(self, players: list, count: int):
        # TODO: detect when the deck is empty?
        for _ in range(count):
            for p in players:
                # here, p is an instance of the Player class
                # so we can make changes to that player's .cards attribute
                p.cards.append(self.cards.pop())

    # you can define any of the dunder methods, or "magic methods"
    # whether or not they have been previously defined for this class
    def __len__(self) -> int:
        return len(self.cards)


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []

    def draw(self, deck):
        # here, deck is an instance of the deck Class
        self.cards.append(deck.cards.pop())

    def discard(self, card_index: int):
        self.cards.pop(card_index)

    def show_hand(self):
        cards = [str(card) for card in self.cards]
        print(", ".join(cards))

    def __str__(self) -> str:
        return f'Player: {self.name}'


if __name__ == '__main__':
    # creating a single card
    ace = Card('A', 'Spades')
    print(type(ace))
    ace.show()
    print(ace)

    ace2 = Card('A', 'Spades')
    print(ace == ace)
    print(ace == ace2)

    # To set up the game:
    # create a deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # create players
    a = Player('Abby')
    b = Player('Bob')
    c = Player('Caroline')

    # deal cards to the players from the deck
    deck.deal_hands([a, b, c], 5)

    print(a)
    print(len(deck))

    a.show_hand()
    a.draw(deck)
    a.discard(2)
    a.show_hand()
