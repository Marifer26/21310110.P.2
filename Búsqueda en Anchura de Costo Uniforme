import queue  # Importa el módulo queue de Python para usar colas de prioridad.

def busqueda_costo_uniforme(grafo, inicio, fin):  # Define la función de búsqueda de costo uniforme.
    cola_prioridad = queue.PriorityQueue()  # Crea una cola de prioridad vacía.
    cola_prioridad.put((0, inicio))  # Agrega el nodo inicial a la cola con un costo de 0.
    visitados = set()  # Crea un conjunto vacío para almacenar los nodos visitados.

    while not cola_prioridad.empty():  # Mientras la cola no esté vacía, sigue iterando.
        (costo, nodo_actual) = cola_prioridad.get()  # Obtiene el nodo con el menor costo de la cola.
        if nodo_actual not in visitados:  # Si el nodo actual no ha sido visitado...
            visitados.add(nodo_actual)  # ...lo agrega al conjunto de nodos visitados.

            if nodo_actual == fin:  # Si el nodo actual es el nodo final...
                return costo  # ...devuelve el costo para llegar a él.

            for vecino, costo_vecino in grafo[nodo_actual]:  # Para cada vecino del nodo actual...
                if vecino not in visitados:  # ...si el vecino no ha sido visitado...
                    costo_total = costo + costo_vecino  # ...calcula el costo total para llegar a él.
                    cola_prioridad.put((costo_total, vecino))  # ...y lo agrega a la cola con su costo total.

    return -1  # Si no se puede llegar al nodo final, devuelve -1.

# Ejemplo de uso
grafo = {
    'A': [('B', 1), ('C', 3)],  # Define un grafo como un diccionario.
    'B': [('A', 1), ('D', 2), ('E', 3)],
    'C': [('A', 3), ('F', 5)],
    'D': [('B', 2)],
    'E': [('B', 3), ('F', 1)],
    'F': [('C', 5), ('E', 1)]
}

inicio = 'A'  # Define el nodo de inicio.
fin = 'F'  # Define el nodo final.
resultado = busqueda_costo_uniforme(grafo, inicio, fin)  # Llama a la función con el grafo, el nodo de inicio y el nodo final.
print(f"El costo mínimo desde {inicio} hasta {fin} es {resultado}")  # Imprime el costo mínimo para ir del nodo de inicio al nodo final.


