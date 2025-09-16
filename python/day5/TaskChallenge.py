import time
start = time.time()
res = 1

def power (base, exponent):
    if exponent > 1:
        return base * power(base, exponent -1)
    else :
        return res

print(power(42,84))
print(power(42,168))
print(time.time()- start) 