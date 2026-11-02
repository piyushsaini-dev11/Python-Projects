print("Welcome to My Computer Quiz!")

playing = input("do you want to play? , Yes or No: "  )
if playing.lower() != "yes":
    quit()
    
print("Okay Lets Play!")    

score=0

answer = input("What Does CPU Stands For?  ")

if answer.lower() == "central processing unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
answer = input("What Does Ram Stands for?  ")    
if answer.lower() == "random access memory":
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
answer =  input("What Does ROM Stands For?  ")  
if answer.lower() == "read only memory":
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
answer = input("What Does WHO Stands For?  ")    
if answer.lower() == "world health organisation":
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
answer = input("What Does RBI Stands For?  ")    
if answer.lower() == "reserve bank of india":
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
print("You got", str(score),"/ 5 questions correct!") 
print("You Got", (score/5)*100, "%.") 
                   
    