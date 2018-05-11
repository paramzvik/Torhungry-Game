#Import turtle libraby
import turtle as tu
import math as m
import random as rd

#Set up screen
wn = tu.Screen()
wn.bgcolor("lightgreen")
wn.tracer(4)

#Draw border
mypen = tu.Turtle()
mypen.shape("arrow")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(5):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Create player Turtle
player = tu.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)

#Create the score variable
score = 0

#Create goals
maxGoals = 8
goals = []
for count in range(maxGoals):
    goals.append(tu.Turtle())
    goals[count].color("brown")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(rd.randint(-300, 300), rd.randint(-300, 300))

#Set speed variable
speed = 1

#Define functions here

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def incspeed():
    global speed
    speed += 1

def decspeed():
    global speed
    speed -= 1

def iscollison(t1, t2):
    d = m.sqrt(m.pow(t1.xcor()-t2.xcor(), 2)+m.pow(t1.ycor()-t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False
        
#Set keyboar bindings
tu.listen()
tu.onkey(turnleft, "Left")
tu.onkey(turnright, "Right")
tu.onkey(incspeed, "Up")
tu.onkey(decspeed, "Down")

while True:
    player.forward(speed)
    #Boundary Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
    

#Move the goal
    for count in range(maxGoals):

#Collosion Avoiding
        goals[count].forward(3)
        if goals[count].xcor() > 300 or goals[count].xcor() < -300:
            goals[count].right(180)
        if goals[count].ycor() > 300or goals[count].ycor() < -300:
            goals[count].right(180)
        if iscollison(player, goals[count]):
            goals[count].setposition(rd.randint(-300,300), rd.randint(-300,300))
            goals[count].right(rd.randint(0, 360))
            score+=1
            #Draw the score on screen
            mypen.undo()
            mypen.penup()
            mypen.ht()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align="left", font=("Arial",14, "normal"))

delay = input("Press Enter to exit")

