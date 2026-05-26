M = [
    [120,150,100],
    [200,180,220],
    [90,110,95]
]

C = [
    [30,20,10],
    [15,25,20],
    [40,10,30]
]

print("Promedio por funcion")

for g in range(3):

    tiempo_total = 0
    cantidad_total = 0

    for b in range(3):

        tiempo_total += (M[g][b] * C[g][b])

        cantidad_total += C[g][b]

    promedio = tiempo_total / cantidad_total

    print(promedio)

print("Promedio por servidor")

for b in range(3):

    tiempo_total = 0
    cantidad_total = 0

    for g in range(3):

        tiempo_total += (M[g][b] * C[g][b])

        cantidad_total += C[g][b]

    promedio = tiempo_total / cantidad_total

    print(promedio)