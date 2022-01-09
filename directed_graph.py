from collections import defaultdict, deque, Counter

class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacent = []

    def addEdge(self, vertex):
        self.adjacent.append(vertex)

    def getEdges(self, vertex):
        return self.adjacent

class Directed_Graph:
    def __init__(self):
        self.vertexes = []

    def addVertex(self, vertex):
        self.vertexes.append(vertex)

    def getAllAdjacent(self, vertex):
        return self.find(vertex).getEdges(vertex)


    