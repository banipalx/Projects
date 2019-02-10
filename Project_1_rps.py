import random


def rps():
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    else:
        computer_choice_scissors()


def computer_choice_rock():
    player = input('Choose 1 for rock, 2 for paper, or 3 for scissors: ')
    if player == '1':
        print('You Tied. You both chose rock!')
        try_again()
    elif player == '2':
        print('You Win. You chose paper and the computer chose rock!')
        try_again()
    elif player == '3':
        print('You Lose. You chose scissors and the computer chose rock!')
        try_again()
    else:
        print('Invalid input. Try again.')
        computer_choice_rock()


def computer_choice_paper():
    player = input('Choose 1 for rock, 2 for paper, or 3 for scissors: ')
    if player == '1':
        print('You Lose. You chose rock and the computer chose paper!')
        try_again()
    elif player == '2':
        print('You Tied. You both chose paper!')
        try_again()
    elif player == '3':
        print('You Win. You chose scissors and the computer chose paper!')
        try_again()
    else:
        print('Invalid input. Try again.')
        computer_choice_rock()


def computer_choice_scissors():
    player = input('Choose 1 for rock, 2 for paper, or 3 for scissors: ')
    if player == '1':
        print('You Win. You chose rock and the computer chose scissors!')
        try_again()
    elif player == '2':
        print('You Lose. You chose paper and the computer chose scissors!')
        try_again()
    elif player == '3':
        print('You Tied. You both chose scissors!')
        try_again()
    else:
        print('Invalid input. Try again.')
        computer_choice_rock()


def try_again():
    choice = input('Would you like to play again? (y/n) ').lower()
    if choice == 'y' or choice == 'yes':
        rps()
    elif choice == 'n' or choice == 'no':
        print('Thanks for playing!')
        quit()
    else:
        print('Invalid input. Try again.')
        try_again()


rps()


# 26/07/2018
