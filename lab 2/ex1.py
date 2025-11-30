#1
nota= int(input("Introduceti nota (0-100): "))
if 90<= nota <=100:
    print("Foarte bine")
elif 70<= nota <=89:
    print("Bine")
elif 50<= nota <=69:
    print("Suficient")
elif 0<= nota <=49:
    print("Insuficient")
else:
    print("Nota invalida")