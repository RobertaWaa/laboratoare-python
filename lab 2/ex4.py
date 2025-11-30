#4
sir = input("Introduceti un sir de caractere: ")
sir=sir.lower()
if sir == sir[::-1]:
    print(f"'{sir}' este palindrom")
else:
    print(f"'{sir}' nu este palindrom") 