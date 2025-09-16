import random


def looser(n):
    if n >= 12:
        print("You loose!")


def rdm_set():
    sete = {1, 2, 3, 4, 5, 6}
    print(random.sample(sorted(sete), k=1))


rdm_set()
