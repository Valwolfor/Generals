#Encontrará algunos codigos resumidos y con un comentario al inicio que los describe.

# 1. Mach como remplazo de if elif que hacía de swich en  Py
# print("Ingrese un número entero")
# num = int(input())

# def numero_pos_neg_par_impar(numero):
#     match numero:
#         case 404:
#             return "solicitud incorrecta"
#         case _: # el _ es el else o contrario.
#             return "No encontrado"
        
# print(numero_pos_neg_par_impar(404))

# 2. Uso de FOR, especialmente cuando se conoce el numero de iteraciones o listas
from __future__ import barry_as_FLUFL
from collections import Counter


dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"] #Lista es con []

for i in dias:
    print(i)
    if i == "Viernes":  #para hacer un punto de corte.
        break
    
for i in dias:
    if i == "Viernes": #para encontrar una posición
        break
    print(i)