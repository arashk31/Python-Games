#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Milestone Project 2 - Blackjack Game
# In this milestone project you will be creating a Complete BlackJack Card Game in Python.
# 
# Here are the requirements:
# 
# * You need to create a simple text-based [BlackJack](https://en.wikipedia.org/wiki/Blackjack) game
# * The game needs to have one player versus an automated dealer.
# * The player can stand or hit.
# * The player must be able to pick their betting amount.
# * You need to keep track of the player's total money.
# * You need to alert the player of wins, losses, or busts, etc...
# 
# And most importantly:
# 
# * **You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!**
# 
# 
# Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits! Remember to you are free to use any resources you want and as always:
# 
# # HAVE FUN!

# In[1]:


import random 
from IPython.display import clear_output

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# In[2]:


class Card:
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'


# In[3]:


class Deck:
    
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
        
    def deal_card(self):
        return self.all_cards.pop()


# In[4]:


class Player:
    
    def __init__(self,name, bankroll):
        self.name=name
        self.bankroll=bankroll
    
    def add_money(self, amount):
        self.bankroll+=amount
    
    def __str__(self):
        return f'{self.name} has ${self.bankroll}.'
    


# In[5]:


def display_player_cards(cardlist):
    print(f'Player cards: {cardlist}')
    if not cardlist.count('Ace'):
        print(f'Sum is {sum(map(lambda card: values[card],cardlist))}')
    else:
        print(f'Sum is {sum(map(lambda card: values[card],cardlist))-10}/{sum(map(lambda card: values[card],cardlist))}')


# In[6]:


def display_dealer_cards(cardlist):
    print(f'Dealer cards: {cardlist}')
    if not cardlist.count('Ace'):
        print(f'Sum is {sum(map(lambda card: values[card],cardlist))}')
    else:
        print(f'Sum is {sum(map(lambda card: values[card],cardlist))-10}/{sum(map(lambda card: values[card],cardlist))}')


# In[9]:


def get_bet(player):
    
    while 1:
        
        try:
            bet=int(input('How much would you like to bet? '))
            if bet<=0:
                print('Must be a positive value.')
                continue
            elif bet>player.bankroll:
                print(f'You have insufficient funds. Your current bankroll is {player.bankroll}.')
                continue
            return bet
        except:
            print('Please input a integer.')
            continue


# In[10]:


def get_hit():
    
    while 1:
        
        ans=input('Would you like to hit? (Y/N)')
        if ans.lower()[0]=='y':
            return True
        elif ans.lower()[0]=='n':
            return False
        else:
            print('I dont understand. Please input Y or N.')
        


# In[11]:


def card_sum(cardlist):
    card_sum=0
    ace=cardlist.count('Ace')
    for card in cardlist:
        card_sum+=values[card]
    while card_sum>21 and ace>0:
        card_sum-=10
        ace-=1
    return card_sum
        


# In[12]:


def play_again():
    
    while 1:    
        ans=input('Would you like to play again? (Y/N)')
        if ans.lower()[0]=='y':
            return True
        elif ans.lower()[0]=='n':
            return False
        else:
            print('I dont understand. Please input Y or N.')
        


# In[13]:


def player_ready():
    
    while 1:    
        ans=input('Are you ready to play? (Y/N)')
        if ans.lower()[0]=='y':
            return True
        elif ans.lower()[0]=='n':
            return False
        else:
            print('I dont understand. Please input Y or N.')


# In[14]:


def get_player():
    name=input('Please enter your game name: ')
    print(f'Welcome to the table {name} :)')
    while 1:
        try:
            bankroll=int(input('How much would you like to play with? '))
            break
        except:
            print('Please enter a positive integer.')
            continue
    player=Player(name, bankroll)
    print(f'Good luck {player.name}, you are starting with ${player.bankroll}!')
    print(player)
    return player


# In[ ]:





# In[ ]:


#print('Welcome to the nino! We are excited that you are here!')
print('The name of the game is BlackJack!\nYou will learn the rules as you play >:)')
player=get_player()
game_on=player_ready()
clear_output()
while game_on:
    player_bust=False
    dealer_bust=False
    mydeck=Deck()
    mydeck.shuffle_deck()
    bet=get_bet(player)
    player_cards=[]
    dealer_cards=[]
    player_cards.append(mydeck.deal_card().rank)
    dealer_cards.append(mydeck.deal_card().rank)
    player_cards.append(mydeck.deal_card().rank)
    dealer_hole_card=mydeck.deal_card()
    display_dealer_cards(dealer_cards)
    print('\n')
    display_player_cards(player_cards)
    if card_sum(player_cards)==21:
        print('BLACKJACK!')
        player.add_money(bet*1.5)
        print(f'Congratulations! You won ${bet*1.5}. You currently have ${player.bankroll}')
        if play_again():
            game_on=True
            clear_output()
            continue
        else:
            print('Thank you for playing '+player.name)
            break
    while not player_bust:
        if get_hit():
            player_cards.append(mydeck.deal_card().rank)
            clear_output()
            display_dealer_cards(dealer_cards)
            print('\n')
            display_player_cards(player_cards)
        else:
            break
        if card_sum(player_cards)>21:
            print('Player Bust! ')
            game_on=False
            player_bust=True
            
    if player_bust:
        player.add_money(-bet)
        print(f'You lost ${bet}. You currently have ${player.bankroll}')
        if play_again():
            game_on=True
            clear_output()
            continue
        else:
            print('Thank you for playing '+player.name)
            break
            
    dealer_cards.append(dealer_hole_card.rank)
    while not dealer_bust:
        clear_output()
        display_dealer_cards(dealer_cards)
        print('\n')
        display_player_cards(player_cards)
        if card_sum(dealer_cards)>21:
            print('Dealer Bust! ')
            game_on=False
            dealer_bust=True
            break 
        elif card_sum(dealer_cards)>card_sum(player_cards):
            break
        else: 
            dealer_cards.append(mydeck.deal_card().rank)
    if dealer_bust:
        player.add_money(bet)
        print(f'Congratulations! You won ${bet}. You currently have ${player.bankroll}')
        if play_again():
            game_on=True
            clear_output()
            continue
        else:
            print('Thank you for playing '+player.name)
            break
    else:
        print('Dealer wins')
        player.add_money(-bet)
        print(f'Your current bankroll is {player.bankroll}')
        if player.bankroll==0:
            print(f'You ran out of money :( Better luck next time {player.name}')
            break
        elif play_again():
            game_on=True
            clear_output()
            continue
        else:
            print('Thank you for playing '+player.name+'!')
            break 
    
    print('end of round')
    


# In[ ]:




