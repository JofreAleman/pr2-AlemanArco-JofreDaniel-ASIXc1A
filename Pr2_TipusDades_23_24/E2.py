"""
Jofre Aleman i Daniel Arco
09/10/2023
ASXIc M03-UF1 A2 pr2

Exercici 2: Per poder fer un estudi de la ventilació d'una aula necessitem poder calcular la quantitat d'aire que hi cap en
una habitació. Llegeix les 3 dimensions de l'aula i mostra per pantalla quin volum té.
Cal mostrar per pantalla: “El volum de l’aula és xxx m3
"""

print("Per fer un estudi de la ventilació duna aula, necessitem calcular el volum d'aquesta. Si us plau introdueix les "
      "dades següents. ")

#Demanem les dades necessaries
b = float(input("Introdueix la base de la habitació: "))
h = float(input("Introdueix l'altura de la habitació: "))
a = float(input("Introdueix l'amplada de l'habitació: "))

#Calculem el volum amb la seva formula
volum = a * b * h

print(f"El volum de l'habitació té un total de {volum} m³.")

