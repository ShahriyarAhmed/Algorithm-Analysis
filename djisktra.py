import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.shortest_paths import weighted
from networkx.algorithms.shortest_paths.dense import floyd_warshall
from numpy import *
from numpy import inf
G = nx.Graph()
G2 = nx.Graph()
def Djisktra():
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
 dist = [inf] * nodes
 parent = [-1] * nodes
 line = myfile.readline()
 line = myfile.readline()
 dist[int(line)] = 0
 queue = []
 for i in range (nodes):
          queue.append(i)
 while (queue):
          minimum = inf
          min_index = -1
          for i in range (nodes):
               if (dist[i] < minimum and i in queue):
                    minimum = dist[i]
                    min_index = i
          queue.remove(min_index)
          for i in range (nodes):
               if (adjmat[min_index][i] and i in queue):
                    if (dist[min_index] + adjmat[min_index,i] < dist[i]):
                         dist[i] = dist[min_index] + adjmat[min_index,i]
                         parent[i] = min_index
                         #G2.add_edge(str(min_index),str(i))
 print("Nodes       :    Weigths    :     Paths")
 for i in range(nodes):
          print(int(line), "  -  ",i,"  :  " ,dist[i], end = "         ")
          j = i
          queue1 = []
          while(parent[j] != -1):
               G2.add_edge(str(parent[j]),str(j))
               queue1.append(j)
               j = parent[j]
          queue1.reverse()
          for j in queue1:
               print(j, end = " ")
          print()
 nx.draw(G2,pos,with_labels = True)
 plt.show()