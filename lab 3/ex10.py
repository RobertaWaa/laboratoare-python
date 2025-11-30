#10
import time
import random
fraze = [
    "Cunoasterea este putere.",
    "Invatarea continua este cheia succesului.",
    "Practica duce la perfectiune.",
    "Fiecare zi este o noua oportunitate.",
    "Nu renunta niciodata la visele tale."]
fraza_aleasa = random.choice(fraze)
print("Tastati urmatoarea fraza cat mai repede posibil:")
print(fraza_aleasa)
input("Apasati Enter cand sunteti gata...")
start_time = time.time()
tastare_utilizator = input("Tastati fraza aici: ")
end_time = time.time()
timp_petrecut = end_time - start_time
print(f"Timpul petrecut: {timp_petrecut:.2f} secunde")
if tastare_utilizator == fraza_aleasa:
    print("Felicitari! Fraza a fost tastata corect.")
else:
    print("Fraza nu a fost tastata corect.")