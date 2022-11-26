from replit import clear
#Calculator

def add(num1, num2):
  return num1 + num2
def multiply(num1,num2):
  return num1 * num2
def divide(num1, num2):
  return num1 / num2
def subtract(num1, num2):
  return num1 - num2

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

operations ={
  "+": add,
  "-": subtract,
  "/":divide,
  "*":multiply
}

def calculator():
  print(logo)
  isRerun = True
  num1 = float(input("What is the first number?: "))
  for symbol in operations:
    print(symbol)
  while isRerun:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    calc = operations[operation_symbol]
    answer = calc(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    choice = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
    if choice == 'n':
      isRerun = False
      clear()
      calculator()
    else:
      num1 = answer

calculator()
