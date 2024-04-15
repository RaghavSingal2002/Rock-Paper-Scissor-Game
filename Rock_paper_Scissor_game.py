import random

while True:
    print("1. Rock, 2. Scissors, 3. Paper")
    user_input = int(input("Enter the number : "))

    while user_input > 3 or user_input < 1:
        user_input = int(input("Please enter the number between 1-3"))

    if user_input == 1:
        user_input_choice = 'Rock'
    elif user_input == 2:
        user_input_choice = 'Scissors'
    else:
        user_input_choice = 'Paper'


    print("User has selected", user_input_choice)

    device_choice = random.randint(1, 3)

    while user_input == device_choice:
        device_choice = random.randint(1, 3)


    if device_choice == 1:
        device_input_choice = 'Rock'
    elif device_choice == 2:
        device_input_choice = 'Scissors'
    else:
        device_input_choice = 'Paper'


    print("Device has selected", device_input_choice)

    if (user_input == 1 and device_choice == 2) or (user_input == 2 and device_choice == 1):
        print("Rock Wins in this situation")
        result = 'Rock'
    elif (user_input == 1 and device_choice == 3) or (user_input == 3 and device_choice == 1):
        print("Paper Wins in this situation")
        result = 'Paper'
    else:
        print("Scissors Wins in this situation")
        result = 'Scissors'

    if user_input_choice == result:
        print("User Wins the game")
    else:
        print("Device Wins the game")

    print("Would you like to play again ?")
    print("Y for Yes else N for No")
    rematch = input()
    if rematch == 'n' or rematch == 'N':
        break


    print("Thank you for playing")


