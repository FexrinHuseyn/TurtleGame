import turtle
import random

# Write Setting
Pen_1=turtle.Turtle()
Pen_1.color("#4B0366")
Pen_1.hideturtle()
Pen_1.penup()
Pen_1.goto(0,300)
Pen_1.write("Turtle Game",move=False,align="center",font=("Comic Sans MS", 50, "normal"))
Pen_1.color("#000000")
Pen_1.goto(0,250)
Pen_1.write("Catch the Turtle",False,align="center",font=("Comic Sans MS", 25, "normal"))



#screen settings
screen= turtle.Screen()
screen.bgcolor("#FAAAF8")
screen.title("Catch The Turtle")
FONT= ("Comic Sans MS", 25 ,"normal")
grid_size=10
score=0
gameover=False

#turtlelist
turtlelist=[]

#countdownturtle
countdownturtle=turtle.Turtle()

#make turtle properties
x_cord=[-20,-10,0,10,20]
y_cord=[20,10,0,-10]

#SOCRETURTLE
scoreturtle=turtle.Turtle()


def setup_scroreturtle():
    scoreturtle.hideturtle()
    scoreturtle.color("white")
    scoreturtle.penup()

    scoreturtle.setpos(-350,325)
    scoreturtle.write(arg= "Score : 0", move=False, align="left", font=("Comic Sans MS", 25 ,"normal"))

def maketurtle(x,y):
    t= turtle.Turtle()

    def handleclick(x,y):
        global score
        score+=1
        scoreturtle.clear()
        scoreturtle.write(arg=f"Score : {score}", move=False, align="left", font=FONT)
        print(x,y)


    t.onclick(handleclick)
    t.penup()
    t.shape("circle")
    t.shapesize(3)
    t.color("#E336F4")
    t.goto(x*grid_size,y*grid_size)
    turtlelist.append(t)

def setup_turtles():

    for x in x_cord:
         for y in y_cord:
            maketurtle(x,y)

def hideturtle():
    for t in turtlelist:
        t.hideturtle()

#recursive function
def showturtlerandom():
    if not gameover:
        hideturtle()
        random.choice(turtlelist).showturtle()
        screen.ontimer(showturtlerandom,1000)

def countdown(time):
    global gameover
    countdownturtle.hideturtle()
    countdownturtle.color("#660D6F")
    countdownturtle.penup()

    countdownturtle.setpos(-350, 275)
    countdownturtle.clear()

    if time>0:
        countdownturtle.clear()
        countdownturtle.write(arg=f"Time: {time}", move=False, align="left", font=FONT)
        screen.ontimer(lambda: countdown(time-1),1000)
    else:
        gameover=True
        countdownturtle.clear()
        hideturtle()
        countdownturtle.write(arg="Game Over!", move=False, align="left", font=FONT)


def startgame():
    turtle.tracer(0)

    setup_scroreturtle()
    setup_turtles()
    hideturtle()
    showturtlerandom()
    countdown(15)
    turtle.tracer(1)


startgame()
turtle.mainloop()

