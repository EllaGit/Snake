import turtle #Grafikmodul importieren
import time #Zeitbezogene Funktionen importieren
import random #importiert die zufallsfunktion
turtle.colormode(255) #

delay = 0.1 

# Score auf 0 setzen
punkte = 0
rekord = 0

# Benutzeroberfläche einstellen (Farbe, Titel, Größe...)
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor(154, 195, 97)
wn.setup(width=800, height=600)
wn.tracer(0) # keine screen updates

#Schlangenkopf(erstes Segment) 
head = turtle.Turtle()

head.shape("turtle") #Das Kopfelement 
head.color(45, 78, 0)
head.penup() #
head.goto(0,0)
head.setheading(90)
head.direction = "stop"

# Schlangen Futter
food = turtle.Turtle()
food.shape("turtle")
food.color(104, 98, 29)
food.tilt(90)
food.penup()
food.goto(0,100)

segments = []

# Schrift
pen = turtle.Turtle()
pen.shape("square")
pen.color(45, 78, 0)
pen.penup()
pen.hideturtle()
pen.goto(0, -260)
pen.write("Punkte: 0     Rekord: 0", align="center", font=("Courier", 24, "normal"))

# Funktionen
def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.setheading(90)
        
def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.setheading(270)

def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.setheading(180)

def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.setheading(0)

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>370 or head.xcor()<-380 or head.ycor()>290 or head.ycor()<-270:
        time.sleep(0.5)
        head.goto(0,0)
        head.setheading(90)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Punkte: {}     Rekord: {}".format(punkte, rekord), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-380, 370)
        y = random.randint(-270, 280)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.shape("circle")
        new_segment.color(76, 117, 19)
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        punkte += 1

        if punkte > rekord:
            rekord = punkte
        
        pen.clear()
        pen.write("Punkte: {}     Rekord: {}".format(punkte, rekord), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.setheading(90)
            head.direction = "stop"
            
            #head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            punkte = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Punkte: {}     Rekord: {}".format(punkte, rekord), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
