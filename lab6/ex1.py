import numpy as np
import random

lista_originala = [random.randint(100, 1000) for _ in range(20)]
print("Lista originala:", lista_originala)

arr = np.array(lista_originala)
arr_incrementat = arr * 1.2 

print("\nLista dupa incrementare cu 20%:")
print(arr_incrementat)

suma = np.sum(arr_incrementat)
media = np.mean(arr_incrementat)

print(f"Suma valorilor: {suma:.2f}")
print(f"Media valorilor: {media:.2f}")