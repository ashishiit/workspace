'''
Created on May 15, 2018

@author: S528358
'''
class Graph:
    def __init__(self,graph_dict=None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict
    def mst(self):
        
        for i in range(len(self.graph_dict)):
            visited = []
            s = []
            s.append(list(self.graph_dict)[i])
            while len(s)>0:
                item = s.pop()
                visited.append(item)
                for i in self.graph_dict[item]:
                    if i not in visited:
                        print(item,i)
                        visited.append(i)
                        s.append(i)
                        print()
    #                     self.mst(i)
                        break
#                 
g = {
    'a':['b', 'c', 'd', 'e'],
    'b':['a', 'c', 'd', 'e'],
    'c':['a', 'b', 'd', 'e'],
    'd':['a', 'b', 'c', 'e'],
    'e':['a', 'b', 'c', 'd']
    }
graph = Graph(g)
graph.mst()