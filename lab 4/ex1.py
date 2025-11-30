#1
def calcul_arie_drept(lungime, latime):
    arie = lungime * latime
    return arie
L= int(input("Introduceti lungimea dreptunghiului: "))
l= int(input("Introduceti latimea dreptunghiului: "))
arie_dreptunghi = calcul_arie_drept(L, l)
print("Aria dreptunghiului este:", arie_dreptunghi)