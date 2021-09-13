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
 
    def minDistance(self, dist, sptSet):
 
        min = sys.maxsize
 
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index

    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            u = self.minDistance(dist, sptSet)

            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
 
        #self.printSolution(dist)
 

with open("Output/outDijkstra.csv", "w", encoding='utf-8') as output:
    files = ['800.txt','1000.txt','1500.txt']
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
        tempo = 0
        output.write("DataSet;TempoMedio;\n")
        for execution in range(0, 3):
            start = time.perf_counter()
            for dij in range(0, V):
                g.dijkstra(dij)
            end = time.perf_counter()
            tempo =+ end -start
            #print('tempo', end - start)
        output.write(f"{dataSet};{tempo/3};\n")

