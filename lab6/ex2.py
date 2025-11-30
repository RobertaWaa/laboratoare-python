import numpy as np 
arr_original = np.random.rand(4, 3) * 10
print("Tabloul original:")
print(arr_original)

np.save('tablou_original.npy', arr_original)

arr_modificat = arr_original.copy()

arr_modificat[0, :] += 1  #incrementare +1 pe prima linie
arr_modificat[:, 1] *= 2  #dublare tot pe a doua coloana
arr_modificat[-1, :] *= -1  #schimbare semn pe ultima linie
arr_modificat[:, 2] = 0  #inlocuire coloana a treia cu 0

print("\nTabloul modificat:")
print(arr_modificat)

arr_incarcat = np.load('tablou_original.npy')

diferenta = arr_modificat - arr_incarcat

print("\nDiferenta dintre tabloul modificat si cel original:")
print(diferenta)