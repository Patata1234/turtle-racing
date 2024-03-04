import turtle
import random
import time

WIDTH, HEIGHT = 500, 500

COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racerss():
    racerss = 0
    while True:
        racerss = input("Type the number of racerss (2 - 10): ")
        if racerss.isdigit():
            racerss = int(racerss)
        else:   
            print("Type a number next time.")
            continue
    
        if 2 <= racerss <= 10:
            return racerss
        else:
            print("Input out of range 2 - 10. Try again!")

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH// (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) *spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,10)
            racer.forward(distance)
            
            x,y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
                

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing.')        

racers = get_number_of_racerss()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f"The winner is {winner} turtle! ")
time.sleep(10)