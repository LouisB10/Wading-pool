import random

num = random.randint(1, 100)

is_odd = (num % 2) 

print(f"Le nombre {num} est {'impair' if is_odd else 'pair'}")