for x in range (5) :
    for y in range (5) :
        if x + y == 4 or x == y :
            print("*", end=" ")
        else :
            print(" ", end=" ")
    print()
p = int(input("Input size of x "))
for x in range (p) :
    for y in range (p) :
        if x + y == p-1 or x == y :
            print("*", end=" ")
        else :
            print(" ", end=" ")
    print()