print('Welcome to the Tip Calculator!')
bill = float(input('How much is the bill?\n$'))
tip_percent = float(input('What percent tip would you like to give? 10, 12, or 15%\n')) / 100
if tip_percent == 0:
    print("That\'s not very nice!")
people = int(input('How many people are splitting the cost?\n'))
full_cost = bill * tip_percent + bill
each_pay = format(full_cost / people, '.2f')
print(f'Each person should pay ${each_pay}')
