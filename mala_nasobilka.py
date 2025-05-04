print("Malá násobilka sedmi:")
for i in range(1, 11):
    print(7 * i)

# 2. Sudá čísla v intervalu
print("\nSudá čísla od 1 do 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# 3. Zdvojnásobení haléře
castka = 0.01
suma = 0
for i in range(30):
    suma += castka
    castka *= 2
print("\nPo 30 dnech máš:", round(suma, 2), "Kč")

# 4. Součet násobilky šesti
soucet = 0
for i in range(1, 11):
    soucet += 6 * i
print("\nSoučet násobilky šesti:", soucet)

# 5. Investice bez vkladu
castka = 10000
urok = 0.05
roky = 10
for i in range(roky):
    castka *= 1 + urok
print("\nInvestice bez vkladu:", round(castka, 2), "Kč")

# 6. Investice s měsíčním vkladem
castka = 10000
vklad = 500
urok = 0.05
mesicni_urok = (1 + urok) ** (1/12) - 1
for i in range(12 * roky):
    castka = castka * (1 + mesicni_urok) + vklad
print("\nInvestice s měsíčním vkladem:", round(castka, 2), "Kč")