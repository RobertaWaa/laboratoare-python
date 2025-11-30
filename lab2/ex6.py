#6
fraza = input("Introduceti o fraza: ")
vocale = "aeiou"
consoane = "bcdfghjklmnpqrstvwxyz"
numar_vocale = 0
numar_consoane = 0
for caracter in fraza.lower():
    if caracter in vocale:
        numar_vocale += 1
    elif caracter in consoane:
        numar_consoane += 1
print("Numar de vocale:", numar_vocale)
print("Numar de consoane:", numar_consoane)