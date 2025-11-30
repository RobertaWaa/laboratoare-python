#5
import math
nota_plata= float(input("Introduceti nota de plata: "))
numar_persoane= int(input("Introduceti numarul de persoane: "))
suma_persoana= nota_plata/numar_persoane
lei= math.floor(suma_persoana)
bani= round((suma_persoana - lei) * 100)
print(f"Fiecare persoana trebuie sa plateasca: {lei} lei si {bani} bani")