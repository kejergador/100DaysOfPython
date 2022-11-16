print('''
88,dPYba,,adPYba,  ,adPPYYba, 888888888  ,adPPYba,  
88P'   "88"    "8a ""     `Y8      a8P" a8P_____88  
88      88      88 ,adPPPPP88   ,d8P'   8PP"""""""  
88      88      88 88,    ,88 ,d8"      "8b,   ,aa  
88      88      88 `"8bbdP"Y8 888888888  `"Ybbd8"'

88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 Find Winter the dog! 88888888888888888888888888888888888888888888888
Kevin Gador

''')
print("Welcome to the Maze!")
print("Your mission is to find your dog named Winter in the maze. \nBEWARE of your choices there are a monsters and traps that might lead to your demise.\n\n\n") 

choice = input("You entered the Maze. Welcome! Where do you want to go? \"Left\" or \"Right\"?").lower()
if choice == "left":
  choice = input("\n\nYou escaped death from traps! You see a small space where you can crawl and a pool of water. What will you do? \"Swim\" or \"Crawl\"?").lower()
  if choice == "crawl":
    choice = input("\n\nWise choice! The water was full of sea creatures waiting to feast on you! Next! You see three doors which will you choose?\"left\",\"middle\" or \"right\"?").lower()
    if choice == "left":
      print("\n\nThe room suddenly bursted into flames. Game over!")
    elif choice == "middle":
      print("\n\nYou hear the bark of your dog Winter. You found him! You win!")
    elif choice == "right":
      print("\n\nThe walls started to move towards you very fast! The walls has crushed you and your soul! Game over!")
  else:
    print("\n\nA megalodon with 3 tiger shark suddenly appears and chomps your body off! Game over!")
      
else:
  print("\n\nYou fell into a hole full of spikes. Game over!")
  
          
