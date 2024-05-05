# Definimos la clase Nodo
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = []

    # Añadimos vecinos al nodo
    def añadir_vecino(self, vecino):
        if vecino not in self.vecinos:
            self.vecinos.append(vecino)
            vecino.añadir_vecino(self)

# Definimos la función de búsqueda bidireccional
def busqueda_bidireccional(nodo_inicio, nodo_objetivo):
    # Creamos dos conjuntos para almacenar los nodos visitados desde el inicio y el objetivo
    visitados_inicio = {nodo_inicio}
    visitados_objetivo = {nodo_objetivo}

    # Creamos dos listas para almacenar los nodos a visitar desde el inicio y el objetivo
    a_visitar_inicio = [nodo_inicio]
    a_visitar_objetivo = [nodo_objetivo]

    while a_visitar_inicio and a_visitar_objetivo:
        # Visitamos el siguiente nodo desde el inicio
        nodo_actual_inicio = a_visitar_inicio.pop(0)
        for vecino in nodo_actual_inicio.vecinos:
            if vecino in visitados_objetivo:
                return True  # Encontramos un camino
            if vecino not in visitados_inicio:
                visitados_inicio.add(vecino)
                a_visitar_inicio.append(vecino)

        # Visitamos el siguiente nodo desde el objetivo
        nodo_actual_objetivo = a_visitar_objetivo.pop(0)
        for vecino in nodo_actual_objetivo.vecinos:
            if vecino in visitados_inicio:
                return True  # Encontramos un camino
            if vecino not in visitados_objetivo:
                visitados_objetivo.add(vecino)
                a_visitar_objetivo.append(vecino)

    return False  # No encontramos un camino

# Creamos algunos nodos
nodoA = Nodo("A")
nodoB = Nodo("B")
nodoC = Nodo("C")
nodoD = Nodo("D")
nodoE = Nodo("E")

# Añadimos vecinos a los nodos
nodoA.añadir_vecino(nodoB)
nodoB.añadir_vecino(nodoC)
nodoC.añadir_vecino(nodoD)
nodoD.añadir_vecino(nodoE)

# Realizamos la búsqueda bidireccional
print(busqueda_bidireccional(nodoA, nodoE))  # Debería imprimir: True

