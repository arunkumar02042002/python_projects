"""COLOUR CHOICES GAME(CCG)
This Game will take input from the user and compare it with the computer choice and will return the score.
"""

# Importing Ramdom Module which is Required for this game.
import random

# Intial Scores
Your_score = 0
computer_score = 0

# Giving choices
choices = ["Red", "Yellow", "Green", "Blue", "White", "Black"]

# This loop will keep executing until player exit the game
while True:

    #computer choosing it's colour
    computer_col = random.choice(choices)

    print("Choose your colour :\nPress 1 for Red\nPress 2 for Yellow\nPress 3 for Green\nPress 4 for Blue\nPress 5 for White\nPress 6 for Black")
    
    #Taking input from the user
    player_choice = input("Enter your choice : ")
    
    # This method will help in ignoring the error and will proctect from crash
    try:
        player_choice = int(player_choice)
        print("Choose correct option")
        #If user enters which is not btw 0 to 5 or enters a wrong input (or if user's input in list index out of range or enters a wrong input) then it will take input again
        while player_choice > 6 or player_choice < 1:
            player_choice = int(input("Enter your choice again : "))

    except:
        print("Choose correct option")
        player_choice = input("Enter Your Choice : ")
        while player_choice not in ['0','1','2','3','4','5']:
            player_choice = input("Enter Your Choice : ")
        player_choice = int(player_choice)

    # Checks the input enter by player and will compare and give a colour which satisfies the condition
        if player_choice == 1:
            player_col = choices[0]
        elif player_choice == 2:
            player_col = choices[1]
        elif player_choice == 3:
            player_col = choices[2]
        elif player_choice == 4:
            player_col = choices[3]
        elif player_choice == 5:
            player_col = choices[4]
        else:
            player_col = choices[5]

    #Comparing the colour giving score sccordingly
    if computer_col == player_col:
        Your_score += 1
    else:
        computer_score += 1
    
    print(f"Computer Choosed : {computer_col}")
    print(f"You Choosed : {player_col}")
    print(f"Your Score = {Your_score}")
    print(f"Computer Score = {computer_score}")

    # This will check the player wants to play again or not
    next_input = input("Press Y to play again or press N to exit the game")
    if next_input == "N" or next_input == 'n':
        print(f"Computer Score = {computer_score}")
        print(f"Your Score = {Your_score}")
        if computer_score > Your_score:
            print("Computer Won!")
        elif computer_score == Your_score:
            print("Game Tied!")
        else:
            print("Hurrah! You Won!")
        print("Thanks for playing")
        break
