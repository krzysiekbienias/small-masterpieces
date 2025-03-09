import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []

    def create_deck(self):
        for suit in DeckOfCards().SUITS:
            for rank in DeckOfCards().RANKS:
                self.__cards.append((suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        while self.__cards:
            self.__cards.pop()
        return None

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
if __name__=='__main__':
    deck=DeckOfCards()
    deck.create_deck()
    deck.shuffle_deck()
    deck.deal_card()