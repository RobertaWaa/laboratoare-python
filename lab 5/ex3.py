#3
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
            print("Eroare: Media generala trebuie sa fie intre 0 si 10.")
    
    def afisare_informatii(self):
        print(f"Student: {self.nume}, Media generala: {self._medie_generala}")

student1 = Student("Ion Popescu", 95)
student1.afisare_informatii()
student1.set_medie(85)
student1.set_medie(105)