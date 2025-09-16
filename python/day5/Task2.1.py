num = int(input("Enter a number : "))


def sum_recursive(num):
    if num == 1:  # Base case
        return num
    return num + sum_recursive(num - 1)  # Recursive case


print(sum_recursive(num))

# Demande à l'utilisateur de saisir un nombre entier et le stocke dans la variable 'num'
# Définition de la fonction 'sum_recursive' qui calcule la somme des entiers de 1 à 'num' de manière récursive
#   - Cas de base : si 'num' est égal à 1, retourne 1 (arrêt de la récursion)
#   - Cas récursif : sinon, retourne 'num' additionné au résultat de 'sum_recursive(num - 1)'
# Appel de la fonction 'sum_recursive' avec la valeur saisie par l'utilisateur et affichage du résultat
# Exemple : si l'utilisateur entre 3, la fonction calcule 3 + 2 + 1 = 6
