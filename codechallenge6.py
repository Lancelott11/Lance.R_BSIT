g = 1 
for x in range (1, 6) :
    for y in range (x) :
        print(g, end="  ")
        g += 1
    print()
p = int(input("How many rows?"))
g = 1 
for x in range (1, p + 1) :
    for y in range (x) :
        print(g, end="  ")
        g += 1
    print()