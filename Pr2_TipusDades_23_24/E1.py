"""
Jofre Aleman i Daniel Arco
09/10/2023
ASIXc M03-UF1 A2 pr2

"""
##Demanar el diàmetre d'una pizza rodona i imprimeix la seva superfície. Pots usar Math.PI per escriure el valor de Pi.
import math

r = float(input("Vols saber la superfície d'una pizza? Doncs passem el seu radi en cm!\n : "))


supericie_output = 2 * math.pi * r**2

print(f"El seu diamtre es de {r} cm")
