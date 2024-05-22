
import ColabTurtlePlus.Turtle as turtle
import random
import math

# GLOBAL CONSTANTS
MAXSTEP = 20      # maximum step size for the turtles to move
BOUNDARY = 100    # the race boundary (i.e. radius of the circle)

# draw a circle
def draw_circle(radius):
    local_turtle = turtle.Turtle()
    local_turtle.penup()
    local_turtle.goto(0, -radius)
    local_turtle.pendown()
    local_turtle.circle(radius)
    local_turtle.hideturtle()

# make turtle step
def step(t):
    angle = random.randint(0, 360)
    distance = random.randint(0, MAXSTEP)
    t.setheading(angle)
    t.forward(distance)

# get the distance of the turtle from the center
def distance(t):
    x, y = t.pos()
    return math.sqrt(x**2 + y**2)

# check if the turtle is in bound
def inBound(t):
    return distance(t) < BOUNDARY

# check whois further away from (0,0)
def farthest(t1, t2):
    if distance(t1) > distance(t2):
        return t1
    else:
        return t2

# race two turtles
def main():
    # Draw the race boundary
    draw_circle(BOUNDARY)

    # Create two turtle objects with different colors
    turtle1 = turtle.Turtle()
    turtle1.shape("turtle")
    turtle1.color("red")
    turtle1.penup()
    turtle1.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))

    turtle2 = turtle.Turtle()
    turtle2.shape("turtle")
    turtle2.color("blue")
    turtle2.penup()
    turtle2.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))

    
    race_on = True

    while race_on:
        step(turtle1)
        step(turtle2)

        if not inBound(turtle1):
            print(f"{turtle1.pencolor().capitalize()} turtle wins!")
            race_on = False
        elif not inBound(turtle2):
            print(f"{turtle2.pencolor().capitalize()} turtle wins!")
            race_on = False

# Run the main function
turtle.clearscreen()
main()
