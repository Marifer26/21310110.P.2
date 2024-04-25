# Definimos la función de búsqueda en profundidad limitada (BPL).
def bpl(grafo, inicio, fin, limite, visitado=None):
    # Si es la primera vez que se llama a la función, inicializamos el conjunto de nodos visitados.
    if visitado is None:
        visitado = set()
    # Agregamos el nodo de inicio al conjunto de nodos visitados.
    visitado.add(inicio)
    # Si el nodo de inicio es igual al nodo final, hemos encontrado un camino y devolvemos True.
    if inicio == fin:
        return True
    # Si hemos alcanzado el límite de profundidad, detenemos la búsqueda y devolvemos False.
    if limite <= 0:
        return False
    # Recorremos cada nodo vecino del nodo de inicio que aún no ha sido visitado.
    for siguiente in grafo[inicio] - visitado:
        # Llamamos a la función bpl de forma recursiva con el nodo vecino como nuevo nodo de inicio y reducimos el límite en 1.
        # Si esta llamada devuelve True, hemos encontrado un camino y devolvemos True.
        if bpl(grafo, siguiente, fin, limite - 1, visitado):
            return True
    # Si hemos recorrido todos los nodos vecinos y no hemos encontrado un camino, devolvemos False.
    return False

# Definimos la función de búsqueda en profundidad iterativa (BPI).
def bpi(grafo, inicio, fin, limite_maximo):
    # Para cada profundidad desde 1 hasta el límite máximo...
    for limite in range(1, limite_maximo + 1):
        # Llamamos a la función bpl con el nodo de inicio, el nodo final y el límite de profundidad actual.
        # Si la función devuelve True, significa que existe un camino desde el nodo de inicio hasta el nodo final dentro del límite de profundidad, y devolvemos True.
        if bpl(grafo, inicio, fin, limite):
            return True
    # Si hemos probado todas las profundidades hasta el límite máximo y no hemos encontrado un camino, devolvemos False.
    return False

# Definimos un grafo más complejo como un diccionario, donde cada clave es un nodo y cada valor es un conjunto de nodos vecinos.
grafo = {
    'A': set(['B', 'C', 'D']),
    'B': set(['A', 'E', 'F']),
    'C': set(['A', 'G', 'H']),
    'D': set(['A', 'I']),
    'E': set(['B', 'J']),
    'F': set(['B', 'K', 'L']),
    'G': set(['C']),
    'H': set(['C']),
    'I': set(['D']),
    'J': set(['E']),
    'K': set(['F']),
    'L': set(['F']),
}

# Definimos el nodo de inicio, el nodo final y el límite máximo de profundidad.
inicio = 'A'
fin = 'L'
limite_maximo = 3

# Llamamos a la función bpi con el nodo de inicio, el nodo final y el límite máximo de profundidad, e imprimimos el resultado.
# Si la función devuelve True, significa que existe un camino desde el nodo de inicio hasta el nodo final dentro del límite máximo de profundidad.
# Si la función devuelve False, significa que no existe tal camino dentro del límite máximo de profundidad.
print(bpi(grafo, inicio, fin, limite_maximo))

