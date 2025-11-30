#7
class ContBancar:
    def __init__(self, titular_cont, sold=0):
        self.titular_cont = titular_cont
        self.sold = sold
        self.descoperire_permisa = False
    
    def alimentare(self, suma):
        if suma > 0:
            self.sold += suma
            print(f"Suma de {suma} a fost alimentata. Sold curent: {self.sold}")
        else:
            print("Suma trebuie sa fie pozitiva.")
        return self.sold
    
    def retragere(self, suma):
        if suma <= 0:
            print("Suma trebuie sa fie pozitiva.")
            return self.sold
        
        if suma<= self.sold:
            self.sold -= suma
            print(f"Suma de {suma} a fost retrasa. Sold curent: {self.sold}")
        elif self.descoperire_permisa:
            self.sold -= suma
            print(f"Suma de {suma} a fost retrasa cu descoperire permisa. Sold curent: {self.sold}")
        else:
            print("Fonduri insuficiente si descoperire nepermisa.")
        return self.sold
    
    def set_descoperire_permisa(self, permisiune):
        self.descoperire_permisa = permisiune
        if permisiune:
            print("Descoperirea este permisa.")
        else:
            print("Descoperirea nu este permisa.")
    
    def afisare_sold(self):
        print(f"Titular cont: {self.titular_cont}, Sold curent: {self.sold}, Descoperire permisa: {self.descoperire_permisa}")
    

cont1 = ContBancar("Ion Popescu", 1000)
cont1.afisare_sold()
cont1.alimentare(500)
cont1.retragere(200)
cont1.retragere(2000)
cont1.set_descoperire_permisa(True)
cont1.retragere(2000)
cont1.afisare_sold()