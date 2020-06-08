from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        self.values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self.cards = [Card(a, i) for a in self.suits for i in self.values]
    
    def __repr__(self):
        return f"Deck of {self.count()} cards"
    
    def count(self):
        count = len(self.cards)
        return count
    
    def _deal(self, number):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        no_cards_to_remove = min(self.count(), number)
        dealt_cards = self.cards[-no_cards_to_remove:]
        self.cards = self.cards[:-no_cards_to_remove]
        return dealt_cards
    
    def shuffle(self):
        if self.count() == 52:
            shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")
        return self
    
    def deal_card(self):
        return self._deal(1)
    
    def deal_hand(self, number):
        return self._deal(number)
        
        
deck = Deck()
print(deck.count())
print(deck.deal_card())
print(deck.count())
print(deck.deal_hand(5))
print(deck.count())
print(deck.deal_hand(47))
print(deck.deal_card())
