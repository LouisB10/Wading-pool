num1 = 12.24
num2 = 424242.8412

# On les passe en chaîne de caractères
num1_str = str(num1)
num2_str = str(num2)

# Extraire la partie entière en utilisant split()
partie_entiere1 = num1_str.split('.')[0]  
partie_entiere2 = num2_str.split('.')[0]

print(f"Partie entière de {num1} : {partie_entiere1}")
print(f"Partie entière de {num2} : {partie_entiere2}")


