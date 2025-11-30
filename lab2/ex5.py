#5
lista = input("Introduceti o lista de numere separate prin spatiu: ").split()

if lista == lista[::-1]:
    print("Lista este palindrom")
else:
    print("Lista nu este palindrom")