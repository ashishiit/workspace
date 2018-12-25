'''
Created on Dec 26, 2017

@author: S528358
'''
class Graph:
    def __init__(self, graph_dict = None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict
#         self.graph_dict = {}
    def vertices(self):
        return list(self.graph_dict.keys())
    def edges(self):
        edges = []
        for i in self.graph_dict:
            for j in self.graph_dict[i]:
                edges.append([i,j])
        return edges
    def add_vertex(self,vertex):
        self.graph_dict[vertex] = []
    def add_edge(self, edge ):
        [vertex1, vertex2] = edge
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]
g = {
    'a' : ['c'],
    'b' : ['c', 'e'],
    'c' : ['a', 'b', 'd', 'e'],
    'd' : ['c'],
    'e' : ['b', 'c'],
    'f' : []
    }
G = Graph(g)
print (G.vertices())
print(G.edges())
print(G.add_vertex('g'))
print(G.vertices())
print(G.add_edge(['a','b']))
print(G.edges())
print(G.add_edge(['x','y']))
print(G.vertices())
print(G.edges())