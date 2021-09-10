# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
 
# Library for INT_MAX
import sys
import time
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)
 

with open("Output/outDijkstra.csv", "w", encoding='utf-8') as output:
    files = ['10.txt',]
    ##files = ['10.txt', '25.txt', '50.txt','75.txt','100.txt','150.txt','200.txt','250.txt','300.txt','400.txt','500.txt','650.txt','800.txt','1000.txt','1500.txt']
    for dataSet in files:

        with open(f'Proposta/{dataSet}', 'r') as f:
            V = int(f.readline())
            l = [[int(num) for num in line.split(' ')] for line in f]
        #print(l)
        #print(V)
            f.close()
        '''
                for x, row in enumerate(l, start=0):
                    for y, elem in enumerate(row, start=0):
                        if(elem == 0 and x != y):
                            l[x][y]=INF
        '''
        g = Graph(V)
        g.graph = l
 

        output.write("Execucao;DataSet;Tempo;\n")
        for execution in range(0, 10):
            
            start = time.perf_counter()

            for dij in range(0, V):
                g.dijkstra(dij)

            end = time.perf_counter()
            tempo = end -start
            #print('tempo', end - start)
            output.write(f"{execution};{dataSet};{tempo};\n")

