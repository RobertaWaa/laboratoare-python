#4
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n=int(input("Introduceti pozitia in sirul Fibonacci: "))
if n < 0:
    print("Pozitia trebuie sa fie un numar intreg nenegativ.")
else:
    rezultat = fibonacci(n)
    print(f"Numarul de pe pozitia {n} in sirul Fibonacci este: {rezultat}")