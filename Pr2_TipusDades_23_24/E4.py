"""
Jofre Aleman i Daniel Arco
09/10/2023
ASXIc M03-UF1 A2 pr2

Exercici 4: Escriu un programa que llegeixi l'edat de l'usuari i mostri si té edat per treballar, l'edat mínima per treballar
legalment és 16 i suposarem l'edat màxima als 65.
Consultar: Python If Statement. La sentència if es veurà a més detalls
 en el proper tema.
 """

#Demanem l'edat
edat = int(input("Això es un programa que et diu si tens edat per traballar o no. Introdueix la teva edat: "))

#Mirem si es menor o major de 16 o 65 per saber si pot o no treballar
if edat < 16 or edat > 65:
    print("No tens l'edat suficient per traballar.")
else:
    print("Estas en el rang d'edat per treballar. ")