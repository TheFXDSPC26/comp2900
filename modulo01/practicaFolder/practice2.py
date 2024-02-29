tries = 0
while tries <3:
    if tries ==2:
        print(f'You have {3-tries} attempt left')
    else:
        print(f'You have {3-tries} attempts left')
    
    guessNum = int(input('Welcome to the number guessing game!\n\nThe correct number is between 1 to 10\n\nEnter your number to get started: '))
    if guessNum == 9:
        print('Correct answer entered!!\n\nYou Win!!')
        exit()
    else:
        tries+=1
        if tries == 3:
            print('You lose')
            exit()
        else:
            print('\nTry again')        