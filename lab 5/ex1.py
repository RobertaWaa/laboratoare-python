#1
class Vehicul:
    def __init__(self, marca, an_fabricatie):
        self.marca = marca
        self.an_fabricatie = an_fabricatie
    
    def afisare_informatii(self):
        print(f"Marca: {self.marca}, An fabricatie: {self.an_fabricatie}")

class Masina(Vehicul):
    def __init__(self, marca, an_fabricatie, numar_usi):
        super().__init__(marca, an_fabricatie)
        self.numar_usi = numar_usi
    
masina1 = Masina("Mazda", 2023, 2)
print("Informatii masina:")
masina1.afisare_informatii()
print(f"Numar usi: {masina1.numar_usi}")