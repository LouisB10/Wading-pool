import turtle

def draw_polygon(sides):
    # Initialisation de l'écran et de la tortue
    screen = turtle.Screen()
    screen.bgcolor("white")
    pen = turtle.Turtle()
    pen.color("blue")
    pen.speed(1)  # Vitesse de dessin (1 = lente, 10 = rapide)

    # Calcul de l'angle de rotation entre chaque côté
    angle = 360 / sides

    # Dessin du polygone régulier
    for _ in range(sides):
        pen.forward(100)  # Longueur de chaque côté
        pen.left(angle)   # Tourne à gauche de l'angle calculé

    # Garde la fenêtre ouverte jusqu'au clic
    screen.exitonclick()

# Exemple d'utilisation :
# draw_polygon(5)  # Dessine un pentagone régulier
draw_polygon(8)
