my_first_list = [4 , 5, 6]
my_second_list = [1 , 2, 3]
my_first_list . extend ( my_second_list )
print(my_first_list)
# On initialise 2 liste différente qui contiennent des entiers
# Puis on fait un .extend qui va permettre de "fusionner" nos 2 listes en 1 seule

my_first_list = [7 , 8, 9]
my_second_list = [4 , 5, 6]
my_first_list = [* my_first_list , * my_second_list ]
print(my_first_list)
# On initialise 2 liste différente qui contiennent des entiers
# Puis on fait une fusion de nos listes en 1