text = "Špek"
delka_textu = len(text)
print(delka_textu)

pole = [" "] * delka_textu
print(pole)

for i in range(delka_textu):
    pole[delka_textu-i-1] = text[i]
print(pole)

for i in range(delka_textu):
    print(i)

for i in range(delka_textu):
    print(pole[i])