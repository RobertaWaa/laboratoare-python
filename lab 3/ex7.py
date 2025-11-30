#7
nume_institutie = input("Introduceti numele institutiei: ")
cuvinte = nume_institutie.split()
acronim = ""
for cuvant in cuvinte:
    acronim += cuvant[0].upper()
print(f"Acronimul institutiei '{nume_institutie}' este: {acronim}")