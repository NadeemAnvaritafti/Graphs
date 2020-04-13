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
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        ss = Stack()
        ss.push(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While stack is not empty...
        while ss.size() > 0:
            # Pop the first vertex
            vert = ss.pop()
            # If that vertex has not been visited...
            if vert not in visited:
                # Mark as visited
                print(vert)
                visited.add(vert)
                # Then add all of its neighbors to the top of the stack
                for next_vert in self.get_neighbors(vert):
                    ss.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Base case
        if visited is None:
            # Create an empty Set to store visited verticies
            visited = set()
        # If vertex has not been added to visited...
        if starting_vertex not in visited:
            # Add starting vertex to visited
            visited.add(starting_vertex)
            print(starting_vertex)
            # Find neighbors to starting vertex
            for next_vert in self.get_neighbors(starting_vertex):
                # Recursively call function on new verticies
                self.dft_recursive(next_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH to the starting vertex ID
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a Set to store visited verticies
        visited = set()
        # While the queue is not empty...
        while qq.size() > 0:
            # Dequeue the first PATH
            path = qq.dequeue()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # If so, return the path
                    return path
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH to its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    # COPY THE PATH and append the new vertex
                    new_path = path.copy()
                    new_path.append(next_vert)
                    # Append the neighbor to the back
                    qq.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH to the starting vertex ID
        ss = Stack()
        ss.push([starting_vertex])
        # Create a Set to store visited verticies
        visited = set()
        # While the queue is not empty...
        while ss.size() > 0:
            # Pop the first PATH
            path = ss.pop()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # If so, return the path
                    return path
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH to its neighbors to the top of the stack
                for next_vert in self.get_neighbors(v):
                    # COPY THE PATH and append the new vertex
                    new_path = path.copy()
                    new_path.append(next_vert)
                    # Add the neighbor to the top of the stack
                    ss.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initialize visited if it's not yet initialized
        if visited is None:
            visited = set()

        # initialize path if it's not yet initialized
        if path is None:
            path = []
        # Check if starting vertex has been visited
        if starting_vertex not in visited:
            # Add starting vertex to visited
            visited.add(starting_vertex)
            # Add starting vertex to the path
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            # Check if starting vertex is the target
            if starting_vertex == destination_vertex:
                return path_copy
            # Find neighbors of starting vertex
            for neighbor in self.get_neighbors(starting_vertex):
                # Recursively call function
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path

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
