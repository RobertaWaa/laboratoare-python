#2
import random

nume_participanti = []
print("Introduceti numele participantilor:")
for i in range(5):
    nume = input(f"Nume participant {i+1}: ")
    nume_participanti.append(nume)
print(f"\nLista participanti sortata alfabetic: {sorted(nume_participanti)}")
castigator = random.choice(nume_participanti)
print(f"Castigatorul este: {castigator}")