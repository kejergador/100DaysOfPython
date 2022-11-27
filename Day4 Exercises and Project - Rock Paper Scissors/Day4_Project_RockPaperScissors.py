import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
isWin = False
isTie = False
map = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
randChoice = random.randint(0,2)
if choice == 0:
  print(rock)
  if randChoice == 0:
    isTie = True
  if randChoice == 1:
    isWin = False
  if randChoice == 2:
    isWin = True
elif choice == 1:
  print(paper)
  if randChoice == 0:
    isWin = True
  if randChoice == 1:
    isTie = True
  if randChoice == 2:
    isWin = False
elif choice == 2:
  print(scissors)
  if randChoice == 0:
    isWin = False
  if randChoice == 1:
    isWin = True
  if randChoice == 2:
    isTie = True


computerChoice =  map[randChoice]
print(f"Computer chose:\n\n{computerChoice}")

if isTie:
  print("It's a draw!")
else:
  if isWin:
    print("You win!")
  else:
    print("You lose!")








