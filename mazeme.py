class Grafo3D:
    def __init__(self):
        self.nodi = set()
        self.archi = {}

    def aggiungi_nodo(self, x, y, z):
        nodo = (x, y, z)
        self.nodi.add(nodo)
        if nodo not in self.archi:
            self.archi[nodo] = set()

    def aggiungi_arco(self, nodo1, nodo2):
        self.aggiungi_nodo(*nodo1)
        self.aggiungi_nodo(*nodo2)
        self.archi[nodo1].add(nodo2)

    def vicini(self, nodo):
        return self.archi.get(nodo, set())

    def __str__(self):
        return f'Nodi: {self.nodi}\nArchi: {self.archi}'
