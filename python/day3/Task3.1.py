msg = input("Clear message : ").lower()
key = int(input("Key between 1 and 25 : "))
ref = "abcdefghijklmnopqrstuvwxyz"
res = ""

for char in msg:
    if char in ref:
        index = ref.index(char)
        new_index = (index + key) % 26
        res += ref[new_index]
    else:
        res += char  

print(msg)

# Initialise une chaîne vide pour stocker le résultat chiffré
# Parcourt chaque caractère du message
# Vérifie si le caractère est une lettre de l'alphabet
# Trouve l'index du caractère dans la référence
# Calcule le nouvel index en appliquant le décalage (avec modulo 26 pour gérer le dépassement)
# Ajoute le caractère chiffré au résultat
# Si le caractère n'est pas une lettre (espace, ponctuation, etc.), il est ajouté tel quel

