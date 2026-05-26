tiempos = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]
print("Tiempo promedio de cada función:")

for fila in range(len(tiempos)):

    acumulador = 0

    for columna in range(len(tiempos[fila])):
        acumulador = acumulador + tiempos[fila][columna]

    resultado = acumulador / len(tiempos[fila])

    print("Función", fila + 1, "->", resultado, "milisegundos")
print("\nTiempo promedio de cada servidor:")
filas_totales = len(tiempos)
columnas_totales = len(tiempos[0])
for columna in range(columnas_totales):

    acumulador = 0

    for fila in range(filas_totales):
        acumulador = acumulador + tiempos[fila][columna]

    resultado = acumulador / filas_totales

    print("Servidor", columna + 1, "->", resultado, "milisegundos")