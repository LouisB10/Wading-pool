first_names = [" Jackie " , " Chuck " , " Arnold " , " Sylvester "]
last_names = [" Stallone " , " Schwarzenegger " , " Norris " , " Chan "]
magic = [* zip ( first_names , last_names [:: -1]) ]
print ( magic [0])
print ( magic [3])
print ( magic [1][0])
print ( magic [0][1])
print ( magic [2])

# on définit 2 listes qui contiennent des prénoms et des noms 
# notre variable magic attends un index en entrée, il va prendre les prénoms en partant du début et les noms de familles
# en partant de la fin avec le slice -1