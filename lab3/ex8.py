#8
fraza = input("Introduceti o fraza: ")
fraza_curata = fraza.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")
cuvinte = fraza_curata.split()
dictionar_cuvinte = {}
for cuvant in cuvinte:
    if cuvant in dictionar_cuvinte:
        dictionar_cuvinte[cuvant] += 1
    else:
        dictionar_cuvinte[cuvant] = 1
print("Frecventa cuvintelor in fraza:")
for cuvant, frecventa in dictionar_cuvinte.items():
    print(f"'{cuvant}': {frecventa}")