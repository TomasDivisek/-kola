text = "Jakub halamka"
znaku = len(text)
print("znaku =", znaku)

sloupcu = round(znaku ** 0.5)
print("sloupcu =", sloupcu)

radku = znaku // sloupcu
if sloupcu * radku < znaku:
    radku += 1
print("radku =", radku)