import turtle

toto = turtle.Screen()
toto.bgcolor("black")
titi = turtle.Turtle()
titi.color("red")
for i in range(3):
    titi.right(90)
    titi.circle(42)
toto.exitonclick()

# On crée une fenêtre graphique (un "écran") où le dessin aura lieu. Ici, cette fenêtre est assignée à la variable toto
# Définit la couleur de fond de l'écran en noir.
# Crée une "tortue", un curseur qui se déplace et dessine sur l'écran. Ici, elle est assignée à la variable titi.
# Définit la couleur de dessin de la tortue en rouge
#  La boucle s'exécute 3 fois.
# À chaque itération, la tortue tourne de 90 degrés vers la droite.
# La tortue dessine un cercle de rayon 42 pixels. Le centre du cercle est à gauche de la tortue (par défaut).
# La tortue dessine 3 cercles rouges, en tournant de 90 degrés entre chaque cercle. Cela crée une forme en "trèfle" ou en "spirale" selon l'angle de vue.
# La fenêtre reste ouverte jusqu'à ce que l'utilisateur clique dessus pour la fermer.