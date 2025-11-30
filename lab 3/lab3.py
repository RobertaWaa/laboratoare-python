#1
# fraza = input("Introduceceti o fraza: ")
# cuvant_cenzurat = input("Introduceceti cuvantul de cenzurat: ")
# if cuvant_cenzurat in fraza:
#     fraza_cenzurata = fraza.replace(cuvant_cenzurat, '*' * len(cuvant_cenzurat))
#     print("Fraza cenzurata:", fraza_cenzurata)

#2
# import random

# nume_participanti = []
# print("Introduceti numele participantilor:")
# for i in range(5):
#     nume = input(f"Nume participant {i+1}: ")
#     nume_participanti.append(nume)
# print(f"\nLista participanti sortata alfabetic: {sorted(nume_participanti)}")
# castigator = random.choice(nume_participanti)
# print(f"Castigatorul este: {castigator}")

#3
# inventar = {
#     "mar": 10,
#     "banana": 5,
#     "biscuiti": 3,
#     "lapte": 8,
#     "oua": 12    
# }
# articol_cautat = input("Introduceti numele articolului cautat: ")
# if articol_cautat in inventar:
#     print(f"Articolul '{articol_cautat}' este in stoc. Cantitate: {inventar[articol_cautat]}")
# else:
#     print(f"Articolul '{articol_cautat}' nu este in stoc.")

#4
# import math
# raza = float(input("Introduceti raza cercului: "))
# perimetru = 2 * math.pi * raza
# arie = math.pi * raza ** 2
# print(f"Perimetrul cercului este: {perimetru:.2f}")
# print(f"Aria cercului este: {arie:.2f}")

#5
# import math
# nota_plata= float(input("Introduceti nota de plata: "))
# numar_persoane= int(input("Introduceti numarul de persoane: "))
# suma_persoana= nota_plata/numar_persoane
# lei= math.floor(suma_persoana)
# bani= round((suma_persoana - lei) * 100)
# print(f"Fiecare persoana trebuie sa plateasca: {lei} lei si {bani} bani")

#6
# import random
# zar1 = random.randint(1, 6)
# zar2 = random.randint(1, 6)
# print(f"Rezultatul aruncarii celor doua zaruri este: {zar1} si {zar2}. Suma este: {zar1 + zar2}")

#7
# nume_institutie = input("Introduceti numele institutiei: ")
# cuvinte = nume_institutie.split()
# acronim = ""
# for cuvant in cuvinte:
#     acronim += cuvant[0].upper()
# print(f"Acronimul institutiei '{nume_institutie}' este: {acronim}")

#8
# fraza = input("Introduceti o fraza: ")
# fraza_curata = fraza.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")
# cuvinte = fraza_curata.split()
# dictionar_cuvinte = {}
# for cuvant in cuvinte:
#     if cuvant in dictionar_cuvinte:
#         dictionar_cuvinte[cuvant] += 1
#     else:
#         dictionar_cuvinte[cuvant] = 1
# print("Frecventa cuvintelor in fraza:")
# for cuvant, frecventa in dictionar_cuvinte.items():
#     print(f"'{cuvant}': {frecventa}")

#9
# import random
# numar_secret = random.randint(1, 100)
# incercari = 0
# print("Ghicește numărul între 1 și 100!")
# while True:
#     incercare = int(input("Introdu numărul tău: "))
#     incercari += 1
#     if incercare == numar_secret:
#         print(f"Felicitări! Ai ghicit numărul {numar_secret} în {incercari} încercări.")
#         break
#     elif incercare < numar_secret:
#         print("Numărul este mai mare. Încearcă din nou.")
#     else:
#         print("Numărul este mai mic. Încearcă din nou.")

#10
# import time
# import random
# fraze = [
#     "Cunoasterea este putere.",
#     "Invatarea continua este cheia succesului.",
#     "Practica duce la perfectiune.",
#     "Fiecare zi este o noua oportunitate.",
#     "Nu renunta niciodata la visele tale."]
# fraza_aleasa = random.choice(fraze)
# print("Tastati urmatoarea fraza cat mai repede posibil:")
# print(fraza_aleasa)
# input("Apasati Enter cand sunteti gata...")
# start_time = time.time()
# tastare_utilizator = input("Tastati fraza aici: ")
# end_time = time.time()
# timp_petrecut = end_time - start_time
# print(f"Timpul petrecut: {timp_petrecut:.2f} secunde")
# if tastare_utilizator == fraza_aleasa:
#     print("Felicitari! Fraza a fost tastata corect.")
# else:
#     print("Fraza nu a fost tastata corect.")