#3
def numar_cifre_pare(n):
    if n < 0:
        return False, -1
    
    cifre_pare = []
    numar_original = n 

    while n> 0 :
        cifra = n % 10
        if cifra % 2 == 0:
            cifre_pare.append(str(cifra))
        n //= 10
    
    if not cifre_pare:
        return False, -1
    
    cifre_pare.reverse()
    numar_nou = int(''.join(cifre_pare))
    return True, numar_nou

numar = int(input("Introduceti un numar intreg pozitiv: "))
succes, rezultat = numar_cifre_pare(numar)

if succes:
    print(f"Numarul format din cifrele pare ale lui {numar} este: {rezultat} ")
else:
    print("Numarul nu contine cifre pare sau este negativ.")