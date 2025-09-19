import turtle

def draw_spiral():

    screen = turtle.Screen()
    screen.bgcolor("white")
    pen = turtle.Turtle()

    for i in range(100):
        pen.forward(i * 2) 
        pen.left(30)         

    screen.exitonclick()

draw_spiral()

# Initialisation de l'écran et de la tortue
# boucle qui itere 100 fois 
# Augmente la longueur du segment à chaque itération
# Tourne de 30 degrés à gauche