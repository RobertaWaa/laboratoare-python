#6
def scriere_notite():
    nume_fisier = "notite.txt"

    with open(nume_fisier, "w", encoding="utf-8") as f:
        print("Introduceti notitele. Pentru a opri, introduceti 'stop' la nume.")

        while True:
            nume = input("\nIntroduceti numele:")
            if nume.lower() == 'stop':
                break

            notita = input("Introduceti notita:")
            if notita.lower() == 'stop':
                break

            f.write(f"Notita de la {nume}: {notita}\n")
            print("Notita salvata.")

scriere_notite()