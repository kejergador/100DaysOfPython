from game_data import data
from art import logo,vs
from replit import clear
import random

# FUNCTIONS
def generate_account(data):
  """Returns a random account from the list."""
  account = random.choice(data)
  return account

def print_compare(list_data):
  """Prints the account's name, description and country from the list."""
  account_name = list_data["name"].title()
  account_description = list_data["description"].title()
  account_country = list_data["country"].title()
  return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(account_a,account_b,guess):
  """Returns true if the player guessed the account with more followers."""
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  if a_follower_count > b_follower_count:
    return guess == "a"
  else:
    return guess == "b"
  
  
# MAIN
game_over = False
score = 0
print(logo)
account_b = generate_account(data)
while not game_over:
  account_a = account_b
  account_b = generate_account(data)
  while account_a == account_b:
    account_b = generate_account(data)
  
  print(f"Compare A: {print_compare(account_a)}")
  print(vs)
  print(f"Against B: {print_compare(account_b)}")
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  is_correct = check_answer(account_a,account_b,guess)
  if is_correct:
    score += 1
    clear()
    print(logo)
    print(f"You're right! Current score: {score}")
  else:
    game_over = True
    clear()
    print(logo)
    print(f"Sorry, you're wrong. Final score: {score}")
 
