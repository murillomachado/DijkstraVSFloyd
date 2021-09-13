import time
 
V = 4

INF = 99999
 
def floydWarshall(graph):
   
    """ dist[][] will be the output
       matrix that will finally
        have the shortest distances
        between every pair of vertices """
    """ initializing the solution matrix
    same as input graph matrix
    OR we can say that the initial
    values of shortest distances
    are based on shortest paths considering no
    intermediate vertices """
 
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
 
    """ Add all vertices one by one
    to the set of intermediate
     vertices.
     ---> Before start of an iteration,
     we have shortest distances
     between all pairs of vertices
     such that the shortest
     distances consider only the
     vertices in the set
    {0, 1, 2, .. k-1} as intermediate vertices.
      ----> After the end of a
      iteration, vertex no. k is
     added to the set of intermediate
     vertices and the
    set becomes {0, 1, 2, .. k}
    """
    for k in range(V):
 
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    #printSolution(dist)
 
 
def printSolution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" % ("INF")),
            else:
                print( "%7d\t" % (dist[i][j])),
            if j == V-1:
                print("")
 
with open("Output/outFloyd.csv", "w", encoding='utf-8') as output:
    files = ['800.txt','1000.txt','1500.txt']
    ##files = ['10.txt', '25.txt', '50.txt','75.txt','100.txt','150.txt','200.txt','250.txt','300.txt','400.txt','500.txt','650.txt','800.txt','1000.txt','1500.txt']
    for dataSet in files:

        with open(f'Proposta/{dataSet}', 'r') as f:
            V = int(f.readline())
            l = [[int(num) for num in line.split(' ')] for line in f]
        #print(l)
        #print(V)
            f.close()

        for x, row in enumerate(l, start=0):
            for y, elem in enumerate(row, start=0):
                if(elem == 0 and x != y):
                    l[x][y]=INF
        
        tempo = 0
        output.write("DataSet;Tempo;\n")
        for execution in range(0, 3):
            start = time.perf_counter()
            floydWarshall(l)
            end = time.perf_counter()
            tempo =+ end - start
            #print('tempo', end - start)
        output.write(f"{dataSet};{tempo/3};\n")



            