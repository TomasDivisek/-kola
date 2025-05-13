def faktorial(n):
    if n == 0:
        return 1
    return n * faktorial(n - 1)

cislo = int(input("Zadej číslo: "))
print("Faktoriál:", faktorial(cislo))