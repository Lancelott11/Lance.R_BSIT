for x in range (1, 16) :
    for y in range (1, x) :
        print("*", end="  ")
    print(x)
for x in range (16, 0, -1) :
    for y in range (1, x) :
        print("*", end="  ")
    print(x)
    