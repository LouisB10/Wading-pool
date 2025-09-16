import re
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
# s = input("type a string : ")
# n = int(input("type an integer : "))

def funA(s,n):
    if len(s) >= n :
        return True
    return False

def funB(s,n):
    if len(re.findall(r"[!@#$%^&*()_+{}\[\]:;<>,.?\\/-]", s)) >= n:
        return True
    return False

def funC(s,n):
    if len(re.findall(r"[0123456789]", s)) >= n:
        return True
    return False

def passcheck(funct,n,s):
    if isinstance(n, int) and isinstance(s, str) and callable(funct):
        if funct(s,n):
            return True
        return False
    return "Type error : verify parameter of passcheck function"

print(passcheck(funA, 16, "mysecretpassword"))
print(passcheck(funB, 3, "mysecretpassword"))
print(passcheck(funC, 1, "mysecretpassword"))

print(passcheck(funA, 16, "mysecretpassword%*$5"))
print(passcheck(funB, 3, "mysecretpassword%*$4"))
print(passcheck(funC, 1, "mysecretpassword@*$4"))

print(passcheck(5, 2, "mysecretpassword@!0$5"))
print(passcheck(funC, funA, "mysecretpassword@!0$5"))
print(passcheck(funC, 4, 7))