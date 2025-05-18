while True:
    print("1 = Soucet, 2 = Prumer, 0 = Konec")
    volba = input("Zadej volbu: ")
    if volba == "1":
        a, b = int(input("A: ")), int(input("B: "))
        print("Součet:", a + b)
    elif volba == "2":
        data = list(map(int, input("Zadej cisla: ").split()))
        print("Prumer:", sum(data)/len(data))
    elif volba == "0":
        break
    else:
        print("Neplatna volba")
