import turtle 
import time
import random

WIDTH, HEIGHT = 500, 500
COLOURS = ["red", "blue", "green", "orange", "purple", "black", "pink", "yellow", "cyan", "grey"]

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers ( 2 - 10 ):  ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter a valid input. Try Again!")
            continue
            
        if 2 <= racers <= 10:
            return racers 
        else:
            print("Please enter the number of the racers between ( 2 -20 ).")  
            continue
        
def race(colours):
    turtles = create_turtles(colours)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 -10:
                return colours[turtles.index(racer)]
          
def create_turtles(colours):
    turtles =[]
    spacingx = WIDTH // (len(colours) + 1)
    for i, colour in enumerate(colours):   
        racer = turtle.Turtle()
        racer.color(colour)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20 )
        racer.pendown()
        turtles.append(racer)    
    return turtles 
    
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")  
          
racers = get_number_of_racers()
init_turtle()
random.shuffle(COLOURS)
colours = COLOURS[:racers] 

winner = race(colours)
print("The Winner is the turtle with the colour:", winner)
time.sleep(5)




              
            
       