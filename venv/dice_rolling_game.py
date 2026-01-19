# ask: roll a dice
# if user enters y
#   Generate two random numbers
#   print the sum of the two numbers
# If user enters n
#   print "Game exited"
# else
#   print "Invalid input"

import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f'You rolled a {die1} and a {die2}. Total: {total}')
    elif choice == 'n':
        print('Game exited')
        break
    else:
        print('Invalid input!')