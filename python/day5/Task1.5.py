def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print("O O O O O O")


def ham():
    print(" ============ ")


def sandwich():
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()


def vegansandwich():
    bread()
    lettuce()
    tomato()
    bread()


while True:
    try:
        n = int(input("How many sandwiches do u want ? : "))
        veg = input("Do u want vegan sandwich ? : (o/n)")
        veg.lower()
        break
    except ValueError:
        print("I can't do this!")


def preparesandwich(n, veg):
    if veg == "o":
        True
        for i in range(0, n):
            vegansandwich()
    else:
        veg != "o"
        False
        for i in range(0, n):
            sandwich()


preparesandwich(n, veg)

# On initialise une fonction pour les vegan
# Boucle pour demander à l'utilisateur le nombre de sandwiches souhaités
# On demande aussi si l'utilisateur veut un sandwich vegan avec (o/n)
# On applique .lower() si au cas où l'user rentre une majuscule
# et on vérifie que l'entrée est un nombre entier valide, si oui : on sort de la boucle avec le break
# Message d'erreur si l'entrée n'est pas un nombre

# Ajout du parametre veg à la Fonction "prepapresandwich(n, veg)""
# On rajoute donc une condition avant de rentrer dans la boucle for afin de savoir si l'user
# A bien validé le fait de vouloir un vegan ou non
# Boucle pour créer 'n' sandwiches
# Appelle la fonction sandwich() pour chaque itération
# Appelle la fonction preparesandwich avec le nombre de sandwiches souhaités
