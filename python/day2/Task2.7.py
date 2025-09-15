print("hello"+42)
#pour débug on execute d'abord notre programme, il nous indique une TypeError : can only concatenate str (not "int") to str
#ce qui veut dire simplement que on ne peut pas afficher notre 42 de cette façon, 
#on devra plutot le mettre en chaine de charactere lui aussi et pas en int avec le + et sans ""
print("hello"+"42")