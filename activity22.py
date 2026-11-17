type = ["chinita","morena", "mestiza"]
girl_type = []

while True:
    ans = input("do you like girls? --> ")

    if ans.lower() == "yes" :
        print("what is your type? -- select from the list ")
        for x in type:
            print(x)
        a_type = input("Type --> ")

        girl = input("what is the girls type")
        girl_type.append(girl)
        continue
    else:
        print("LUPET MO BOSS")
        break


