from utils import calcule

raza = float(input("Introduceti raza cercului: "))
arie = calcule.calcul_arie(raza)
perimetru = calcule.calcul_perimetru(raza)

print(f"Pentru cercul cu raza {raza}:")
print(f"Aria: {arie:.2f}")
print(f"Perimetrul: {perimetru:.2f}")