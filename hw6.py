import networkx as nx
import doctest

def find_circle_in_consumption_graph(allocation: list[list[float]]):
    """
     >>> find_circle_in_consumption_graph([[0.5,0.2,1,0,0],[0.5,0.8,0,0,0]])
     [(0, 2), (2, 1), (1, 3), (3, 0)]
     >>> find_circle_in_consumption_graph([[1,1,1],[0,0,0]])
     []
     >>> find_circle_in_consumption_graph([[0.4,0,0],[0,4,1,0],[0.2,0,0]])
     []
     >>> find_circle_in_consumption_graph([[0.7,0,0],[0.2,0.2,0],[0,0.8,0.1],[0.1,0,0.9]])
     [(4, 1), (1, 5), (5, 2), (2, 6), (6, 3), (3, 4)]
     >>> find_circle_in_consumption_graph([[0.5,0,0],[0.1,0.5,0],[0,0.5,1],[0.4,0,0]])
     []
     >>> find_circle_in_consumption_graph([[0.3,0.3,0.3],[0,0.7,0],[0.7,0,0.7]])
     [(0, 3), (3, 2), (2, 5), (5, 0)]
     >>> find_circle_in_consumption_graph([[0,0.5,0.5],[0,0.5,0],[1,0,0.5]])
     []
     >>> find_circle_in_consumption_graph([[0,0,0,0],[1,1,0,0],[0,1,0,1],[1,0,0,1]])
     [(1, 4), (4, 3), (3, 7), (7, 2), (2, 5), (5, 1)]
    """
    #building the consumption graph
    g= nx.Graph()
    for i in range(len(allocation)):
        for j in range(len(allocation[0])):
            if allocation[i][j]>0:
                g.add_edge(i,len(allocation)+j)
    #try to find a cycle in the graph
    try:
        cycle=nx.find_cycle(g)
    except:
        cycle=[]
    return cycle

# run tests
#doctest.testmod()
def options( avaiable):
    if len(avaiable)==0:
        print(avaiable)
    for i in avaiable:
        options(avaiable.remove(i))



def g(avaible,l,options:list):
    if len(avaible)==0:
        options.append(l)
        #print(l)
    else:
        for i in avaible:
            avaibleCopy=avaible.copy()
            lCopy=l.copy()
            avaibleCopy.remove(i)
            lCopy.append(i)
            g(avaibleCopy,lCopy,options)

arr=[1,2,3,4,5]
l=[]
opt=[]
g(arr,l,opt)
print(opt)
print(len(opt))
