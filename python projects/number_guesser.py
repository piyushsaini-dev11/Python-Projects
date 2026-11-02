import random

top_of_range = input("type a number:  ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <=0:
        print("please enter a number larger than 0")
        quit()
        
else:
    print("please enter a number next time")       
    quit()
    
random_number = random.randint(0,top_of_range)     
guesses = 0

while True:
    guesses += 1
    
    guess_number = input("Make a guess:  ")
    
    if guess_number.isdigit():
         guess_number = int(guess_number)
    else:
        print("type a number next time!")
        continue
        
    if guess_number == random_number:
        print("You got it!")
        break
    
    elif guess_number > random_number:
        print("Your guess is above the number")   
    else:
        print("Your guess is below the number")
        
print("You got it in", guesses, "guesses")             
        
                 

    
    
        