"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = []
        queue = Queue()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            item = queue.dequeue()
            if item not in visited:
                visited.append(item)
                print(item)
                for adj in self.vertices[item]:
                    queue.enqueue(adj)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = []
        stack = Stack()
        stack.push(starting_vertex)
        while stack.size() > 0:
            item = stack.pop()
            if item not in visited:
                visited.append(item)
                print(item)
                for adj in self.vertices[item]:
                    stack.push(adj)
            

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if not visited:
            visited = []
        print(starting_vertex)
        visited.append(starting_vertex)
        for adj in self.vertices[starting_vertex]:
            if adj not in visited:
                self.dft_recursive(adj, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = []
        queue = Queue()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            path = queue.dequeue()
            v = path[-1]
            if v not in visited:
                for adj in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(adj)
                    queue.enqueue(new_path)
                    if adj == destination_vertex:
                        return new_path

                visited.append(v)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = []
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            v = path[-1]
            if v not in visited:
                visited.append(v)
                for adj in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(adj)
                    stack.push(new_path)
                    if adj == destination_vertex:
                        return new_path

                

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if not path:
            path = []
        if not visited:
            visited = []
        path.append(starting_vertex)
        if starting_vertex == destination_vertex:
            return path
        if starting_vertex not in visited:
            visited.append(starting_vertex)
        for adj in self.vertices[starting_vertex]:
            if adj not in visited:
                new_path = list(path)
                next_path = self.dfs_recursive(adj, destination_vertex, new_path, visited)
                if next_path:
                    return next_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
