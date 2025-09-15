n = int(input("Veuillez renseigner un entier : "))
for i in range(2, n // 2 + 1, +1):
    for j in range(n - 1, 1, -1):
        if j % i == 0:
            print(j, end=" ")
    print("")

# initialisation de n un entier
# 1ere boucle qui itère sur i entre 2 et n // 2 +1
# 2eme boucle qui itère sur j entre n - 1 et 1 en partant du plus grand (-1)
# si j modulo i égal 0 alors on affiche j et on va à la ligne
