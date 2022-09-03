import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.shortest_paths import weighted
from networkx.algorithms.shortest_paths.dense import floyd_warshall
from numpy import *
from numpy import inf

G = nx.Graph()
G2 = nx.Graph()
entered = 0


def Prims():
    x=input("enter the input#")
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
            G.add_node(str(i), pos=(x[i], y[i]))
            G2.add_node(str(i), pos=(x[i], y[i]))
    plt.scatter(x, y)
    plt.show()
    adjmat = array([[inf] * nodes] * nodes)
    line = myfile.readline()
    for i in range(nodes):
            line = myfile.readline()
            words = line.split()
            numberofwords = len(words)
            fir = int(words[0])
            for j in range(1, numberofwords, 4):
                sec = int(words[j])

                if (adjmat[fir, sec] > float(words[j + 2]) / 1000000):
                    adjmat[fir, sec] = float(words[j + 2]) / 1000000
                    adjmat[sec, fir] = adjmat[fir, sec]
                    if (not (fir == sec)):
                        G.add_edge(str(fir), str(sec))

    for i in range(nodes):
        adjmat[i, i] = 0
        for i in range(nodes):
            for j in range(nodes):
                print(str.format('{0:5}', adjmat[i, j]), end="  ")
            print()
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True)
    plt.show()
    selected = [0] * nodes
    edges = 0
    line = myfile.readline()
    line = myfile.readline()
    selected[int(line)] = True
    print("Edges    : Weixghts")
    while (edges < nodes - 1):
            min = inf
            a = 0
            b = 0
            for i in range(nodes):
                if (selected[i]):
                    for j in range(nodes):
                        if ((not selected[j]) and adjmat[i, j]):
                            if (min > adjmat[i, j]):
                                a = i
                                b = j
                                min = adjmat[i, j]
            mst += adjmat[a, b]
            G2.add_edge(str(a), str(b))
            print(str(a) + "  -  " + str(b) + "  :  " + str(adjmat[a][b]))
            selected[b] = True
            edges += 1
    print(mst);
    nx.draw(G2, pos, with_labels=True)
    plt.show()