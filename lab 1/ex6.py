#ex6
v=int(input("valoarea notei de plata= "))
n=int(input("numarul de persoane= "))
p=v/n
if p%1==0:
    print("valoarea pe persoana este de: ", int(p), "lei")
else: 
    print ("valoarea pe persoana este de: ", int(p), "lei" , "si", round(p%1,2), "bani")