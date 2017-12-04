#coding:utf-8

import random

class Card(object):
    """
    Represents a standard playing card
    """
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])


    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other. rank
        return t1 < t2


class Deck(object):
    """Represents a 52 deck of cards"""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        return self.cards.sort()

    def deal_hands(self, hands, cards):
        res = []
        for hand in range(hands):
            for card in range(cards):
                res.append(self.pop_card())
        return res

class Hand(Deck):
    """
    Represents a hand of playing cards
    """
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

deck = Deck()
print deck.deal_hands(5, 5)