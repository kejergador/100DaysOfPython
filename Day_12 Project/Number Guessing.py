#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

logo = """
                                                                                                                
,--.  ,--.                  ,--.                      ,----.                                ,--.                
|  ,'.|  |,--.,--.,--,--,--.|  |-.  ,---. ,--.--.    '  .-./   ,--.,--. ,---.  ,---.  ,---. `--',--,--,  ,---.  
|  |' '  ||  ||  ||        || .-. '| .-. :|  .--'    |  | .---.|  ||  || .-. :(  .-' (  .-' ,--.|      \| .-. | 
|  | `   |'  ''  '|  |  |  || `-' |\   --.|  |       '  '--'  |'  ''  '\   --..-'  `).-'  `)|  ||  ||  |' '-' ' 
`--'  `--' `----' `--`--`--' `---'  `----'`--'        `------'  `----'  `----'`----' `----' `--'`--''--'.`-  /  
                                                                                                        `---'   
"""

def print_logo():
  """Print the number guessing game logo."""
  print(logo)

def generate_random_number():
  """Generate a random number from 0 to 100."""
  number = random.randint(0,100)
  return number

def check_lives():
  global lives
  """Return remaining lives left."""
  return f"You have {lives} attempts remaining to guess the number."

def make_guess():
  """Compare the random number to the user's guessed number."""
  global random_number, lives
  user_guess = int(input("Make a guess:"))
  if user_guess == random_number:
    lives = 0
    return "You win! Great! You guessed the number. Congrats!"
  elif user_guess > random_number:
    lives -= 1
    print("Too high.")
  elif user_guess < random_number:
    lives -= 1
    print("Too low.")
  if lives >= 1:
    print("Guess again.")
    
    
  

print_logo()
print("Welcome to the Number Guessing Game! Developed by Kevin Gador ")
print("I am thinking of a number between 0 and 100.")
#testing code
random_number = generate_random_number()
print(f"psst the correct answer is {random_number}")


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
  lives = 10
else:
  lives = 5

while lives != 0:
  print(check_lives())
  make_guess()
if lives == 0:
  print(f"You've run out of guesses.The number is {random_number}. Game over!")
