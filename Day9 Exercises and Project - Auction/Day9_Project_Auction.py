#from os import system, name
from replit import clear


def logo():
  print('''
                           ___________
                           \         /
                            )_______(
                            |"""""""|_.-._,.---------.,_.-._
                            |       | | |               | | ''-.
                            |       |_| |_             _| |_..-'
                            |_______| '-' `'---------'` '-'
                            )"""""""(
                           /_________\\
                         .-------------.
                        /_______________\\
  ''')


#Check for the highest bid in the dictionary
def checkHighestBidder(dictAuctionLog):
  max = 0
  winner = ""
  for key in dictAuctionLog:
    if dictAuctionLog[key] > max:
      max = dictAuctionLog[key]
      winner = key
  print(f"Congrats! {winner.upper()}, you have won the auction with the bid of ${max}")

#ASCII art of a gavel used in auctions
logo()
print("Welcome to the secret auction program.")
auction_log = {}
isRerun = True
while isRerun:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  auction_log[name] = bid
  #Testing Code
  print(f"\n{auction_log}")
  choice = input("Are there any other bidders? Type 'yes or 'no'.").lower()
  if choice == 'no':
    isRerun = False
    clear()
    checkHighestBidder(auction_log)
  else: 
    clear()
