#JEEPNEY SIMULATOR
route = ["Terminal", "Perez Park", "Pacific Mall"]
passenger = []
seats = 6
fare = 13
total = 0

while True :
    print()
    print("Sakay:", passenger)
    print(len(passenger), "of", seats, "seat")
    print("0 option 1 Sakay  2 Priority seat  3 para po!")
    print("4 baba sa pinto  5 baba sa harap")
    print("6 seat check  7 balikan  8 exit")
    choice = input("Choice:")

    name = input("name")
    print("1. Regular")
    print("2. Student")
    print("3. Senior")
    

    if choice == "1" :
        if len(passenger) == seats:
            print("Puno na!")
        else:
            name = input("Name:  ")
            passenger.append(name)
            total = total + fare
            print(name, "boarded at the back")
            
    elif choice == "2":
        if len(passenger) == seats:
            print("Puno na!")
        else:
            name = input("Name: ")
            passenger.insert(0, name)
            total = total + fare
            print(name, "took the priority seat")

    elif choice == "3":
        name = input("who is getting off? ")
        if name in passenger:
            passenger.remove(name)
            print(name, "is not on this jeep")

    elif choice == "4":
        if len(passenger) == 0:
            print("The jeep is empty")
        else:
            left = passenger.pop()
            print(left, "got off at the door")

    elif choice == "5":
        if len(passenger) == 0:
            print("the jeep is empty")
        else:
            front = passenger.pop
            print(front, "got off at the door")

    elif choice == "6":
        for i in range(len(passenger)):
            print("Seat", i + 1, passenger[1])

    elif choice == "7":
        route,reverse()
        print("Route:", route)
