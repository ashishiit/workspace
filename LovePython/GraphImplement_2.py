'''
Created on Jan 20, 2017

@author: S528358
'''
class Vertex:
    def __init__(self,data):
        self.data = data
        self.connectedTo = {}
    def AddNeighbor(self,nbr,weight):
        if nbr not in self.connectedTo:
            self.connectedTo[nbr] = weight
class Graph:
    def __init__(self):
        self.numVertices = 0
        self.Vertices = {}
    def Add_Vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.data not in self.Vertices:
            self.Vertices[vertex.data] = vertex
            return True
        else:
            return False
    def Add_Edge(self, start, end, weight):
        if start in self.Vertices and end in self.Vertices:
            for key, value in self.Vertices.items():
                if key == start:
                    value.AddNeighbor[end,weight]
                if key == end:
                    value.AddNeighbor[start,weight]
            return True
        else:
            return False
    def Print_Graph(self):
        for key in 