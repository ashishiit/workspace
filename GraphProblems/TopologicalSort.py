'''
Created on May 16, 2018

@author: S528358
'''
class Graph:
    def __init__(self,graph_dict=None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict
    def topoSort(self):
        visited = []
        while len(self.graph_dict) > 0:
            for i in list(self.graph_dict):
                if len(self.graph_dict[i]) == 0:
                    visited.insert(0, i)
                    self.graph_dict.pop(i)
                    for j in list(self.graph_dict):
                        if i in self.graph_dict[j]:
                            self.graph_dict[j].remove(i)
        print(visited)

g = {
    'a':['d', 'e'],
    'b':['e'],
    'c':['f'],
    'd':['g'],
    'e':['g'],
    'f':['h'],
    'g':['h'],
    'h':[]
    }
graph = Graph(g)
graph.topoSort()