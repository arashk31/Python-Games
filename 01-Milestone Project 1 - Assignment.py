#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Milestone Project 1
# ## Congratulations on making it to your first milestone!
# You've already learned a ton and are ready to work on a real project.
# 
# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.
# 
# Here are the requirements:
# 
# * 2 players should be able to play the game (both sitting at the same computer)
# * The board should be printed out every time a player makes a move
# * You should be able to accept input of the player position and then place a symbol on the board
# 
# Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python" otherwise you won't learn anything!) Keep in mind that this project can take anywhere between several hours to several days.
# 
# There are 4 Jupyter Notebooks related to this assignment:
# 
# * This Assignment Notebook
# * A "Walkthrough Steps Workbook" Notebook
# * A "Complete Walkthrough Solution" Notebook
# * An "Advanced Solution" Notebook
# 
# I encourage you to just try to start the project on your own without referencing any of the notebooks. If you get stuck, check out the next lecture which is a text lecture with helpful hints and steps. If you're still stuck after that, then check out the Walkthrough Steps Workbook, which breaks up the project in steps for you to solve. Still stuck? Then check out the Complete Walkthrough Solution video for more help on approaching the project!

# There are parts of this that will be a struggle...and that is good! I have complete faith that if you have made it this far through the course you have all the tools and knowledge to tackle this project. Remember, it's totally open book, so take your time, do a little research, and remember:
# 
# ## HAVE FUN!

# In[1]:


from IPython.display import clear_output


# In[2]:


def display_board(game_list):
    clear_output()
    print('   |   |   ')
    print(f' {game_list[6]} | {game_list[7]} | {game_list[8]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {game_list[3]} | {game_list[4]} | {game_list[5]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {game_list[0]} | {game_list[1]} | {game_list[2]} ')
    print('   |   |   ')
     
        


# In[3]:


mylist=['O','X','X','O',' ',' ','O',' ','X']
mylist.count('O')


# In[4]:


display_board(mylist)
if input('Clear Screen?')=='Y':
    clear_output()


# In[5]:


def check_winner(game_list):
    if game_list.count('X')<3:
        return False
    if game_list.count(' ')==0:
        print('TIED GAME!!')
        return True
    for i in range(0,7,3):
        if game_list[i]==game_list[i+1] and game_list[i]==game_list[i+2] and game_list[i]!=' ':
            print('WINNER WINNER CHICKEN DINNER')
            return True 
    for i in range(0,3):
        if game_list[i]==game_list[i+3] and game_list[i]==game_list[i+6] and game_list[i]!=' ':
            print('WINNER WINNER CHICKEN DINNER')
            return True 
    if game_list[0]==game_list[4] and game_list[0]==game_list[8] and game_list[i]!=' ':
            print('WINNER WINNER CHICKEN DINNER')
            return True 
    if game_list[2]==game_list[4] and game_list[2]==game_list[6] and game_list[i]!=' ':
            print('WINNER WINNER CHICKEN DINNER')
            return True 
    return False


# In[6]:


check_winner(mylist)


# In[7]:


def update_list(game_list,index, player):
    if player==1:
        game_list[index]='X'
    else: 
        game_list[index]='O'
    return game_list


# In[8]:


update_list(mylist, 1, 2)


# In[9]:


def user_choice(game_list,player):
    '''
    User inputs a number (0-10) and we return this in integer form.
    No parameter is passed when calling this function.
    '''
    
    choice = 'Initialize'
    
    while not choice.isdigit() or int(choice) not in range(1,10) or game_list[int(choice)-1]!=' ':
            choice = input(f"Player {player}, choose your position (1-9):")
            
            if not choice.isdigit() or int(choice) not in range(1,10):
                print("Sorry, that input is invalid :(\n")
            elif game_list[int(choice)-1]!=' ':
                print("Sorry, that space is already filled :(\n")
    
    return int(choice)-1


# In[10]:


user_choice(2)


# In[11]:


def new_game():
    
    choice = 'Initialize'
    
    while choice not in ['Y','N']:
        choice = input("Would you like to play again? (Y or N):")
        clear_output()
        if choice not in ['Y','N']:
            print("Sorry, I don't understand. Please choose Y or N.")
        
    
    return choice=='Y'


# In[12]:


new_game()


# In[13]:


play_game= True 
game_list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
while play_game:
    
    #display the board
    display_board(game_list)
    
    #check for winner
    if check_winner(game_list):
        play_game=new_game() 
        if play_game:
            game_list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
            continue
        else:
            break
            
    #ask player 1 for input
    index=user_choice(game_list,1)
    
    #update the list
    game_list=update_list(game_list,index,1)
    
    #display the board
    display_board(game_list)
    
    #check for winner
    if check_winner(game_list):
        play_game=new_game() 
        if play_game:
            game_list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
            continue
        else:
            break
        
    
    #ask player 2 for input
    index=user_choice(game_list,2)
    
    #update the list
    game_list=update_list(game_list,index,2)
    


# In[ ]:


game_list


# In[ ]:




