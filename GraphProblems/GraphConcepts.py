'''
Created on Jan 1, 2018

@author: S528358
'''
class Graph():
    def __init__(self,graph_dict):
        if graph_dict is None:
            self.graph_dict = {}
        self.graph_dict = graph_dict
    
    def vertices(self):
        return list(self.graph_dict.keys())
    
    def edges(self):
        return self.generate_edges()
    
    def add_vertex(self,vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
            
    def add_edge(self,edge):
        '''assume edge is of type list'''
        [vertex1, vertex2] = edge
        if vertex1 not in self.graph_dict:
            self.graph_dict[vertex1] = [vertex2]
        else:
            self.graph_dict[vertex1].append(vertex2)
    
    def generate_edges(self):
        edges = []
        for i in self.graph_dict:
            for j in self.graph_dict[i]:
                if (i,j) not in edges:
                    edges.append((i,j))
        return edges
    
    def find_path(self, start, end , path = []):
#         print('start=',start)       
        if path is None:
            path = []
        path.append(start)
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        for i in self.graph_dict[start]:
#             print(start, self.graph_dict[start], path)            
            if i not in path:
                extended_path = self.find_path(i, end, path)
                if extended_path:
                    return extended_path  
#         print('print once')                         
        return None
    
    def find_all_paths(self,start, end, path=[]): 
        if path is None:
            path = []
        path.append(start)
        if start == end:
            return path
        if start not in self.graph_dict:
            return []
        paths = []
        for i in self.graph_dict[start]:
            if i not in path:
                extended_path = self.find_all_paths(i, end, path)
                for p in extended_path:
                    paths.append(p)
        return paths
    def degree_vertex(self,vertex):
        if vertex in self.graph_dict:
            return len(self.graph_dict[vertex])+self.graph_dict[vertex].count(vertex)
    
    def find_isolatedvertices(self):
        isolated = []
        for vertex in self.graph_dict:
            if not self.graph_dict[vertex]:
                isolated.append(vertex)
        return isolated
                         
g = {
    'a':['d'],
    'b':['c'],
    'c':['c', 'b', 'd', 'e'],
    'd':['a', 'c'],
    'e':['c'],
    'f':[]
    }
graph = Graph(g)
# print(graph.vertices())
# print(graph.edges())
print(graph.find_path('c', 'e'))
print(graph.find_all_paths('a','b'))
print(graph.degree_vertex('c'))
print(graph.find_isolatedvertices())