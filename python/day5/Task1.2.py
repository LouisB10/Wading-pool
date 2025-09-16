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


sandwich()

# Avec nos 4 fonctions qui correspondent aux 4 parties du sandwich
# Nous pouvons les utiliser dans une nouvelle fonction qui va
# Simplement appeler dans l'ordre de l'énoncé les différentes parties du sandwich
