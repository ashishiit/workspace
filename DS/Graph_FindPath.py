'''
Created on Dec 26, 2017

@author: S528358
'''
from django.urls.conf import path
from matplotlib.path import Path
class Graph:
    def __init__(self, dict_graph = None):
        if dict_graph is None:
            self.graph_dict = {}
        else:
            self.graph_dict = dict_graph
    def addVertex(self,vertex):
        self.graph_dict[vertex] = []
    def addEdge(self, edge):
        [vertex1, vertex2] = edge
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]
    def Vertices(self):
        return list(self.graph_dict.keys())
    def Edges(self):
        edges = []
        for i in self.graph_dict:
            for j in self.graph_dict[i]:
                edges.append([i,j])
        return edges
    def graph_find_path(self,start_vertex, end_vertex, path = None):
        if path is None:
            path = []
        path.append(start_vertex)
        if start_vertex not in self.graph_dict:
            return None
        
        if start_vertex == end_vertex:
            return path
        for i in self.graph_dict[start_vertex]:
            if i not in path:
                print('start = ',i)
                extended_path = self.graph_find_path(i, end_vertex, path)
                if extended_path:
                    return path
                
#         print('start = ',start_vertex)
        return None
input_g = {
    'a':['d'],
    'b':['c'],
    'c':['b','c','d','e'],
    'd':['a','c'],
    'e':['c'],
    'f':[]
    }
g = Graph(input_g)
print(g.Edges())
print(g.Vertices())
print(g.graph_find_path('a', 'f'))