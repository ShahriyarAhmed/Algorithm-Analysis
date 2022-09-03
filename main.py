import kruskal
import prims
import djisktra
import bellman_ford
import floyd
import cluster
import boruvka
y=0
while(y==0):
    x=input("1---Prims\n2---kruskal\n3---djisktra\n4---cluster\n5---boruvka\n6---Bellmanford\n7---floyd\nEnter Algo#=")
    if x =='1':
        prims.Prims()
    elif x =='2':
        kruskal.Kruskals()
    elif x =='3':
        djisktra.Djisktra()
    elif x =='4':
         cluster.Cluster()
    elif x =='5':
        boruvka.Boruvka()
    elif x =='6':
        bellman_ford.Bellman_Ford()
    elif x =='7':
         floyd.Floyd()
    else:
        print("wrong choice")
        y=10