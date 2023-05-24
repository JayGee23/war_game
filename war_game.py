"""
File: war_game.py

Game based on the card game WAR. Card suits have been changed to Races and Card numbers have been changed to a character with a corresponding strength rating.
Example: 10 of hearts is changed to Dwarven Paladin with a strength of 10.
Every round will show how many cards each player has and there is an option to shuffle or quit using 's' or 'q' respectively.
Enjoy!

"""
import random

# Create Deck
card_suits = ["Human", "Elven", "Dwarven", "Goblin"]

card_values = {"Bard": 2, "Monk": 3, "Fighter": 4, "Cleric": 5, "Druid": 6, "Ranger": 7, "Rogue": 8, "Barbarian": 9, "Paladin": 10, "Sorcerer": 11, "Wizard": 12, "Warlock": 13, "Battle Mage": 14}

card_deck = []

# Classes/Functions
class Player:
    def __init__(self):
        self.score = 26
    
    def get_username(self):
        username = input("\nPlease type in a Username: ")
        print(f"\nThe mighty {username} has been created!")
        input("Press any key to continue: ")
        return username

    def get_villan(self):
        villians = ["Sauron", "The Dark One", "Vecna", "Homelander", "Darth Vader", "The Joker", "HAL 9000", "Cruella De Vil", "Hans Gruber", "Cersei Lannister"]
        opponent = random.choice(villians)
        print(f"\nYour opponent has been selected. You will face the dreaded..... {opponent}!")
        input("Press any key to continue: ")
        return opponent
    
class Card:
    def __init__(self, suit: str, name: str, strength: int):
        self.suit = suit
        self.name = name
        self.strength = strength

def generate_deck():
    for suit in card_suits:
        for name, strength in card_values.items():
            card = Card(suit, name, strength)
            card_deck.append(card)

player1_deck = []
player2_deck = []

def split_deck(deck):
    random.shuffle(deck)
    for card in deck:
        if len(player1_deck) < 26:
            player1_deck.append(card)
        else:
            player2_deck.append(card)

def shuffle_decks():
    random.shuffle(player1_deck)
    random.shuffle(player2_deck) 

def draw(deck):
    return deck.pop(0)

def turn(player_card, opp_card):
    print(f"{username}'s card is: {player_card.suit} {player_card.name}, Str: {player_card.strength}")
    print(f"{opponent}'s card is: {opp_card.suit} {opp_card.name}, Str: {opp_card.strength}")
    
    if player_card.strength > opp_card.strength:
        player1_deck.append(player_card)
        player1_deck.append(opp_card)
        player1.score += 1
        player2.score -= 1
        print(f"{username} wins the round")

    elif opp_card.strength > player_card.strength:
        player2_deck.append(opp_card)
        player2_deck.append(player_card)
        player2.score += 1
        player1.score -= 1
        print(f"{opponent} wins the round")

    else:
        print("!!WAR!!")
        if len(player1_deck) <=2 or len(player2_deck) <=2:
            print("Not enough cards for WAR. So there will be a Re-Draw.")
            player1_deck.append(player_card)
            player2_deck.append(opp_card)
            shuffle_decks
            return
        
        player_card2 = player1_deck.pop(0)
        player_card3 = player1_deck.pop(0)
        opp_card2 = player2_deck.pop(0)
        opp_card3 = player2_deck.pop(0)
        print(f"{username}'s cards are: {player_card2.suit} {player_card2.name}, Str: {player_card2.strength} and {player_card3.suit} {player_card3.name}, Str: {player_card3.strength}")
        print(f"{opponent}'s cards are: {opp_card2.suit} {opp_card2.name}, Str: {opp_card2.strength} and {opp_card3.suit} {opp_card3.name}, Str: {opp_card3.strength}")
        
        if player_card3.strength > opp_card3.strength:
            player1_deck.append(player_card)
            player1_deck.append(player_card2)
            player1_deck.append(player_card3)
            player1_deck.append(opp_card)
            player1_deck.append(opp_card2)
            player1_deck.append(opp_card3)
            player1.score += 3
            player2.score -= 3
            print(f"{username} wins the WAR")
        
        elif opp_card3.strength > player_card3.strength:
            player2_deck.append(opp_card)
            player2_deck.append(opp_card2)
            player2_deck.append(opp_card3)
            player2_deck.append(player_card)
            player2_deck.append(player_card2)
            player2_deck.append(player_card3)
            player2.score += 3
            player1.score -= 3
            print(f"{opponent} wins the WAR")

        else:
            print("A TIE. Who will win with brute strength?!")
            player1_strength = player_card.strength + player_card2.strength + player_card3.strength
            player2_strenth = opp_card.strength + opp_card2.strength + opp_card3.strength
            if  player1_strength >= player2_strenth:
                player1_deck.append(player_card)
                player1_deck.append(player_card2)
                player1_deck.append(player_card3)
                player1_deck.append(opp_card)
                player1_deck.append(opp_card2)
                player1_deck.append(opp_card3)
                player1.score += 3
                player2.score -= 3
                print(f"{username} wins the WAR with a brute strength of {player1_strength}!")
            
            else:
                player2_deck.append(opp_card)
                player2_deck.append(opp_card2)
                player2_deck.append(opp_card3)
                player2_deck.append(player_card)
                player2_deck.append(player_card2)
                player2_deck.append(player_card3)
                player2.score += 3
                player1.score -= 3
                print(f"{opponent} wins the WAR with a brute strength of {player2_strenth}!")






#----------------
#----------------

print("""

____    __    ____  ___      .______      
\   \  /  \  /   / /   \     |   _  \     
 \   \/    \/   / /  ^  \    |  |_)  |    
  \            / /  /_\  \   |      /     
   \    /\    / /  _____  \  |  |\  \----.
    \__/  \__/ /__/     \__\ | _| `._____|
                                          

""")

generate_deck()

player1 = Player()
player2 = Player()

split_deck(card_deck)

# Intro
print(f"\nWelcome to the Game of War!")

username = player1.get_username()

opponent = player2.get_villan()

print(f"\nToday we are here to witness the epic battle between {username} and {opponent}!!")
print("The crowd goes wild!")
input("Press any key to continue: ")

#Rules
print(f"\nThe Rules: \nEvery round, each player will draw a card. The card with the higher strength value wins. Both cards are returned to the winner's card deck. The player who reaches 52 cards first wins! \n\nA 'War' occurs when players draw cards with equal strength values. When this occurs, each player will draw two more cards. The strength value of the 3rd cards will be compared and the winner will return all six cards to their deck. \nIf the 3rd cards have equal strength, the round is decided by 'brute strength' where all 3 cards' strength values are added up and compared. The player with the higher strength total wins the round.")
print("\nPress 'S' after any round to shuffle the cards. Press 'Q' after any round to quit the game.")
input("Press any key to continue: ")


# Taking turns
round = 1
while True:
    print("\nRound: ", round)
    print(f"{username} has {len(player1_deck)} cards in their deck. --- {opponent} has {len(player2_deck)} cards in their deck.")
    player1_card = draw(player1_deck)
    player2_card = draw(player2_deck)

    turn(player1_card, player2_card)

    if len(player1_deck) == 0:
        print(f"{username} has been defeated by {opponent}!. {opponent} wins.... Better luck next time")
        break

    if len(player2_deck) == 0:
        print(f"{username} is victorious!! You have defeated {opponent}. Congratulations!!")
        break
    round += 1
    
    next = input("Press any key to continue to the next round: ")
    if next.lower() == "s":
        shuffle_decks
        print("The decks have been shuffled.")
        input("Press any key to continue: ")
    elif next.lower() == "q":
        print(f"{username} has decided to forfeit the game. {opponent} wins the game!. Better luck next time.")
        quit()
    else:
        continue