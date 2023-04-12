
            ### Implementation of Ford Fulkerson Algorithm ###

from collections import defaultdict

# This class represents a directed graph using adjacency matrix representation
class Graph:

    def __init__(self, graph):
        self.graph = graph              # residual graph
        self. ROW = len(graph)
        # self.COL = len(gr[0])         # returns true if there is a path from source 's' to sink 't'
                                        # in residual graph + fills parent[] to store the path
        

    # Using BFS as a searching algo
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)  # mark all the vertices as not visited
        queue = []                      # create a queue for BFS


        queue.append(s)
        visited[s] = True               # mark the source node as visited and enqueue it

        while queue:                    # standard BFS Loop

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying FF algo
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 5

print("Max Flow: %d " % g.ford_fulkerson(source, sink))