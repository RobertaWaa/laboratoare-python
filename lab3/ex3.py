#3
inventar = {
    "mar": 10,
    "banana": 5,
    "biscuiti": 3,
    "lapte": 8,
    "oua": 12    
}
articol_cautat = input("Introduceti numele articolului cautat: ")
if articol_cautat in inventar:
    print(f"Articolul '{articol_cautat}' este in stoc. Cantitate: {inventar[articol_cautat]}")
else:
    print(f"Articolul '{articol_cautat}' nu este in stoc.")