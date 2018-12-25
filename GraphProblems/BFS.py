'''
Created on May 12, 2018

@author: S528358
'''
class Graph():
    def __init__(self,graph_dict=None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict
    def bfs(self):
        visited = []
        q = []
        q.append(list(self.graph_dict)[0])
        while len(q)>0:
            item = q.pop(0)
            if item not in visited:
                visited.append(item)
                for i in self.graph_dict[item]:
                    q.append(i)
        return visited
                    
            
g = {
    'A':['B','D'],
    'B':['A','C'],
    'C':['B'],
    'D':['A','E'],
    'E':['D']
    }
graph = Graph(g)
print(graph.bfs())