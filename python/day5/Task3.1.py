import re
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
s = input("type a string : ")
n = int(input("type an integer : "))

def funA(s,n):
    if len(s) - n >= 0 :
        return True
    return False

def funB(s,n):
    if len(s) - n >= 0 :
        return True
    return False

def funC(s,n):
    if s.isalpha()  :
        return True
    return False



# print(funA(s,n))
print(funC(s,n))