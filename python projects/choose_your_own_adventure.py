name = input("Type your name:  ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end, so you go left or right. Which way you go?  (left/right)  ").lower()
if answer == "left":
    answer = input("You can come to a river. You can walk around it or swim across?  (walk/swim)  ")
    
    if answer == "swim":
        print("you swam across and were eaten by an alligator, You lose!")
    elif answer =="walk":
        print("You walked out many miles and ran out of water and lost the game!")
    else:
        print("Please type a valid option.  You Lose!")    
    
    
elif answer == "right":
    answer = input("You come to a bridge it looks wobbly. Do you want yo cross it or head back?  (cross/back)  ")
    if answer == "back":
        print("You go back and lose!")
    elif answer == "cross":
        answer = input("After croosed the bridge. You met a stanger. do you want to talk to him/her or ignore him/her?  (talk/ignore)  ")
        if answer == "talk":
            print("You talked to the stanger and he/she liked you and gived you gold. You Won!")
        elif answer =="ignore":
            print("You ignored the stranger and went forward and you lost the path. You Lose!")  
        else:
            print("Please type a valid option.  You Lose!") 
                
    else:
        print("Please type a valid option.  You Lose!") 
        
else:
    print("Please type a valid option.  You Lose!") 
    
print("Thanks For Joining This Exciting Adventure", name, ".")                