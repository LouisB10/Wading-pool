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
    if funct(s,n):
        return True
    return False

print(passcheck(funA, 16, "mysecretpassword"))
print(passcheck(funB, 3, "mysecretpassword"))
print(passcheck(funC, 1, "mysecretpassword"))

print(passcheck(funA, 16, "mysecretpassword%*$5"))
print(passcheck(funB, 3, "mysecretpassword%*$4"))
print(passcheck(funC, 1, "mysecretpassword%*$4"))