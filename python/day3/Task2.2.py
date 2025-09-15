str = list(input("String : "))
res = ""
for i in str:
    res += i[0] * 2
print(res)

# on initialise str qui est une chaine de caractère passé dans list()
# on initialise res comme une chaine de caractère vide
# boucle for qui parcourt str et qui ajoute à chaque fois la première lettre 2 fois
