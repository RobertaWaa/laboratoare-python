#1
# class Vehicul:
#     def __init__(self, marca, an_fabricatie):
#         self.marca = marca
#         self.an_fabricatie = an_fabricatie
    
#     def afisare_informatii(self):
#         print(f"Marca: {self.marca}, An fabricatie: {self.an_fabricatie}")

# class Masina(Vehicul):
#     def __init__(self, marca, an_fabricatie, numar_usi):
#         super().__init__(marca, an_fabricatie)
#         self.numar_usi = numar_usi
    
# masina1 = Masina("Mazda", 2023, 2)
# print("Informatii masina:")
# masina1.afisare_informatii()
# print(f"Numar usi: {masina1.numar_usi}")


#2
# class Masina(Vehicul):
#     def __init__(self, marca, an_fabricatie, numar_usi):
#         super().__init__(marca, an_fabricatie)
#         self.numar_usi = numar_usi
#     def afisare_informatii(self):
#         print(f"Marca: {self.marca}, An fabricatie: {self.an_fabricatie}, Numar usi: {self.numar_usi}")

# masina1=Masina("Mazda", 2023, 2)
# print("Informatii masina:")
# masina1.afisare_informatii()


#3
# class Student:
#     def __init__(self, nume, medie_generala=0):
#         self.nume = nume
#         self._medie_generala = 0
#         self.set_medie(medie_generala)

#     def get_medie(self):
#         return self._medie_generala
    
#     def set_medie(self, medie_noua):
#         if 0 <= medie_noua <= 100:
#             self._medie_generala = medie_noua
#         else:
#             print("Eroare: Media generala trebuie sa fie intre 0 si 10.")
    
#     def afisare_informatii(self):
#         print(f"Student: {self.nume}, Media generala: {self._medie_generala}")

# student1 = Student("Ion Popescu", 95)
# student1.afisare_informatii()
# student1.set_medie(85)
# student1.set_medie(105)


#4
# # calcule.py
# import math
# #pentru cerc
# def calcul_arie(raza):
#     return math.pi * raza ** 2

# def calcul_perimetru(raza):
#     return 2 * math.pi * raza

# #main.py
# import calcule

# raza = float(input("Introduceti raza cercului: "))
# arie = calcule.calcul_arie(raza)
# perimetru = calcule.calcul_perimetru(raza)

# print(f"Pentru cercul cu raza {raza}:")
# print(f"Aria: {arie:.2f}")
# print(f"Perimetrul: {perimetru:.2f}")


#5
# # calcule.py
# import math
# #pentru cerc
# def calcul_arie(raza):
#     return math.pi * raza ** 2

# def calcul_perimetru(raza):
#     return 2 * math.pi * raza

# #main.py
# from utils import calcule

# raza = float(input("Introduceti raza cercului: "))
# arie = calcule.calcul_arie(raza)
# perimetru = calcule.calcul_perimetru(raza)

# print(f"Pentru cercul cu raza {raza}:")
# print(f"Aria: {arie:.2f}")
# print(f"Perimetrul: {perimetru:.2f}")


#6
# def scriere_notite():
#     nume_fisier = "notite.txt"

#     with open(nume_fisier, "w", encoding="utf-8") as f:
#         print("Introduceti notitele. Pentru a opri, introduceti 'stop' la nume.")

#         while True:
#             nume = input("\nIntroduceti numele:")
#             if nume.lower() == 'stop':
#                 break

#             notita = input("Introduceti notita:")
#             if notita.lower() == 'stop':
#                 break

#             f.write(f"Notita de la {nume}: {notita}\n")
#             print("Notita salvata.")

# scriere_notite()


#7
# def citire_si_actualizare_notite():
#     nume_fisier = "notite.txt"

#     try:
#         #citire si afisare continut
#         with open(nume_fisier, 'r', encoding='utf-8') as f:
#             linii = f.readlines()
#             print("Notitele salvate sunt:")
#             for i, linie in enumerate(linii, 1):
#                 print(f"{i}. {linie.strip()}")
        
#         #adaugare numar notite la final
#         with open(nume_fisier, 'a', encoding='utf-8') as f:
#             f.write(f"\nNumar total de notite: {len(linii)}\n")
#             print(f"\nS-au adaugat {len(linii)} in fisier.")

#     except FileNotFoundError:
#         print(f"Fisierul nu exista! Rulati mai intai problema 6.")

# citire_si_actualizare_notite()


#8
# import csv

# def creare_fisier_csv():
#     nume_fisier = "studenti.csv"

#     #exemplu
#     studenti = [
#         {'NumeStudent': 'Ion Popescu', 'NotaTest1': 8, 'NotaTest2': 9},
#         {'NumeStudent': 'Maria Ionescu', 'NotaTest1': 10, 'NotaTest2': 9},
#         {'NumeStudent': 'Ana Georgescu', 'NotaTest1': 7, 'NotaTest2': 8},
#         {'NumeStudent': 'Vasile Dumitrescu', 'NotaTest1': 6, 'NotaTest2': 7}
#     ]

#     with open(nume_fisier, mode='w', newline='', encoding='utf-8') as f:
#         campuri = ['NumeStudent', 'NotaTest1', 'NotaTest2']
#         writer = csv.DictWriter(f, fieldnames=campuri)

#         writer.writeheader()
#         writer.writerows(studenti)

#     print(f"Fisierul '{nume_fisier}' a fost creat cu succes.")
#     print("Continutul fisierului:")

#     with open(nume_fisier, mode='r', encoding='utf-8') as f:
#         print(f.read())

# creare_fisier_csv()


#9
# import csv

# class Student:
#     def __init__(self, nume, medie_generala=0):
#         self.nume = nume
#         self._medie_generala = 0
#         self.set_medie(medie_generala)
    
#     def get_medie(self):
#         return self._medie_generala
    
#     def set_medie(self, medie_noua):
#         if 0 <= medie_noua <= 100:
#             self._medie_generala = medie_noua
#         else:
#             print(f"Eroare: Media {medie_noua} trebuie sa fie intre 0 si 100")
    
#     def afisare_informatii(self):
#         print(f"Student: {self.nume}, Medie: {self._medie_generala}")

# def citire_studenti_din_csv():
#     nume_fisier = "studenti.csv"
#     lista_studenti = []
#     try:
#         with open(nume_fisier, 'r', encoding='utf-8') as f:
#             reader = csv.DictReader(f)

#             for rand in reader:
#                 nume = rand['NumeStudent']
#                 nota1 = float(rand['NotaTest1'])
#                 nota2 = float(rand['NotaTest2'])
#                 medie = (nota1 + nota2) / 2
#                 student = Student(nume, medie)
#                 lista_studenti.append(student)
#         return lista_studenti
#     except FileNotFoundError:
#         print(f"Eroare! Rulati mai intai problema 8.")
#         return []
    
# def calcul_medie_clasa(lista_studenti):
#     if not lista_studenti:
#         return 0
#     suma_medii = sum(student.get_medie() for student in lista_studenti)
#     return suma_medii / len(lista_studenti)

# studenti = citire_studenti_din_csv()
# if studenti:
#     print("\nLista studenti:")
#     for student in studenti:
#         student.afisare_informatii()
    
#     medie_clasa = calcul_medie_clasa(studenti)
#     print(f"\nMedia generala a clasei: {medie_clasa:.2f}")