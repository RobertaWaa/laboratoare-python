def citire_si_actualizare_notite():
    nume_fisier = "notite.txt"

    try:
        #citire si afisare continut
        with open(nume_fisier, 'r', encoding='utf-8') as f:
            linii = f.readlines()
            print("Notitele salvate sunt:")
            for i, linie in enumerate(linii, 1):
                print(f"{i}. {linie.strip()}")
        
        #adaugare numar notite la final
        with open(nume_fisier, 'a', encoding='utf-8') as f:
            f.write(f"\nNumar total de notite: {len(linii)}\n")
            print(f"\nS-au adaugat {len(linii)} in fisier.")

    except FileNotFoundError:
        print(f"Fisierul nu exista! Rulati mai intai problema 6.")

citire_si_actualizare_notite()