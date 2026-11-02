import random

options = ["rock", "paper", "scissors"]

user_win = 0
computer_win = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or 'Q' to quit:  ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Select a correct option")
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]  
    print("Computer Picked", computer_pick + ".")  
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_win+=1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_win+=1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")   
        user_win+=1  
                 
    else:
        print("You Lost!")
        computer_win+=1
        
print("You Won", user_win, "times!")      
print("Computer Won", computer_win, "times!")
print("Thanks For Playing.")  