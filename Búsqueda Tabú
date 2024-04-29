# DEFINIENDO EL GRAFO MEDIANTE UN DICCIONARIO DE PYTHON:
# Cada clave representa un nodo, y su valor es una lista de tuplas (nodo_adyacente, costo).
grafo = {
    'a': [('p', 4), ('j', 15), ('b', 1)],
    'b': [('a', 1), ('d', 2), ('e', 2), ('c', 3)],
    'j': [('a', 15)],
    'p': [('a', 4)],
    'd': [('b', 2), ('g', 3)],
    'e': [('b', 2), ('g', 4), ('f', 5), ('c', 2)],
    'c': [('b', 3), ('e', 2), ('f', 5), ('i', 20)],
    'g': [('d', 3), ('e', 4), ('f', 10), ('h', 1)],
    'f': [('g', 10), ('e', 5), ('c', 5)],
    'i': [('c', 20)],
    'h': [('g', 1)]
}

# MUESTRA EL GRAFO ANTES DEL RECORRIDO
print("Muestra el grafo antes del recorrido:\n")
for key, lista in grafo.items():
    print(key)
    print(lista)

visitados = []
cola = []

# Ingresa el nodo origen
origen = input("Ingresa el nodo origen: ")
print("\nLista de recorrido en anchura:\n")

# Colocamos el vértice origen en una cola
cola.append(origen)

#  Mientras la cola no esté vacía
while cola:
    # Desencolamos un vértice, este será ahora el vértice actual
    actual = cola.pop(0)

    # Si el vértice actual no ha sido visitado
    if actual not in visitados:
        # Procesamos (imprimimos) el vértice actual
        print("Vertice actual ->", actual)
        # Colocamos el vértice actual en la lista de visitados
        visitados.append(actual)
        # Para cada vértice que el vértice actual tiene como destino
        for key, _ in grafo[actual]:
            # Encolamos el vértice si no ha sido visitado
            if key not in visitados:
                cola.append(key)





