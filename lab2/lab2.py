#1
# nota= int(input("Introduceti nota (0-100): "))
# if 90<= nota <=100:
#     print("Foarte bine")
# elif 70<= nota <=89:
#     print("Bine")
# elif 50<= nota <=69:
#     print("Suficient")
# elif 0<= nota <=49:
#     print("Insuficient")
# else:
#     print("Nota invalida")

#2
# n=int(input("Introduceti un numar: "))
# for i in range(1,n+1):
#     print('*' * i)

#3
# l = [11, 4, 23, 8, 16]
# maxim = l[0]
# for numar in l:
#     if numar > maxim:
#         maxim = numar
# print("Numarul maxim este:", maxim)

#4
# sir = input("Introduceti un sir de caractere: ")
# sir=sir.lower()
# if sir == sir[::-1]:
#     print(f"'{sir}' este palindrom")
# else:
#     print(f"'{sir}' nu este palindrom") 

#5
# lista = input("Introduceti o lista de numere separate prin spatiu: ").split()

# if lista == lista[::-1]:
#     print("Lista este palindrom")
# else:
#     print("Lista nu este palindrom")

#6
# fraza = input("Introduceti o fraza: ")
# vocale = "aeiou"
# consoane = "bcdfghjklmnpqrstvwxyz"
# numar_vocale = 0
# numar_consoane = 0
# for caracter in fraza.lower():
#     if caracter in vocale:
#         numar_vocale += 1
#     elif caracter in consoane:
#         numar_consoane += 1
# print("Numar de vocale:", numar_vocale)
# print("Numar de consoane:", numar_consoane)

#7
# agenda = {
#     "Ion Popescu": "0712345678",
#     "Maria Ionescu": "0723456789",
#     "Vasile Georgescu": "0734567890"
# }
# nume_cautat = input("Introduceti numele persoanei cautate: ")
# if nume_cautat in agenda:
#     print(f"Numarul de telefon al lui {nume_cautat} este {agenda[nume_cautat]}")
# else:
#     print(f"{nume_cautat} nu se afla in agenda.")