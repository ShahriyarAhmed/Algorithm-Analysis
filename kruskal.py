import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.shortest_paths import weighted
from networkx.algorithms.shortest_paths.dense import floyd_warshall
from numpy import *
from numpy import inf
G = nx.Graph()
G2 = nx.Graph()

def find(i,parent):
    while parent[i] != i:
        i = parent[i]
    return i
def union(i, j,parent): # for kruskal
    a = find(i,parent)
    b = find(j,parent)
    parent[a] = b
def krus(adjmat,nodes,parent):
    mst = 0
    for i in range(nodes):
        parent[i] = i
    edges = 0
    while edges < nodes - 1:
        min = inf
        a = -1
        b = -1
        for i in range(nodes):
            for j in range(nodes):
                if find(i,parent) != find(j,parent) and adjmat[i][j] < min:
                    min = adjmat[i][j]
                    a = i
                    b = j
        union(a, b,parent)
        print('Edge {}:({}, {}) cost:{}'.format(edges, a, b, min))
        edges += 1
        mst += min
        G2.add_edge(str(a),str(b))
    print("Minimum cost= {}".format(mst))
    return mst
def Kruskals():
 x = input("enter the input#")
 filename = "input" + str(x) + ".txt"
 myfile = open(filename)
 mst = 0
 line = myfile.readline()
 line = myfile.readline()
 line = myfile.readline()
 nodes = int(line)
 line = myfile.readline()
 x = []
 y = []
 for i in range(nodes):
     line = myfile.readline()
     words = line.split()
     x.append(float(words[1]))
     y.append(float(words[2]))
     G.add_node(str(i), pos = (x[i],y[i]))
     G2.add_node(str(i), pos = (x[i],y[i]))
 plt.scatter(x,y)
 plt.show()
 adjmat = array([[inf]* nodes]*nodes)
 line = myfile.readline()
 for i in range(nodes):
     line = myfile.readline()
     words = line.split()
     numberofwords = len(words)
     fir = int(words[0])
     for j in range(1,numberofwords,4):
         sec = int(words[j])
         
         if(adjmat[fir,sec] > float(words[j+2])/1000000):
          adjmat[fir,sec] = float(words[j+2])/1000000
          adjmat[sec,fir] = adjmat[fir,sec]
          if( not (fir == sec)):
              G.add_edge(str(fir),str(sec))
          
 for i in range(nodes):
     adjmat[i,i] = 0
 for i in range(nodes):
     for j in range(nodes):
         print(str.format('{0:5}', adjmat[i,j]),end="  ")
     print()
 pos=nx.get_node_attributes(G,'pos')
 nx.draw(G,pos,with_labels = True)
 plt.show()
 parent = [i for i in range(nodes)]
 mst = krus(adjmat,nodes,parent)
 nx.draw(G2,pos,with_labels = True)
 plt.show()