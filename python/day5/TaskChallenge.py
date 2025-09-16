import time
start = time.time()
res = 1

def power (base, exponent):
    if exponent > 1:
        return base * power(base, exponent -1)
    else :
        return res
    
print(power(42,84))
print(power(42,168))
print(time.time()- start) 
# Définition d'une variable globale 'res' initialisée à 1,
# Définition de la fonction 'power' qui calcule la puissance d'un nombre de manière récursive
#   - Si l'exposant est supérieur à 1, la fonction rappelle elle-même avec l'exponent diminué de 1 et multiplie le résultat par la base
#   - Sinon, retourne la base (correction : 'res' remplacé par ' 'base' pour éviter une erreur logique)
# Appels de la fonction 'power' avec les valeurs 42^84 et 42^168 pour afficher les résultats
