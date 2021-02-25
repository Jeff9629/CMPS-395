from turtle import *
from random import randrange
from freegames import square, vector
from tkinter import *

grape = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, 10)

##change direction of snake
def change(x, y):
    aim.x = x
    aim.y = y

##determines game boundaries
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 200

##makes snake move
def move():
    head = snake[-1].copy()
    head.move(aim)

##arguments which end game, either hitting the boundary or hitting itself
##prints final score upon collision
##deleting quit line will make snake head red upon collison
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        print('Game Over! Final Score:', len(snake)-1)
        quit()
        return

    snake.append(head)

##argument for eating grapes and randomizing next grape location
    if head == grape:
        grape.x = randrange(-15, 15) * 10
        grape.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(grape.x, grape.y, 9, 'purple')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
