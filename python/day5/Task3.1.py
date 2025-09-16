import re
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
s = input("type a string : ")
n = int(input("type an integer : "))
c = 0

def funA(s,n):
    if len(s) - n >= 0 :
        return True
    return False

def funB(s,n):
    regex = re.findall('[@_!#$%^&*()<>?/|}{~:]',s)
    c = len(regex)
    if c >= n:
        return True
    return False

def funC(s,n):
    regex = re.findall('^[0-9]$',s)
    c = len(regex)
    if c >= n:
        return True
    return False



# print(funA(s,n))
# print(funB(s,n))
# print(funC(s,n))
