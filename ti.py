print("Malá násobilka dvou na řádku:")
for i in range(1, 11):
    print(2 * i, end=' ')
print("\n")

# 2. Mocniny dvou od 2 do 65536, zarovnané pod sebou podle řádů
print("Mocniny dvou (zarovnané pod sebou):")
powers = [2**i for i in range(1, 17)]  # 2^1 až 2^16 (65536)
max_width = len(str(powers[-1]))  # Největší šířka čísla
for power in powers:
    print(str(power).rjust(max_width))  # Zarovnání doprava

print("\n")

# 3. Čtení čísel dokud nezadáme 0, pak výpis sumy
print("Zadávejte čísla (0 pro ukončení):")
suma = 0
while True:
    try:
        cislo = int(input("Zadej číslo: "))
        if cislo == 0:
            break
        suma += cislo
    except ValueError:
        print("Zadej platné celé číslo.")
print("Součet zadaných čísel je:", suma)