print("Enter a sentence")
x = input()
liste = x.split()
res = ""
for i in liste:
    res += i[0]
print(res)

#on demande à l'user de renseigner une phrase
#on initialise une variable x qui recupère l'input donc la phrase
#on définit notre liste qui correspond à la phrase du user passé par la fonction split qui récupère chaque mot dans une phrase
#on initialise une variable res avec une chaine de caractère vide qui servira pour notre print final du resultat
#on créé une boucle for qui va parcourir la liste de mot, on ajoute au fur et à mesure les premières lettres de chaque mots grace à i[0],
#i correspond à un mot dans ma liste
#pour finir on print le resultat 
# res+= i[0] res = res i[0]