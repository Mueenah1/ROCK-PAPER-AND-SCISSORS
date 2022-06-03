
from requests import options


game = True
while game == True:
    computer =['R', 'S', 'P']
    name= input('Enter your name: ')
    print('Hello ' + name+', Welcome to Rock, Paper and Scissors game.')
    player= input('Enter R for ROOCK, S for SCISSORS, P for PAPER: ')
    print(player)
    for i in player:
        if i in computer:
            continue
        else:
            break
            print('Wrong entry, input a valid letter...')
        
    import random
    computer_option = random.choice(computer)
    print('I choose '+ computer_option + '.')
    if player ==computer_option:
        print('Tie')
    elif player == 'R' and computer_option == 'S':
        print('Hurray, you win :)')
    elif player == 'R' and computer_option == 'P':
        print('Ohoh, you lose :(')
    elif player == 'S' and computer_option == 'R':
        print('Ohoh, you lose :(')
    elif player == 'S' and computer_option == 'P':
        print('Hurray, you win :)')
    elif player == 'P' and computer_option == 'R':
        print('Hurray, you win :)')
    elif player == 'P' and computer_option == 'S':
        print('Ohoh, you lose :(')
    elif player != computer_option:
        print('Invalid entry')
    print('Would you like to play again')
    retry = input('Enter Y to play again and N to stop: ')
    if retry == 'Y':
        continue
    else:
        print('See you later, '+ name + ' Bye:)')
        break