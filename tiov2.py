text = "TI"
print(text)

for znak in text:
    print(znak)

for znak in text:
    print(znak, end= "-")
print()

x = 42
y = "A" if x > 5 else "B"
print(y)

i = 1
for znak in text:
    print(znak, end= "-" if i < len(text) else "")
    i += 1    
print()

i = 1
for znak in text:
    if i > 1:
        print("-", end= "")
    print(znak, end= "")
    i += 1
print()