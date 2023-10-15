"""
Jofre Aleman i Daniel Arco
09/10/2023
ASXIc M03-UF1 A2 pr2

Exercici 3:Escriu un programa que llegeixi 5 enters. El primer i el segon creen un rang, el tercer i el quart creen un
altre rang. Mostra True si el cinquè valor, està comprès dins els dos rangs, si no False
"""

llista = input("Escriu una llista de 5 nombres enters aleatoris, separats entre ells per ',': ")

#Separem els valors amb la ,
llista_valors = llista.split(',')

# Converteix els element a enters
llista_valors = [int(valor) for valor in llista_valors]

#Determinem el "rang"
llista1 = llista_valors[:2]
llista2 = llista_valors[2:4]
llista3 = llista_valors[-1]

print("llista1:", llista1)
print("llista2:", llista2)
print("llista3:", llista3)

#Mirem si l'ultim valor esta dins dels dos rangs o no
if (min(llista1) <= llista3 <= max(llista1)) and (min(llista2) <= llista3 <= max(llista2)):
    print("True")
else:
    print("False")