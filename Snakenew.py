import turtle #Turtle ist ein Graphikmodul, welches gesteuerte Pfade, die mit der "Turtle" zurück gelegt werden visualisiert und dem Nutzer somit ermöglicht, sich frei auf der Zeichenfläche zu bewegen.
import time #Zeitbezogene Funktionen importieren
import random #importiert die zufallsfunktion
turtle.colormode(255) #Farbmodus in RGB 

delay = 0.1 #zeitlicher Abstand zwischen den Aktualisierungen (Geschwindigkeit)

# Score und Punkte auf 0 setzen
punkte = 0
rekord = 0

#Grafikfenster einstellen (Farbe, Titel, Größe...)
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor(154, 195, 97)
wn.setup(width=800, height=600)
wn.tracer(0) # keine screen updates

#Schlangenkopf (Turtle/erstes Segment) 
head = turtle.Turtle() #erstellt ein Objekt in Turtle, welches wir head nennen
head.shape("turtle") #Setzt den Kopf als Schildkrötensymbol aus der Library fest
head.color(45, 78, 0)
head.penup() #verhindert die Aufzeichnung der Pfade (Stift wird nicht aufgesetzt)
head.goto(0,0) #Startposition festlegen
head.setheading(90) #Da unsere Turtle nicht rotationssymetrisch ist, wird sie zu beginn nach oben ausgerichtet
head.direction = "stop" #Sie soll sich erst bewegen sobald der Spieler die erste Bewegungsrichtung vorgibt

# Setzt Form, Farbe, erste Position... des Futters
food = turtle.Turtle() 
food.shape("turtle")
food.color(104, 98, 29)
food.tilt(90)
food.penup()
food.goto(0,100) 

segments = [] #Liste der Körperelemente

# Eigenschaften der Schrift
pen = turtle.Turtle()
pen.shape("square")
pen.color(45, 78, 0)
pen.penup()
pen.hideturtle() 
pen.goto(0, -260)
pen.write("Punkte: 0     Rekord: 0", align="center", font=("Courier", 24, "normal"))

# Funktionen für die Bewegung der Turtle
def go_up():
    if head.direction != "down": #verhindert Wenden auf der Stelle
        head.direction = "up" #Festlegung der Bewegungsrichtung
        head.setheading(90) #Ausrichtung des Kopfelementes bei Pfeiltaste oben
        
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

def move(): #Änderung der Position
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

#Tastenerkennung
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#Hauptschleife des Spiels
while True:
    wn.update()

    #Überprüft auf Kollision mit Rand des Grafikfensters und setzt die Turtle auf Anfangsposition
    if head.xcor()>370 or head.xcor()<-380 or head.ycor()>290 or head.ycor()<-270:
        time.sleep(0.5)
        head.goto(0,0)
        head.setheading(90)
        head.direction = "stop"

        # Bereits gesammelte Körperelemente werden außerhalb des Grafikfensters versteckt
        for segment in segments:
            segment.goto(1000, 1000)
        
        segments.clear() #Liste der Körperelemente wird gelöscht

        #Setzt alles auf Anfangsparameter (bis auf Rekord)
        punkte = 0
        
        delay = 0.1

        pen.clear()
        pen.write("Punkte: {}     Rekord: {}".format(punkte, rekord), align="center", font=("Courier", 24, "normal")) 


    # Überprüft kollision mit Futterelement
    if head.distance(food) < 20:
        # bewegt Futterelement zu einem zufälligem Punkt innerhalb des Spielfeldes
        x = random.randint(-380, 370)
        y = random.randint(-270, 280)
        food.goto(x,y)

        # definiert Form und Farbe der Körperelemente
        new_segment = turtle.Turtle()
        new_segment.shape("circle")
        new_segment.color(76, 117, 19)
        new_segment.penup()
        segments.append(new_segment) #Funktion für erscheinen der neuen Körperelemente

        # Bei einsammeln eines Futterelemtes, wird die geschwindigkeit...
        delay -= 0.001 

        #... und der Punktestand um eins erhöht
        punkte += 1

        if punkte > rekord: #Wird der Rekord übertroffen wird dieser Punktestand als neuer Rekord angezeigt
            rekord = punkte
        
        pen.clear()
        pen.write("Punkte: {}     Rekord: {}".format(punkte, rekord), align="center", font=("Courier", 24, "normal")) 

    # Bewirkt, dass die Körperelemente wärend der Bewegung der Schlange die Position des jeweils vorherigen annehmen
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Bewegt das erste Element aus der Segmenten Liste auf die ehemalige Position des Kopfes
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Überprüft kollision des Kopfes mit Körperelementen und setzt wie oben beschrieben auf Anfangsparameter zurück (gleiches Vorgehen wie bei Kollision mit Rand)
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.setheading(90)
            head.direction = "stop"
            
        
            for segment in segments:
                segment.goto(1000, 1000)
        
            segments.clear()
            
            punkte = 0

            delay = 0.1
     
            pen.clear()
            pen.write("Punkte: {}     Rekord: {}".format(punkte, rekord), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
