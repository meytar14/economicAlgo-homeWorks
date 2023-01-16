import numpy as np
import doctest


def find_trading_cycle(l:list):
    preferencs=[]
    for i in range(len(l)):
        preferencs.append(l[i][0])
    visited=[0]
    next=preferencs[0]
    #find the end of the cycle
    while not visited.__contains__(next):
        visited.append(next)
        next=preferencs[next]
    end_of_cycle=next
    #build the cycle
    cycle=[next]
    next=preferencs[next]
    while next!=end_of_cycle:
        cycle.append(next)
        next=preferencs[next]
    cycle.append(next)
    return cycle

def trading_cycle_algo(l:list):
    """
    >>> trading_cycle_algo([[0,1,3,2],[1,2,0,3],[2,3,1,0],[3,2,1,0]])
    [[0, 0], [1, 1], [3, 3], [2, 2]]
    >>> trading_cycle_algo([[4,2,1,3,5,0],[5,3,0,1,2,4],[1,2,0,3,4,5],[2,5,0,1,3,4],[2,3,0,1,4,5],[3,4,0,1,2,5]])
    [[2, 1], [1, 5], [5, 3], [3, 2], [0, 4], [4, 0]]
    >>> trading_cycle_algo([[2,0,1,3,4,5],[5,0,1,2,3,4],[1,0,2,3,4,5],[4,0,1,2,3,5],[2,0,1,3,4,5],[0,1,2,3,4,5]])
    [[0, 2], [2, 1], [1, 5], [5, 0], [3, 4], [4, 3]]
    >>> trading_cycle_algo([[2,3,1,4,0],[0,1,3,2,4],[1,0,2,3,4],[4,1,2,3,0],[4,2,1,3,0]])
    [[0, 2], [2, 1], [1, 0], [4, 4], [3, 3]]
    """
    num_of_players=len(l)
    orgenized_players=[]
    while len(orgenized_players)<num_of_players:
        cycle=find_trading_cycle(l)

        for i in range(len(cycle)-1):
            orgenized_players.append([cycle[i], cycle[i + 1]])
            # remove the orgenized homes from other player prefrences
            for p in l:
                p.remove(cycle[i])
    return orgenized_players




#example
preferences=[[4,2,1,3,5,0],[5,3,0,1,2,4],[1,2,0,3,4,5],[2,5,0,1,3,4],[2,3,0,1,4,5],[3,4,0,1,2,5]]
orgenized=trading_cycle_algo(preferences)
for p in orgenized:
    print("player "+str(p[0])+" get house number "+str(p[1]))
doctest.testmod()

