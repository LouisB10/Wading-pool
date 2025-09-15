p = "abcdefghij"
print (p [:: -2][:5][:: -1][3:])

#version simplifiée
print (p [:: -2][:: -1][3:])
#on enleve le [:5] car il ne sert à rien dans notre cas, avec le premier slice 
#on récupère seulement 5 char donc l'étape d'après ne sert à rien 
#car elle est sensé récupérer les 5 premiers char qui sont les mêmes que après le premier slice : jhfdb

#2eme version simplifiée
print(p[7::2])
#on connait notre résultat final qui est : hj donc on compte combien de charactères il y a avant le h
#ce qui donne 7 pour la premiere partie du slice, on ne va pas indiquer de fin car la lettre j est à la fin de la chaine
#pour finir notre step doit etre de 2 car entre le h et le j il y a une lettre
