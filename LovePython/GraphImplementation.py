'''
Created on Jan 20, 2017

@author: S528358
'''
class Vertex:
    def __init__(self,data):
        self.data = data
        self.connectedTo = {}
    def AddNeighbor(self, nbr, weight):
        self.connectedTo[nbr] = weight
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.data
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0
    def AddVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
#         return newVertex
    def AddEdge(self, start, end, weight):
        if start not in self.vertexList:
            self.AddVertex(start)
        if end not in self.vertexList:
            self.AddVertex(end)
        self.vertexList[start].AddNeighbor(self.vertexList[end],weight)
    
    def getVertices(self):
#         return self.vertexList.keys()
        print('***vertices***')
        for i in self.vertexList:
            print(i)
        print('**************')
    def __iter__(self):
        return iter(self.vertexList.values())
g = Graph()
for i in range(6):
    g.AddVertex(i)

# g.getVertices()
g.AddEdge(0, 1, 5)
g.AddEdge(0, 4, 1)
g.AddEdge(0, 5, 2)
g.AddEdge(1, 2, 4)
g.AddEdge(2, 3, 9)
g.AddEdge(2, 5, 1)
g.AddEdge(3, 5, 3)
g.AddEdge(3, 4, 7)
g.AddEdge(4, 5, 8)
# print(g.connectedTo())
print(g)
# print(g.numVertices)
print(g.vertexList)
print(g.vertexList.keys())
print(g.vertexList.values())
for v in g:
#     print(v)
    for w in v.getConnections():
        print("( %d , %d )" % (v.getId(), w.getId()))