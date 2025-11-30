#7
agenda = {
    "Ion Popescu": "0712345678",
    "Maria Ionescu": "0723456789",
    "Vasile Georgescu": "0734567890"
}
nume_cautat = input("Introduceti numele persoanei cautate: ")
if nume_cautat in agenda:
    print(f"Numarul de telefon al lui {nume_cautat} este {agenda[nume_cautat]}")
else:
    print(f"{nume_cautat} nu se afla in agenda.")