# Implementación simplificada del algoritmo de Prim

# Definir el grafo como un diccionario de adyacencia
grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 5},
    'C': {'A': 3, 'B': 4, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Función para encontrar el árbol de expansión mínima de Prim
def prim(grafo):
    arbol_expansion = {}
    nodos_visitados = set(list(grafo.keys())[0])  # Empezar desde el primer nodo del grafo

    while len(nodos_visitados) < len(grafo):
        menor_arista = None
        for nodo in nodos_visitados:
            for vecino, peso in grafo[nodo].items():
                if vecino not in nodos_visitados:
                    if menor_arista is None or peso < menor_arista[2]:
                        menor_arista = (nodo, vecino, peso)
        
        if menor_arista:
            nodo_origen, nodo_destino, peso = menor_arista
            arbol_expansion[(nodo_origen, nodo_destino)] = peso
            nodos_visitados.add(nodo_destino)

    return arbol_expansion

arbol_minimo = prim(grafo)
print("Árbol de expansión mínima (Aristas y Pesos):")
for arista, peso in arbol_minimo.items():
    print(arista, "-", peso)
