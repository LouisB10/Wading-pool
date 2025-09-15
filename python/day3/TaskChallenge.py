vowels = {'a', 'e', 'i', 'o', 'u','y'}
a = int(input("Int : "))
b = input("String : ")
if a >= 42 or any(char in vowels for char in b.lower()):
    print(a)
elif a == 0:
    quit()
else:
    print(b)