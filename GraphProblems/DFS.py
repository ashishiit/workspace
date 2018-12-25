'''
Created on May 13, 2018

@author: S528358
'''
class Graph:
    def __init__(self,graph_dict=None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict
    def dfs(self):
        visited = []
        s = []
        s.append(list(self.graph_dict)[0])
        while len(s)>0:
            item = s.pop()
            if item not in visited:
                visited.append(item)
                for i in self.graph_dict[item]:
                    s.append(i)
        return visited
        
g = {
    'A':['B','D'],
    'B':['A','C'],
    'C':['B'],
    'D':['A','E'],
    'E':['D']
    }
graph = Graph(g)
print(graph.dfs())