#coding:utf-8

import random

#实现的纸牌类的定义

#要建立一张纸牌，可以用你想要的花色和牌值调用 Card。
#queen_of_diamonds = Card(1, 12)
class Card:
    """
    Represents a standard playing card.
    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """
    #Spades = 黑桃
    #suit_names 和 rank_names 这样的变量，都是在类内定义，
    # 但不在任何方法之内，这就叫做类的属性，因为它们属于类 Card
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King"]

#init方法可以为每一个属性接收一个可选参数来初始化。默认的牌面为梅花2
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

#以先把这些列表赋值到类的属性中去
    def __str__(self):
        """
        Returns a human-readable string representation.
        """
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __eq__(self, other):
        """
        Checks whether self and other have the same rank and suit.
        returns: boolean
        """
        return self.suit == other.suit and self.rank == other.rank

#个lt 就是『less than』的缩写，意思是『小于』
#lt接收两个参数，一个是self，一个是另外一个对象，
# 如果 self 严格小于另外一个对象，就返回真。
#     def __lt__(self, other):
#
#         # check the suits
#         if self.suit < other.suit:
#             return True
#         if self.suit > other.suit:
#             return False
#         # suits are the same... check ranks
#         return self.rank < other.rank

    #用元组对比就可以把代码写得更简洁
    def __lt__(self, other):
        """
        Compares this card to other, first by suit, then rank.
        returns: boolean
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

#定义(成副)纸牌
class Deck:
    """
    Represents a deck of cards.
    Attributes:
      cards: list of Card objects.
    """

    def __init__(self):
        """
        Initializes the Deck with 52 cards.
        """
        self.cards = []
        #生成了标准的五十二张牌来初始化
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """
        Returns a string representation of the deck.
        """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

#要添加一张牌，可以用列表的 append 方法
    def add_card(self, card):
        """
        Adds a card to the deck.
        card: Card
        """
        self.cards.append(card)

    def remove_card(self, card):
        """
        Removes a card from the deck or raises exception if it is not there.
        card: Card
        """
        self.cards.remove(card)

#需要一个方法来从牌堆中拿出和放入纸牌
    def pop_card(self, i=-1):
        """
        Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card.
        """
#pop 方法从列表中拿走最后一张牌
        return self.cards.pop(i)

#给 Deck写一个洗牌的方法
    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

# move_cards方法接收两个参数，一个Hand对象，以及一个要处理的纸牌数量。该方法会修改self和hand。返回为空。
#在有的游戏中，纸牌需要从一手牌拿出去放到另外一手牌中去，或者从手中拿出去放到牌堆里面。这就亏用
## move_cards来实现这些操作：第一个变量self可以是一副牌也可以是一手 牌，第二个变量虽然名字是hand，
# 实际上也可以是一个Deck对象
    def move_cards(self, hand, num):
        """
        Moves the given number of cards from the deck into the Hand.
        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())

#表示了 Hand 继承了 Deck
#意味着我们可以在 Hands 中使用 Decks中的那些方法，比如 pop_card 以及 add_card 等

class Hand(Deck):
    """Represents a hand of playing cards."""
#Hand类的init方法应该用一个空列表来初始化手中的牌，而不是像Deck类中那样用一整副52张牌
    def __init__(self, label=''):
        self.cards = []
        self.label = label

#该函数接收一个对象和一个方法的名字（作为字符串），然后返回提供该方法定义的类的名称
def find_defining_class(obj, method_name):
    """
    Finds and returns the class object that will provide
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    hand.sort()
    print(hand)