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


for i in range(4):
    sandwich()

# On nous demande de faire 4 sandwich, on va donc faire une boucle pour pas répeter de code
# Un simple for avec une range de 4 qui appelle
