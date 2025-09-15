x = 0  # Initialisation de la variable qui va contenir notre somme
for i in range(10000000):  # Boucle qui va de 0 à 9999999
    if i % 2 == 0:  # Si i est pair
        x += (1/(2*(i+1)-1))  # On ajoute le terme
    else:  # Si i est impair
        x -= (1/(2*(i+1)-1))  # On soustrait le terme
print(x*4)  # On multiplie par 4 pour obtenir π