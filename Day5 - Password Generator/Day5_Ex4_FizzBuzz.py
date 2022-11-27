#Write your code below this row 👇
for numbers in range (1,101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("\nFizzBuzz")
    elif numbers % 3 == 0:
        print("\nFizz")
    elif numbers % 5 == 0:
        print("\nBuzz")
    else:
        print(f"\n{numbers}")
