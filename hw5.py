
import numpy as np

def isCircleInGraph(matrix):
        players=len(matrix)
        objects=len(matrix[0])
        numOfEdgesFromEachObject = np.zeros(objects)
        numOfEdgesFromEachPlayer=np.zeros(players)
        for i in range(players):
            for j in range(objects):
                if matrix[i][j]>0:
                    numOfEdgesFromEachObject[j]+=1 #add 1 if there is an edge to this object
                    numOfEdgesFromEachPlayer[i]+=1 #add 1 if there is an edge to this player
        numOfNodes=players+objects
        for i in range(objects): #deleting all the nodes of objects that has 1 / 0 edges
            if numOfEdgesFromEachObject[i]==0:
                numOfNodes-=1
            if numOfEdgesFromEachObject[i]==1:
                for j in range(players):
                    if matrix[j][i]>0 and numOfEdgesFromEachPlayer[j]==1:
                        numOfEdgesFromEachObject[i]-=1
                        numOfNodes-=1 #delte the node of the object
                        numOfEdgesFromEachPlayer[j]-=1 #deleting the edge from the player
                        break
                    elif matrix[j][i]>0 and numOfEdgesFromEachPlayer[j]>1:
                        numOfNodes -= 1 #delte only the node of the object because the node of the player still conected to other objects
                        numOfEdgesFromEachPlayer[j] -= 1
                        numOfEdgesFromEachObject[i] -= 1
                        break
        for p in range(players): #deleting all the nodes of the players that left with 0 edges (which means they are unconected)
            if numOfEdgesFromEachPlayer[p]==0:
                numOfNodes-=1
        #now we has a sub-graph that has only nodes of shared-objects, the edges that conected to them,
        #and the nodes of the players that conected to them.
        #if the number of edges in this sub-graph is bigger or equal to the number of nodes in this sub-graph
        #there must be a circle in the graph

        if numOfEdgesFromEachObject.sum()>=numOfNodes:
            return True
        else:
            return False





#tests
rightAnswers=0
g1=[[1,1,0.07,0],[0,0,0.93,1]] # there isnt a circle in the graph
if isCircleInGraph(g1)==False:
    rightAnswers+=1
g2 = [[1,0.4,0,0],[1,0.6,0,0],[0,0,0,0]] # there is a circle in the graph
if isCircleInGraph(g2)==True:
    rightAnswers+=1
g3 = [[1,0.2,0,0],[0,0.8,1,0],[0,0,0,0]] # there isnt a circle in the graph
if isCircleInGraph(g3)==False:
    rightAnswers+=1
g4 = [[1,0.5,0.5,0],[0,0.5,0.2,0],[0,0,0.3,0]] # there is a circle in the graph
if isCircleInGraph(g4)==True:
    rightAnswers+=1
print("right answers: " +str(rightAnswers))
print("wrong answers: "+str(4-rightAnswers))

