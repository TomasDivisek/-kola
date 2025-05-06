
x = 5                  # přiřadíme x hodnotu 5
y = x * 2 - 3          # vypočítáme y: 5 * 2 - 3 = 7

if y % 2 == 0:         # zjistíme, jestli je y sudé
    y += 1             # pokud je sudé, přičteme 1 (změníme na liché)
else:
    y -= 1             # pokud je liché, odečteme 1 (změníme na sudé)

print("Výsledná hodnota y je:", y)