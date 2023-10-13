"""
Jofre Aleman i Daniel Arco
09/10/2023
ASXIc M03-UF1 A2 pr2

Exercici 5: Demana una paraula per teclat i mostrar-la per pantalla, canviar les vocals per als numèrics 1, 2, 3, 4 o 5.
Tenint en compte, que la lletra a i A és l'1, consecutivament fins a la lletra u i U que és el 5.
"""


paraula = input("Escriu una paraula. El que farà aquest programa serà substituir les vocals de la paraula per "
                     "als númerics 1, 2, 3, 4 o 5.\n"
                     "La lletra A és l'1, consecutivament fins la lletra U que és el 5:  ")

paraula_cambiada = ""

for lletra in paraula:
    if lletra == 'a' or lletra == 'A':
        paraula_cambiada += '1'
    elif lletra == 'e' or lletra == 'E':
        paraula_cambiada += '2'
    elif lletra == 'i' or lletra == 'I':
        paraula_cambiada += '3'
    elif lletra == 'o' or lletra == 'O':
        paraula_cambiada += '4'
    elif lletra == 'u' or lletra == 'U':
        paraula_cambiada += '5'
    else:
        paraula_cambiada += lletra

print("La paraula amb les vocals canviades és:", paraula_cambiada)
