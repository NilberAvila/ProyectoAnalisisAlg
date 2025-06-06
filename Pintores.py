def sumatoria(desde, hasta, tablas):
    total = 0
    for i in range(desde, hasta + 1):
        total += tablas[i]
    return total

def calcular_tiempo(cant_tablas, cant_pintores, tablas):
    tabla_tiempos = [[0] * (cant_tablas + 1) for _ in range(cant_pintores + 1)]
    
    for i in range(1, cant_tablas + 1):
        tabla_tiempos[1][i] = sumatoria(0, i - 1, tablas)
    
    for i in range(1, cant_pintores):
        tabla_tiempos[i][1] = tablas[0]
    
    for i in range(2, cant_pintores + 1):
        for tabla in range(2, cant_tablas + 1):
            mejor = float('inf')
            for n in range(1, tabla):
                mejor = min(mejor, max(tabla_tiempos[i - 1][n], sumatoria(n, tabla - 1, tablas)))
            tabla_tiempos[i][tabla] = mejor
    
    return tabla_tiempos[cant_pintores][cant_tablas]


tablas = [2, 2, 2, 2]
cant_tablas = len(tablas)
cant_pintores = 3

resultado = calcular_tiempo(cant_tablas, cant_pintores, tablas)
print(f"El tiempo mínimo para pintar con {cant_pintores} pintores es: {resultado}")