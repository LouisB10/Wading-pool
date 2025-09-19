import turtle

turtle.reset()

for _ in range(4):
    turtle.forward(100)  
    turtle.left(90)     

turtle.done()

# On importe le module turtle
# On utilise reset() au cas où il y aurait déja des dessins
# On fait une boucle de range(4) pour faire notre carré
# Avancer de 100 et tourner à gauche à 90 degrés
# On finit le dessin avec done()