import csv

class Student:
    def __init__(self, nume, medie_generala=0):
        self.nume = nume
        self._medie_generala = 0
        self.set_medie(medie_generala)
    
    def get_medie(self):
        return self._medie_generala
    
    def set_medie(self, medie_noua):
        if 0 <= medie_noua <= 100:
            self._medie_generala = medie_noua
        else:
            print(f"Eroare: Media {medie_noua} trebuie sa fie intre 0 si 100")
    
    def afisare_informatii(self):
        print(f"Student: {self.nume}, Medie: {self._medie_generala}")

def citire_studenti_din_csv():
    nume_fisier = "studenti.csv"
    lista_studenti = []
    try:
        with open(nume_fisier, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for rand in reader:
                nume = rand['NumeStudent']
                nota1 = float(rand['NotaTest1'])
                nota2 = float(rand['NotaTest2'])
                medie = (nota1 + nota2) / 2
                student = Student(nume, medie)
                lista_studenti.append(student)
        return lista_studenti
    except FileNotFoundError:
        print(f"Eroare! Rulati mai intai problema 8.")
        return []
    
def calcul_medie_clasa(lista_studenti):
    if not lista_studenti:
        return 0
    suma_medii = sum(student.get_medie() for student in lista_studenti)
    return suma_medii / len(lista_studenti)

studenti = citire_studenti_din_csv()
if studenti:
    print("\nLista studenti:")
    for student in studenti:
        student.afisare_informatii()
    
    medie_clasa = calcul_medie_clasa(studenti)
    print(f"\nMedia generala a clasei: {medie_clasa:.2f}")