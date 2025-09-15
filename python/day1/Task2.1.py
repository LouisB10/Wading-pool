# Compute the sum: 1 + 11 + 111 + ... + 111111111 (9 terms)
terms = [int('1' * i) for i in range(1, 10)]
total = sum(terms)

print("Sum:", total)
for power in range(2, 6):
    print(f"Sum^{power}:", total ** power)

#Crée une suite de nombres composés uniquement de '1' (de longueur 1 à 9)
#Calcule la somme de tous ces nombres
#Calcule et affiche cette somme élevée aux puissances 2, 3, 4 et 5