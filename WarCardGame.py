# THIS IS A PROGRAM THAT IS  ALLOWS TWO AI TO PLAY EACH OTHER IN THE CARD GAME OF 'WAR' .


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

##################################################################################################################

class Card:
    
    def __init__(self,suit,rank):
    	'''
		Our constructor that instantiates cards.
    	'''
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
    	'''
		Allows for card objects to be printed
    	'''
        return self.rank + " of " + self.suit

##################################################################################################################

class Deck:  
    
    def __init__(self):
    	'''
		Our constructor method which instantiates the 52 card objects in the deck
    	'''
        self.all_cards = []

        # Adds each card object to the all_cards attribute

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank)) #adds card objects to all_cards

    def shuffle(self):
    	'''
		Shuffles the 52 card ojects in the deck
    	'''
        random.shuffle(self.all_cards) 

    def deal_one(self):
    	'''
    	Deals out one card to a player
    	'''
        return self.all_cards.pop()

##################################################################################################################

class Player:
    
    def __init__(self,name):
    	'''
		Our constructor method which instantiates player one and two
    	'''
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
    	'''
		Removes the first card from the top of the player's deck.
    	'''
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
    	'''
		Adds new cards to player's hand.
    	'''
        if type(new_cards) == type([]):
            # List of multiple card objects.
            self.all_cards.extend(new_cards)
        else:
            # For a single card object.
            self.all_cards.append(new_cards)
    
    def __str__(self):
    	'''
		Prints the amount of cards the player has.
    	'''
        return f'Player {self.name} has {len(self.all_cards)} cards.'

##################################################################################################################

# GAME SETUP

# Creates player one and player two objects

player_one = Player('One')
player_two = Player('Two')

# Creates a new deck and shuffles it.

new_deck = Deck()
new_deck.shuffle()

# Deals half of deck to each player.

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0

while game_on:

	# Adds one to the round_num variable each loop and prints it.

    round_num += 1
    print(f"Round {round_num}")
    
    # Checks if a player has won or lost by checking to see if each player's hand is empty.

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player One Wins')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player Two Wins')
        game_on = False
        break
        
    # Starts a new round

    # Lists represents cards on table/cards in play

    # Removes cards from player's cards and adds them to the current cards in play or list

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True
    
    while at_war:

    	# Checks if player one has beat player two during the war and adds player two's cards to their deck in addition to their own cards

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
    	# Checks if player one has beat player two during the war and adds player two's cards to their deck in addition to their own cards

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False
            
        else:
            print('WAR!')

            # Player two wins if player one doesn't have enough cards to declare war
           
        if len(player_one.all_cards) < 5:
            print('Player One unable to declare war')
            print('PLAYER TWO WINS!')
            game_on = False
            break
            
            # Player one wins if player two doesn't have enough cards to declare war

        elif len(player_two.all_cards) < 5:
            print('Player Two unable to declare war')
            print('PLAYER ONE WINS!')
            game_on = False
            break

            # Adds three cards to player's cards in play
            
        else:
            for num in range(3):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())

            

            

