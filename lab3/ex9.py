#9
import random
numar_secret = random.randint(1, 100)
incercari = 0
print("Ghicește numărul între 1 și 100!")
while True:
    incercare = int(input("Introdu numărul tău: "))
    incercari += 1
    if incercare == numar_secret:
        print(f"Felicitări! Ai ghicit numărul {numar_secret} în {incercari} încercări.")
        break
    elif incercare < numar_secret:
        print("Numărul este mai mare. Încearcă din nou.")
    else:
        print("Numărul este mai mic. Încearcă din nou.")