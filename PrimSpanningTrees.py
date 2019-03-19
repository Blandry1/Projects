# A Python program for Prim's Minimum Spanning Tree (MST) algorithm. 
# The program is for adjacency matrix representation of the graph 
"""
vertex of interest stored in parent array
input parameters: Rg, R[i][j], C[i][j], Cg (fixed cost)
"""
  
import sys
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 
  
    # A utility function to test & print the constructed MST stored in parent[] 
    def testMST(self, parent, Rg, Cg): 
        print ("\nEdge \tWeight")
        R_sys = 1
        C_sys = 0    
        C_left = Cg
        testsPassed = [False] * 3

        for i in range(1,self.V): 
            print (parent[i],"-",i,"\t",abs(self.graph[i][ parent[i] ] )) # used abs to turn printed weight positive
            
            R_sys *= abs(R[i][parent[i]])
            C_sys += C[i][parent[i]]
            C_left -= C[i][parent[i]]

        print( "R_sys:", R_sys)
        print( "C_sys:", C_sys)
        print( "Cost_left:", C_left)
        if (R_sys > Rg):
            print("test1 passed")
            testsPassed[0] = True
        else:
            print("test1 failed")
        if(R_sys > Rg and C_sys <= Cg):
            print("test2 passed")
            testsPassed[1] = True
        else:
            print("test2 failed")
        if(C_sys <= Cg):
            print("test3 passed")
            testsPassed[2] = True
        else:
            print("test3 failed")
        #print(testsPassed)

    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minKey(self, key, mstSet): 
  
        # Initilaize min value 
        min = sys.maxsize
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
  
    # Function to construct and print MST for a graph  
    # represented using adjacency matrix representation 
    def primMST(self): 
  
        #Key values used to pick minimum weight edge in cut 
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V # Array to store constructed MST 
        # Make key 0 so that this vertex is picked as first vertex 
        key[0] = 0 
        mstSet = [False] * self.V
  
        parent[0] = -1 # First node is always the root of 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minKey(key, mstSet) 
  
            # Put the minimum distance vertex in  
            # the shortest path tree 
            mstSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                # graph[u][v] is non zero only for adjacent vertices of m 
                # mstSet[v] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] # to be used for extension
                if self.graph[u][v] != 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u
        return parent

        #self.testMST(parent, 0.7, 100) # calculate reliability here
  


# Driver Code / Unit Test
R = [[0, 0.94, 0.91, 0.96, 0.93, 0.92],
    [0.94, 0, 0.94, 0.97, 0.91, 0.92],
    [0.91, 0.94, 0, 0.94, 0.90, 0.94],
    [0.96, 0.97, 0.94, 0, 0.93, 0.96],
    [0.93, 0.91, 0.90, 0.93, 0, 0.91],
    [0.92, 0.92, 0.94, 0.96, 0.91, 0]]
RNeg = [[val*-1 for val in row] for row in R]
C = [[0,  10, 25, 10, 20, 30],
    [10, 0,  10, 10, 25, 20],
    [25, 10, 0,  20, 40, 10],
    [10, 10, 20, 0,  20, 10],
    [20, 25, 40, 20, 0,  30],
    [30, 20, 10, 10, 30, 0]]
n = 6
Rg = 0.7
Cg = 100


g = Graph(n) # max reliability graph
h = Graph(n) # min cost graph
g.graph = RNeg # find max reliablity 
max_R = g.primMST()

h.graph = C # find min cost
min_C = h.primMST()

g.testMST(max_R, Rg, Cg)
h.testMST(min_C, Rg, Cg)
# write logic to pick the object (either g or h) that has all 3 tests passing
    # for now, use min_C
# extend graph, to have max reliability, with the leftover cost (C_left)


