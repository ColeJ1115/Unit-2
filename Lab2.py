name = input('What is your name? ')


while True:
     try:
        random_number = int(input("Enter a number between 1 and 100 "))
        if random_number < 60 and (random_number % 2) == 1:
            print('Your number is odd and less than 60! ')

        elif random_number >= 2 and random_number <= 24 and (random_number % 2) == 0:
            print('Even and less than 25. ')

        elif random_number >= 26 and random_number <= 60 and (random_number % 2) == 0:
            print('Even and between 26 and 60. ')

        elif random_number > 60 and random_number <= 100 and (random_number % 2) == 0:
            print('Even and greater than 60')

        elif random_number > 60 and random_number <= 100 and (random_number % 2) == 1:
            print('Odd and greater than 60. ')

        elif random_number > 100:
            print('That is beyond the given range, choose if you want to try again.')

        else:
            print('Your number is invalid.')

        repeat = input(f"Would you like to go again {name}? (y/n)\n> ")
        if repeat.lower() != 'y':
            break

     except ValueError:
         print(f'That is not a valid input {name}')
         break

print(f'Thanks for playing {name}')