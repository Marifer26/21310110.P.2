from collections import deque

def bfs(grafico, inicio, meta):
    visitado = set()  # Conjunto para almacenar los nodos visitados.
    cola = deque([[inicio]])  # Cola de caminos por verificar.

    if inicio == meta:  # Si el nodo de inicio es igual al nodo de meta.
        print("El nodo de inicio es igual al nodo de meta")
        return

    while cola:  # Mientras haya caminos por verificar.
        camino = cola.popleft()  # Obtenemos el primer camino de la cola.
        vertice = camino[-1]  # El último nodo del camino actual.

        if vertice not in visitado:  # Si el nodo no ha sido visitado.
            vecinos = grafico[vertice]  # Obtenemos los vecinos del nodo.

            for vecino in vecinos:  # Para cada vecino.
                nuevo_camino = list(camino)  # Creamos una copia del camino actual.
                nuevo_camino.append(vecino)  # Añadimos el vecino al final del camino.
                cola.append(nuevo_camino)  # Añadimos el nuevo camino a la cola.

                if vecino == meta:  # Si el vecino es el nodo de meta.
                    print("Camino desde {} hasta {}:".format(inicio, meta))
                    print(nuevo_camino)  # Imprimimos el camino.
                    return

            visitado.add(vertice)  # Marcamos el nodo como visitado.

    print("No hay camino desde {} hasta {}".format(inicio, meta))  # Si no encontramos un camino.

grafico = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B', 'G'},
    'E': {'B', 'H'},
    'F': {'C', 'I'},
    'G': {'D'},
    'H': {'E'},
    'I': {'F', 'J'},
    'J': {'I'},
}

bfs(grafico, 'A', 'J')

