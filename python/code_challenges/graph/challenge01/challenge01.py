# Write here the code challenge solution
class Node:
    def __init__(self, value):
        self.value=value
    
    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex=vertex
        self.weight=weight

class Grahp:
    def __init__(self):
        self.adj_list={}

    def add_node(self,value):
        new_vertex = Node(value)
        self.adj_list[new_vertex]=[]
        return new_vertex

    def add_edge(self,node1,node2,weight=0):

        if not node1 in self.adj_list.keys():
            return f'node {node1} does not exist'
        
        if not node2 in self.adj_list.keys():
            return f'node {node2} does not exist'

        edge1=Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2=Edge(node1,weight)
        self.adj_list[node2].append(edge2)
    
    def BFS(self, root):
        '''this function will add the vertex in order root then neighbor then neighbor of neighbor, etc...'''
        vertex_array = []
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current.value not in vertex_array:
                vertex_array.append(current.value)
                for edge in self.adj_list[current]:
                    queue.append(edge.vertex)
        return vertex_array

