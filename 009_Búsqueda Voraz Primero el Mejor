# Representación de un grafo simple (diccionario de nodos y sus vecinos)
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Función heurística: Distancia estimada desde un nodo al objetivo (en este caso, 'F')
def heuristica(nodo):
    # Puedes usar una heurística simple como la distancia en línea recta
    # o la cantidad de nodos vecinos al objetivo
    if nodo == 'F':
        return 0
    elif nodo == 'E':
        return 2
    else:
        return float('inf')  # Infinito para nodos no explorados

# Algoritmo Búsqueda Voraz Primero el Mejor
def greedy_best_first_search(grafo, inicio, objetivo):
    frontera = [inicio]  # Inicializamos la frontera con el nodo inicial

    while frontera:
        nodo_actual = frontera.pop(0)  # Tomamos el primer nodo de la frontera

        if nodo_actual == objetivo:
            return True  # Hemos encontrado el objetivo
        else:
            # Ordenamos los vecinos según la heurística (más cercano al objetivo primero)
            vecinos_ordenados = sorted(grafo[nodo_actual], key=heuristica)
            frontera.extend(vecinos_ordenados)  # Agregamos los vecinos a la frontera

    return False  # No se encontró el objetivo

# Ejemplo de uso
inicio = 'A'
objetivo = 'F'
if greedy_best_first_search(grafo, inicio, objetivo):
    print(f"Se encontró un camino desde {inicio} hasta {objetivo}.")
else:
    print(f"No se encontró un camino desde {inicio} hasta {objetivo}.")

