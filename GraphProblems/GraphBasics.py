'''
Created on Jun 8, 2018

@author: S528358
'''
from django.urls.conf import path
from matplotlib.path import Path
class Graph:
    def __init__(self,graph=None):
        if graph is None:
            self.graph = {}
        else:
            self.graph = graph
    
    def vertices(self):
        return list(self.graph.keys())
    
    def edges(self):
        return self.generate_edges()
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.graph[vertex1] = [vertex1]
        else:
            self.graph[vertex1].append(vertex2)
            
    def generate_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbors in self.graph[vertex]:
                edges.append([vertex, neighbors])
        return edges
    
    def find_paths(self,start, end, path=None):
        if path is None:
            path = []
        path.append(start)
        if start == end:
            return path
        if start not in self.graph:
            return None
        for vertex in self.graph[start]:
            if vertex not in path:
                print('visited vertices =',vertex)
                extended_path = self.find_paths(vertex, end, path)
                if extended_path:
                    return extended_path
                
    def find_all_paths(self,start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
#         path.append(start)
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for vertex in self.graph[start]:
            if vertex not in path:
#                 print('visited nodes = ', vertex)
                all_paths = self.find_all_paths(vertex, end, path)
                for i in all_paths:
                    paths.append(i)
        return paths
    
    def vertex_degree(self,vertex):
        return len(self.graph[vertex]) + self.graph[vertex].count(vertex)
    
    def find_isolated_vertices(self):
        isolated = []
        for vertex in self.graph:
            if len(self.graph[vertex]) == 0:
                isolated.append(vertex)
        return isolated
    
    
            
g = {
    'a' : ['d', 'f'],
    'b' : ['c'],
    'c' : ['b', 'c', 'd', 'e'],
    'd' : ['a', 'c'],
    'e' : ['c'],
    'f' : ['d']
    }
graph = Graph(g)
# print('edges', graph.generate_edges())
print('path = ', graph.find_paths('q', 'z'))
print('all paths = ', graph.find_all_paths('a', 'b'))