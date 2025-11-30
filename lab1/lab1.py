#ex 1
# a=int(input("a= "))
# b=int(input("b= "))
# c=int(input("c= "))
# print(str(a) + "+" + str(b) + "=", a+b)
# print(str(a) + "+" + str(c) + "=", a+c)
# print(str(c) + "+" + str(b) + "=", c+b)

#ex2
# l=int(input("lungimea= "))
# h=int(input("inaltimea= "))
# A=1/2*l*h
# print("aria triunghiului este: ", A)

#ex3
# l=int(input("lungimea= "))
# h=int(input("inaltimea= "))
# m=int(input("limita= "))
# P=2*(l+h)
# if P>m:
#     print("perimetrul este mai mare decat limita")
# else:
#     print("perimetrul este mai mic decat limita")

#ex4
# n=int(input("varsta= "))
# m=n*365
# print("varsta in zile este: ", m)

#ex5
# c=input("cuvant cheie= ")
# n=int(input("numar= "))
# c=c*n
# print(c)

#ex6
# v=int(input("valoarea notei de plata= "))
# n=int(input("numarul de persoane= "))
# p=v/n
# if p%1==0:
#     print("valoarea pe persoana este de: ", int(p), "lei")
# else: 
#     print ("valoarea pe persoana este de: ", int(p), "lei" , "si", round(p%1,2), "bani")

#ex7
# t=int(input("temperatura in grade celsius= "))
# f=(t*9/5)+32
# print("temperatura in grade fahrenheit este: ", f)

#ex8
# caracter=input("caracter= ")
# for i in range(1,4):
#     print(caracter*i)

#ex9
# a=int(input("a= "))
# b=int(input("b= "))
# a, b = b, a
# print("a=", a)
# print("b=", b)
# print("media numerelor este: ", (a+b)/2)