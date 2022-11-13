print('Welcome to the tip calculator\n\n\n')
total_bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10,12 or 15? '))
cus_num = int(input('How many people to split the bill? '))


payment_per_person = "{:.2f}".format((total_bill/cus_num)*(1+(tip/100)))
print(f'Each person should pay ${payment_per_person}')
