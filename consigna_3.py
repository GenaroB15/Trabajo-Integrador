# =========================================
# MATRIZ CON LOS TIEMPOS DE EJECUCIÓN
# =========================================

# Cada fila representa una función
# Cada columna representa un servidor

tiempos = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]

# ==================================================
# PROMEDIO DE TIEMPO POR FUNCIÓN (POR FILAS)
# ==================================================

# Muestra un título en pantalla
print("Tiempo promedio de cada función:")

# Recorre cada fila de la matriz
for fila in range(len(tiempos)):

    # Variable para acumular la suma
    acumulador = 0

    # Recorre cada columna de la fila actual
    for columna in range(len(tiempos[fila])):

        # Suma cada valor de la fila
        acumulador = acumulador + tiempos[fila][columna]

    # Calcula el promedio de la fila
    resultado = acumulador / len(tiempos[fila])

    # Muestra el promedio de cada función
    print("Función", fila + 1, "->", resultado, "milisegundos")


# ==================================================
# PROMEDIO DE TIEMPO POR SERVIDOR (POR COLUMNAS)
# ==================================================

# Salto de línea + título
print("\nTiempo promedio de cada servidor:")

# Cantidad total de filas
filas_totales = len(tiempos)

# Cantidad total de columnas
columnas_totales = len(tiempos[0])

# Recorre cada columna
for columna in range(columnas_totales):

    # Reinicia el acumulador
    acumulador = 0

    # Recorre todas las filas
    for fila in range(filas_totales):

        # Suma los valores de la columna actual
        acumulador = acumulador + tiempos[fila][columna]

    # Calcula el promedio de cada columna
    resultado = acumulador / filas_totales

    # Muestra el promedio del servidor
    print("Servidor", columna + 1, "->", resultado, "milisegundos")
