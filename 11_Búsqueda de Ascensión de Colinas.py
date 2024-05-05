# Definición del grafo (representado como un diccionario)
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

# Función para calcular el costo total de una ruta
def calcular_costo(ruta):
    costo_total = 0
    for i in range(len(ruta) - 1):
        costo_total += grafo[ruta[i]][ruta[i + 1]]
    return costo_total

# Algoritmo de Ascensión de Colinas
def ascenso_colinas(grafo, inicio):
    nodo_actual = inicio
    ruta_actual = [inicio]

    while True:
        vecinos = list(grafo[nodo_actual].keys())
        mejor_vecino = None
        mejor_costo = float('inf')

        for vecino in vecinos:
            if vecino not in ruta_actual:
                ruta_candidata = ruta_actual + [vecino]
                costo_candidato = calcular_costo(ruta_candidata)
                if costo_candidato < mejor_costo:
                    mejor_vecino = vecino
                    mejor_costo = costo_candidato

        if mejor_vecino is None:
            break  # No hay mejora, terminamos
        else:
            nodo_actual = mejor_vecino
            ruta_actual.append(mejor_vecino)

    return ruta_actual

# Ejemplo de uso
inicio = 'A'
ruta_optima = ascenso_colinas(grafo, inicio)
costo_optimo = calcular_costo(ruta_optima)

print(f'Ruta óptima: {ruta_optima}')
print(f'Costo óptimo: {costo_optimo}')

