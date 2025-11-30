#6
class Student:
    universitate = "Universitatea Politehnica Bucuresti"

    def __init__(self, nume, cnp, an_studiu, facultate, specializare):
        self.nume = nume
        self.cnp = cnp
        self.an_studiu = an_studiu
        self.facultate = facultate
        self.specializare = specializare

    def afisare_informatii(self):
        print(f"Nume: {self.nume}")
        print(f"CNP: {self.cnp}")
        print(f"An de studiu: {self.an_studiu}")
        print(f"Facultate: {self.facultate}")
        print(f"Specializare: {self.specializare}")
        print(f"Universitate: {Student.universitate}")
        print(f"Varsta: {self.calcul_varsta()} ani")
        print("-" * 30)
    
    def calcul_varsta(self):
        an_cnp = int(self.cnp[1:3])
        luna_cnp = int(self.cnp[3:5])
        zi_cnp = int(self.cnp[5:7])

        if an_cnp >= 0 and an_cnp <= 25:
            an_nastere = 2000 + an_cnp
        else:
            an_nastere = 1900 + an_cnp 
        
        from datetime import date
        data_nasterii = date(an_nastere, luna_cnp, zi_cnp)
        data_azi = date.today()
        varsta = data_azi.year - data_nasterii.year - ((data_azi.month, data_azi.day) < (data_nasterii.month, data_nasterii.day))
        return varsta
        
    def modificare_an_studiu(self, an_nou):
        if 1<=an_nou<= 6:
            self.an_studiu = an_nou
            print(f"Anul de studiu al studentului {self.nume} a fost actualizat la {an_nou}.")
        else:
            print("Anul de studiu trebuie sa fie intre 1 si 6.")

student1 = Student("Ion Popescu", "1980506123456", 2, "Facultatea de Calculatoare", "Informatica")
student2 = Student("Maria Ionescu", "6020307123456", 3, "Facultatea de Electronica", "Telecomunicatii")
student3 = Student("Andreea Vasilescu", "2991115123456", 1, "Facultatea de Mecanica", "Inginerie Mecanica")

print("Informatii studenti:")
student1.afisare_informatii()
student2.afisare_informatii()
student3.afisare_informatii()

student1.modificare_an_studiu(3)
student1.afisare_informatii()