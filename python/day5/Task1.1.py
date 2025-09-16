def f1 () :
    return 42
def f2 (x):
    return 2 * x
print ( f1 () )
print ( f2 (5) + f1 () ) 
# On définit une fonction f1 qui n'attend aucune valeur d'entrée, elle retourne 42 dans tout les cas
# On définit une fonction f2 qui attend une valeur de x en entrée et qui retourne le double 2 * x
# Le premier print renvoie 42 et le deuxieme 10 + 42 donc 52