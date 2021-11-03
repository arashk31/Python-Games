from random import shuffle 

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess=''
    
    while guess not in ['0','1','2']:
        guess=input('Pick a number: 0, 1, 2! ')
    return int(guess)

def check_guess(guess, mylist):
    if mylist[guess]=='O':
        print('WINNER WINNER CHICKEN DINNER')
    else: 
        print(':( Please Try Again')
        print(mylist)
         
# Initial List
mylist=['','','O']
# Shuffle List
mixed_list=shuffle_list(mylist)
# User Guess
guess=player_guess()
# Check Guess
check_guess(guess,mixed_list)
