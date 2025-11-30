#1
# def calcul_arie_drept(lungime, latime):
#     arie = lungime * latime
#     return arie
# L= int(input("Introduceti lungimea dreptunghiului: "))
# l= int(input("Introduceti latimea dreptunghiului: "))
# arie_dreptunghi = calcul_arie_drept(L, l)
# print("Aria dreptunghiului este:", arie_dreptunghi)


#2
# import math

# def calcul_arie(figura, *parametri):
#     if figura == "cerc":
#         raza = parametri[0]
#         return math.pi * raza ** 2
#     elif figura == "dreptunghi":
#         lungime, latime = parametri
#         return lungime * latime
#     elif figura == "patrat":
#         latura = parametri[0]
#         return latura ** 2
#     elif figura == "trapez":
#         baza_mare, baza_mica, inaltime = parametri
#         return (baza_mare + baza_mica) * inaltime / 2
#     else:
#         return "Figura necunoscuta "
    
# print("Aria cercului:", calcul_arie("cerc", 5))
# print("Aria dreptunghiului:", calcul_arie("dreptunghi", 4, 6))
# print("Aria patratului:", calcul_arie("patrat", 4))
# print("Aria trapezului:", calcul_arie("trapez", 6, 4, 5))


#3
# def numar_cifre_pare(n):
#     if n < 0:
#         return False, -1
    
#     cifre_pare = []
#     numar_original = n 

#     while n> 0 :
#         cifra = n % 10
#         if cifra % 2 == 0:
#             cifre_pare.append(str(cifra))
#         n //= 10
    
#     if not cifre_pare:
#         return False, -1
    
#     cifre_pare.reverse()
#     numar_nou = int(''.join(cifre_pare))
#     return True, numar_nou

# numar = int(input("Introduceti un numar intreg pozitiv: "))
# succes, rezultat = numar_cifre_pare(numar)

# if succes:
#     print(f"Numarul format din cifrele pare ale lui {numar} este: {rezultat} ")
# else:
#     print("Numarul nu contine cifre pare sau este negativ.")


#4
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# n=int(input("Introduceti pozitia in sirul Fibonacci: "))
# if n < 0:
#     print("Pozitia trebuie sa fie un numar intreg nenegativ.")
# else:
#     rezultat = fibonacci(n)
#     print(f"Numarul de pe pozitia {n} in sirul Fibonacci este: {rezultat}")


#5
# def palindrom_str(sir):
#     sir_curat= ''.join(caracter.lower() for caracter in sir if caracter.isalnum())

#     def verifica_palindrom(s):
#         if len(s) <= 1:
#             return True
#         elif s[0] != s[-1]:
#             return False
#         return verifica_palindrom(s[1:-1])
#     return verifica_palindrom(sir_curat)

# def palindrom_int(numar):
#     def verifica_palindrom_numar(n):
#         if n < 10:
#             return True
        
#         temp = n 
#         numar_cifre = 0 
#         while temp > 0:
#             numar_cifre +=1
#             temp //=10
        
#         putere = 10 ** (numar_cifre -1)
#         prima_cifra = n // putere
#         ultima_cifra = n % 10
#         if prima_cifra != ultima_cifra:
#             return False
        
#         noul_numar = (n % putere) // 10
#         return verifica_palindrom_numar(noul_numar)
#     return verifica_palindrom_numar(numar)

# sir_input = input("Introduceti un sir de caractere: ")
# if palindrom_str(sir_input):
#     print(f'"{sir_input}" este un palindrom.') 
# else:
#     print(f'"{sir_input}" nu este un palindrom.')

# numar_input = int(input("Introduceti un numar intreg: "))
# if palindrom_int(numar_input):
#     print(f'{numar_input} este un palindrom.') 
# else:
#     print(f'{numar_input} nu este un palindrom.')
    

#6
# class Student:
#     universitate = "Universitatea Politehnica Bucuresti"

#     def __init__(self, nume, cnp, an_studiu, facultate, specializare):
#         self.nume = nume
#         self.cnp = cnp
#         self.an_studiu = an_studiu
#         self.facultate = facultate
#         self.specializare = specializare

#     def afisare_informatii(self):
#         print(f"Nume: {self.nume}")
#         print(f"CNP: {self.cnp}")
#         print(f"An de studiu: {self.an_studiu}")
#         print(f"Facultate: {self.facultate}")
#         print(f"Specializare: {self.specializare}")
#         print(f"Universitate: {Student.universitate}")
#         print(f"Varsta: {self.calcul_varsta()} ani")
#         print("-" * 30)
    
#     def calcul_varsta(self):
#         an_cnp = int(self.cnp[1:3])
#         luna_cnp = int(self.cnp[3:5])
#         zi_cnp = int(self.cnp[5:7])

#         if an_cnp >= 0 and an_cnp <= 25:
#             an_nastere = 2000 + an_cnp
#         else:
#             an_nastere = 1900 + an_cnp 
        
#         from datetime import date
#         data_nasterii = date(an_nastere, luna_cnp, zi_cnp)
#         data_azi = date.today()
#         varsta = data_azi.year - data_nasterii.year - ((data_azi.month, data_azi.day) < (data_nasterii.month, data_nasterii.day))
#         return varsta
        
#     def modificare_an_studiu(self, an_nou):
#         if 1<=an_nou<= 6:
#             self.an_studiu = an_nou
#             print(f"Anul de studiu al studentului {self.nume} a fost actualizat la {an_nou}.")
#         else:
#             print("Anul de studiu trebuie sa fie intre 1 si 6.")

# student1 = Student("Ion Popescu", "1980506123456", 2, "Facultatea de Calculatoare", "Informatica")
# student2 = Student("Maria Ionescu", "6020307123456", 3, "Facultatea de Electronica", "Telecomunicatii")
# student3 = Student("Andreea Vasilescu", "2991115123456", 1, "Facultatea de Mecanica", "Inginerie Mecanica")

# print("Informatii studenti:")
# student1.afisare_informatii()
# student2.afisare_informatii()
# student3.afisare_informatii()

# student1.modificare_an_studiu(3)
# student1.afisare_informatii()


#7
# class ContBancar:
#     def __init__(self, titular_cont, sold=0):
#         self.titular_cont = titular_cont
#         self.sold = sold
#         self.descoperire_permisa = False
    
#     def alimentare(self, suma):
#         if suma > 0:
#             self.sold += suma
#             print(f"Suma de {suma} a fost alimentata. Sold curent: {self.sold}")
#         else:
#             print("Suma trebuie sa fie pozitiva.")
#         return self.sold
    
#     def retragere(self, suma):
#         if suma <= 0:
#             print("Suma trebuie sa fie pozitiva.")
#             return self.sold
        
#         if suma<= self.sold:
#             self.sold -= suma
#             print(f"Suma de {suma} a fost retrasa. Sold curent: {self.sold}")
#         elif self.descoperire_permisa:
#             self.sold -= suma
#             print(f"Suma de {suma} a fost retrasa cu descoperire permisa. Sold curent: {self.sold}")
#         else:
#             print("Fonduri insuficiente si descoperire nepermisa.")
#         return self.sold
    
#     def set_descoperire_permisa(self, permisiune):
#         self.descoperire_permisa = permisiune
#         if permisiune:
#             print("Descoperirea este permisa.")
#         else:
#             print("Descoperirea nu este permisa.")
    
#     def afisare_sold(self):
#         print(f"Titular cont: {self.titular_cont}, Sold curent: {self.sold}, Descoperire permisa: {self.descoperire_permisa}")
    

# cont1 = ContBancar("Ion Popescu", 1000)
# cont1.afisare_sold()
# cont1.alimentare(500)
# cont1.retragere(200)
# cont1.retragere(2000)
# cont1.set_descoperire_permisa(True)
# cont1.retragere(2000)
# cont1.afisare_sold()