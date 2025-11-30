import csv

def creare_fisier_csv():
    nume_fisier = "studenti.csv"

    #exemplu
    studenti = [
        {'NumeStudent': 'Ion Popescu', 'NotaTest1': 8, 'NotaTest2': 9},
        {'NumeStudent': 'Maria Ionescu', 'NotaTest1': 10, 'NotaTest2': 9},
        {'NumeStudent': 'Ana Georgescu', 'NotaTest1': 7, 'NotaTest2': 8},
        {'NumeStudent': 'Vasile Dumitrescu', 'NotaTest1': 6, 'NotaTest2': 7}
    ]

    with open(nume_fisier, mode='w', newline='', encoding='utf-8') as f:
        campuri = ['NumeStudent', 'NotaTest1', 'NotaTest2']
        writer = csv.DictWriter(f, fieldnames=campuri)

        writer.writeheader()
        writer.writerows(studenti)

    print(f"Fisierul '{nume_fisier}' a fost creat cu succes.")
    print("Continutul fisierului:")

    with open(nume_fisier, mode='r', encoding='utf-8') as f:
        print(f.read())

creare_fisier_csv()