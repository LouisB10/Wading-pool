def bread () :
    print (" <////////// > ")

def lettuce () :
    print (" ~~~~~~~~~~~~ ")

def tomato () :
    print ("O O O O O O")

def ham () :
    print (" ============ ")

def sandwich():
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()

def vegansandwich():
    bread()
    lettuce()
    tomato()
    bread()

while True:
    try:
        n = int(input("How many sandwiches do u want ? : "))
        veg = input("Do u want vegan sandwich ? : (o/n)")
        veg.lower()
        break
    except ValueError:
        print("I can't do this!")
    

def preparesandwich (n, veg):
    if  veg == "o":
        True
        for i in range (0,n):
            vegansandwich()
    else:
        veg != "o" 
        False
        for i in range (0,n):
            sandwich()


preparesandwich(n,veg)

