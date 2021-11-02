print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

from random import randint
ding=randint(0,100)
guesslist=[0]
while True:
    guess=int(input("What's your guess??"))
    if guess>100 or guess<1:
        print('Out of Bounds')
    elif guess==ding:
        print('WINNER WINNER CHICKEN DINNER')
        break
    elif guesslist[-1]==0:
        if abs(ding-guess)<=10:
            print('WARM!')
            guesslist.append(guess)
        else:
            print('COLD!')
    elif abs(ding-guess)<=abs(ding-guesslist[-1]):
        print('WARMER!')
        guesslist.append(guess)
    else:
        print('COLDER!')
        guesslist.append(guess)


    pass
