import time
import random
start = time.time()
n = 1000000
liste = [random.randint(1, 1000000) for _ in range(n)]
liste.sort()
print(liste)
print(time.time()- start)