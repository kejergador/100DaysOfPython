############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear


#init
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
choice = ""
isContinue = True
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def print_logo():
  print(logo)

def deal_card():
  return cards[random.randint(0,12)]


def calculate_score(cards):
  """Takes a list of cards and return the score calculated from the cards """
  score = sum(cards)
  if score == 21 and len(cards) == 2:
    return 0  
  if 11 in cards and score > 21:
    cards.remove(11)
    cards.append(1)
  return score

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "BUST! You lose!"
  if user_score == computer_score:
    return "It's a draw!"
  elif computer_score == 0:
    return "\tIt's a blackjack! Computer wins!"
  elif user_score == 0:
    return "\tIt's a blackjack! You win!"
  elif computer_score > 21:
    return "\tcomputer BUST. You win!"
  elif user_score > computer_score:
    return "\tYou win!"
  else:
    return "\tYou lose!"
def ask_continue():
  choice = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
  return choice

def play():
  print_logo()
  user_cards = []
  computer_cards = []
  game_end = False
  for _ in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())  

  while not game_end:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"\tYour cards: {user_cards}, current score: {user_score}")
    print(f"\tComputer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_end = True
    else:
      user_choice = input("Type 'hit' to get another card, type 'n' to pass: ").lower()
      if user_choice == "hit":
        user_cards.append(deal_card())
      else:
        game_end = True
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"\tYour final hand: {user_cards}, final score: {user_score}")
  print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  


while isContinue:
  choice = ask_continue()
  if choice == 'y':
    clear()
    play()
  else:
    isContinue = False
    clear()
    print("\n\nThank you for playing Kevin's Blackjack! Have a nice day :)")


