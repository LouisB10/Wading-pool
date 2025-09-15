num = 44490320097 

# Convertir le nombre en string (chaîne de caractères)
num_str = str(num)

# Calculer la somme en convertissant chaque caractère en entier
somme = sum(int(chiffre) for chiffre in num_str)

# Afficher le résultat
print(f"La somme des chiffres de {num} est : {somme}")

# Le programme convertit le nombre en chaîne de caractères, puis parcourt chaque chiffre pour les additionner (12343565 → "12343565" → 1+2+3+4+3+5+6+5)

