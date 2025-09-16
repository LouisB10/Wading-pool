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


while True:
    try:
        n = int(input("How many sandwiches do u want ? : "))
        break
    except ValueError:
        print("I can't do this!")


def preparesandwich(n):
    for i in range(0, n):
        sandwich()


preparesandwich(n)

# Boucle pour demander à l'utilisateur le nombre de sandwiches souhaités
# et vérifier que l'entrée est un nombre entier valide
# Si l'entrée est valide, on sort de la boucle avec le break
# Message d'erreur si l'entrée n'est pas un nombre

# Fonction pour préparer plusieurs sandwiches "prepapresandwich(n)""
# Boucle pour créer 'n' sandwiches
# Appelle la fonction sandwich() pour chaque itération
# Appelle la fonction preparesandwich avec le nombre de sandwiches souhaités
