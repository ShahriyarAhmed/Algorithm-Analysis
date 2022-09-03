import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.shortest_paths import weighted
from networkx.algorithms.shortest_paths.dense import floyd_warshall
from numpy import *
from numpy import inf
G = nx.Graph()
G2 = nx.Graph()
def combine(e,setMatrix):
	e0 = -1
	e1 = -1
	for i in range(0,len(setMatrix)):
		if e[0] in setMatrix[i]:
			e0 = i
		if e[1] in setMatrix[i]:
			e1 = i
	setMatrix[e0] += setMatrix[e1]
	del setMatrix[e1]
def Boruvka():
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
 setMatrix = []
 for i in range(0,len(adjmat)):
          setMatrix.append([i])
 print("Initial Grouping: " + str(setMatrix))
 while (len(setMatrix) > 1):
          edges = []
          for component in setMatrix:
               m = [999,[0,0]]
               for vertex in component:
                    for i in range(0,len(adjmat[0])):
                         if i not in component and adjmat[vertex][i] != 0:
                              if (m[0] > adjmat[vertex][i]):
                                   m[0] = adjmat[vertex][i]
                                   m[1] = [vertex,i]
               if (m[1][0] > m[1][1]):
                    m[1][0], m[1][1] =  m[1][1],m[1][0]
               if (m[1] not in edges):
                    edges.append(m[1])
          for e in edges:
               combine(e,setMatrix)
          print("Edges formed: " + str(edges) + " Groupings: " + str(setMatrix))
          for e in edges:
               a = str(e[0])
               b = str(e[1])
               mst+= adjmat[int(a)][int(b)]
               G2.add_edge(a,b)
 print("MST = ",mst)
 nx.draw(G2,pos,with_labels = True)
 plt.show()