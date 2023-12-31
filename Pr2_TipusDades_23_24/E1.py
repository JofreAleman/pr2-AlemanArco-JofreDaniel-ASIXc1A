"""
Jofre Aleman i Daniel Arco
09/10/2023
ASIXc M03-UF1 A2 pr2

Exercici 1: Demanar el diàmetre d'una pizza rodona i imprimeix la seva superfície.
"""

#Importem el dicionari math
import math

#Demanem el diametre i el transformem en radi, ja que a la formula ens demanen el radi
diametre = float(input("Vols saber la superfície d'una pizza? \nDoncs passem el seu diàmetre en cm!: "))
r = diametre/2

#Calculem la superficie amb la seva formula
superficie = math.pi*r**2

print(f'La superfície de la teva pizza és de: {superficie:.2f}cm²')
