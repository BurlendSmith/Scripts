# used to shuffle deck
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


# Each card is assigned a suit and a rank
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    # Returns a string of the card("Two of Hearts")
    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:  # Stores 52 card objs. in a list to be later shuffled
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # returns all 52 cards

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):  # shuffles deck
        random.shuffle(self.deck)

    def deal_one(self):  # deals cards to players
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? \n'))
        except:
            print('Sorry please provide an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry, you dont have enough chips! You have {}'.format(chips.total))
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter h or s\n')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player stands. Dealers turn\n')
            playing = False
        else:
            print('Sorry I did not understand that. Please enter h or s')
            continue
        break

def show_some(player, dealer):
    print('DEALERS HAND')
    print('one card hidden')
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND')
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print('DEALERS HAND')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND')
    for card in player.cards:
        print(card)


def player_busts(player,dealer,chips):
    print('BUST PLAYER\n')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('PLAYER WINS\n')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('PLAYER WINS, DEALER BUSTED\n')
    chips.win_bet()


def dealer_wins(player,dealer,chips):
    print('DEALER WINS!\n')
    chips.lose_bet()


def push(player,dealer):
    print('Dealer and player tie! PUSH\n')


# CONNECT

while True:

    print('Welcome to Blackjack\n')
    print('You have 100 chips\n')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())



    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)


    print('\nPlayer total chips are at {}'.format(player_chips.total))

    new_game = input('Would you like to play another hand? y/n\n')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing!')

        break

input('Press ENTER to exit')







