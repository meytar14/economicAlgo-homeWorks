#hw4 Meytar Gil-Ron 322876046
def allVectors(objects): #returning all the possible combinations of partition objects
    vectors=[[0,0]]
    print(vectors)
    counter=0
    for object in objects:
        counter=counter+1
        newVectors =[]
        for v in vectors:
            for i in range(len(v)):
                newV=v.copy()
                newV[i]=newV[i]+object
                newVectors.append(newV)
        vectors=newVectors

        print("division of object number: "+str(counter)+" (num of states:"+str(len(vectors))+")   "+str(vectors))
    return vectors

def allVectorsWithPruning(objects):
    vectors=[[0,0]]
    print(vectors)
    counter=0
    for object in objects:
        counter=counter+1
        newVectors =[]
        for v in vectors:
            for i in range(len(v)):
                newV=v.copy()
                newV[i]=newV[i]+object
                isExist=False
                for h in newVectors:
                    if h==newV:
                        isExist=True
                        continue
                if not isExist or len(newVectors)==0:
                    newVectors.append(newV)
        vectors=newVectors

        print("division of object number: "+str(counter)+" (num of states:"+str(len(vectors))+")   "+str(vectors))
    return vectors

def findEgaliterian(vectors): #take all the vector and return the egaliterian vector
    mins=[]
    for v in vectors:
        mins.append(min(v))
    egaliterian=max(mins)
    egaliterianVector=[0,0,0]
    for v in vectors:
        if min(v) ==egaliterian and sum(v)>sum(egaliterianVector):
            egaliterianVector=v
    return egaliterianVector


def egaliterian(objects):
    vectors=allVectors(objects)
    v=findEgaliterian(vectors)
    return v

def egaliterianWithPruning(objects):
    vectors=allVectorsWithPruning(objects)
    v=findEgaliterian(vectors)
    return v

if __name__ == '__main__':

    objects=[1,2,3,3,2,8,5,3]
    print("objects"+str(objects))
    print("without pruning:")
    print("the egaliterian vector: "+str(egaliterian(objects)))
    print()
    print("with pruning:")
    print("the egaliterian vector: "+str(egaliterianWithPruning(objects)))
    print("\n\n\n")
    objects2 = [1, 12, 6, 15, 2, 8, 9, 3]
    print("objects"+str(objects2))
    print("without pruning:")
    print("the egaliterian vector: " + str(egaliterian(objects2)))
    print()
    print("with pruning:")
    print("the egaliterian vector: " + str(egaliterianWithPruning(objects2)))



