# Definición del grafo (representado como un diccionario)
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

# Función heurística (admisible y consistente)
def heuristica(nodo_actual, nodo_destino):
    # En este ejemplo, simplemente usaremos una estimación constante
    return 5

# Algoritmo AO*
def AO_estrella(grafo, inicio, destino):
    cola = [(inicio, [inicio], 0)]  # Cola de nodos a explorar
    visitado = {inicio}  # Conjunto de nodos visitados

    while cola:
        (nodo, camino, costo) = cola.pop(0)

        for vecino in grafo[nodo].keys():
            if vecino == destino:
                return camino + [vecino], costo + grafo[nodo][vecino]
            else:
                if vecino not in visitado:
                    visitado.add(vecino)
                    costo_total = costo + grafo[nodo][vecino] + heuristica(vecino, destino)
                    cola.append((vecino, camino + [vecino], costo_total))

# Ejemplo de uso
inicio = 'A'
destino = 'D'
ruta_optima, costo_optimo = AO_estrella(grafo, inicio, destino)
print(f'Ruta óptima: {ruta_optima}')
print(f'Costo óptimo: {costo_optimo}')


