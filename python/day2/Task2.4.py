p = "abcdefghij"
print (p [:: -2][:5][:: -1][3:])

#on définit p avec des char / lettres
#on print le p avec 4 slices différents
#quand il y a plusieurs slices, ceux qui suivent le 1er vont slices dans le meme array que le 1er
#[::-2] en partant de la fin et print une lettre sur 2 : jhfdb
#[:5] = [0:5] on prend de la 1ere a la 5eme lettre : jhfdb
#[::-1] en partant de la fin et print une lettre sur 1 : bdfhj
#[3:] on part de la 4eme lettre jusqu'à la fin de la string : hj