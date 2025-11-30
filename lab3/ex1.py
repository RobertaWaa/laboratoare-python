#1
fraza = input("Introduceceti o fraza: ")
cuvant_cenzurat = input("Introduceceti cuvantul de cenzurat: ")
if cuvant_cenzurat in fraza:
    fraza_cenzurata = fraza.replace(cuvant_cenzurat, '*' * len(cuvant_cenzurat))
    print("Fraza cenzurata:", fraza_cenzurata)