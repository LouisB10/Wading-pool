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

while True:
    try:
        n = int(input("How many sandwiches do u want ? : "))
        break
    except ValueError:
        print("I can't do this!")
print(n)

def preparesandwich (n):
    for i in range (0,n):
        sandwich()

preparesandwich(n)

