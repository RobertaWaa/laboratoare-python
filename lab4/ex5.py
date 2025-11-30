#5
def palindrom_str(sir):
    sir_curat= ''.join(caracter.lower() for caracter in sir if caracter.isalnum())

    def verifica_palindrom(s):
        if len(s) <= 1:
            return True
        elif s[0] != s[-1]:
            return False
        return verifica_palindrom(s[1:-1])
    return verifica_palindrom(sir_curat)

def palindrom_int(numar):
    def verifica_palindrom_numar(n):
        if n < 10:
            return True
        
        temp = n 
        numar_cifre = 0 
        while temp > 0:
            numar_cifre +=1
            temp //=10
        
        putere = 10 ** (numar_cifre -1)
        prima_cifra = n // putere
        ultima_cifra = n % 10
        if prima_cifra != ultima_cifra:
            return False
        
        noul_numar = (n % putere) // 10
        return verifica_palindrom_numar(noul_numar)
    return verifica_palindrom_numar(numar)

sir_input = input("Introduceti un sir de caractere: ")
if palindrom_str(sir_input):
    print(f'"{sir_input}" este un palindrom.') 
else:
    print(f'"{sir_input}" nu este un palindrom.')

numar_input = int(input("Introduceti un numar intreg: "))
if palindrom_int(numar_input):
    print(f'{numar_input} este un palindrom.') 
else:
    print(f'{numar_input} nu este un palindrom.')