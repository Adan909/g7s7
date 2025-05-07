import time

# Función para mostrar el progreso de carga
def carga():
    puntos = ""
    for i in range(1, 11):
        puntos += "."  # Agregar un punto por cada iteración
        porcentaje = i * 10  # Calcula el porcentaje
        print(f"Cargando{puntos} {porcentaje}%")
        time.sleep(0.5)  # Espera medio segundo antes de continuar

# Llamar a la función
carga()
