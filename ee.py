import datetime as dt
import time 
import os

cant = int(input("Cuantas notas :"))
fecha = dt.date.today ()
print(f"Fecha actual: {fecha}") 

suma = 0
for i in range(cant):
    nota = int(input(f"Ingresa la calificacion:{i + 1}:"))
    suma += nota
    
promedio = suma /cant
max_pasos = 10
cont = 0
tiempo_espera = 3
while cont < max_pasos:
    os.system("cls||clear")
    print("Calculando promedio",end="")
    print(f"."* (cont + 1), end =" ")
    print(f"{(cont + 1) * 10:<11} %")
    time.sleep(1)
    cont += 1
    
print("El promedio es: ", promedio)