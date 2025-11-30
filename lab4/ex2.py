#2
import math

def calcul_arie(figura, *parametri):
    if figura == "cerc":
        raza = parametri[0]
        return math.pi * raza ** 2
    elif figura == "dreptunghi":
        lungime, latime = parametri
        return lungime * latime
    elif figura == "patrat":
        latura = parametri[0]
        return latura ** 2
    elif figura == "trapez":
        baza_mare, baza_mica, inaltime = parametri
        return (baza_mare + baza_mica) * inaltime / 2
    else:
        return "Figura necunoscuta "
    
print("Aria cercului:", calcul_arie("cerc", 5))
print("Aria dreptunghiului:", calcul_arie("dreptunghi", 4, 6))
print("Aria patratului:", calcul_arie("patrat", 4))
print("Aria trapezului:", calcul_arie("trapez", 6, 4, 5))