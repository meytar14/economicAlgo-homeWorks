import numpy as np
import doctest

def find_max(a):
    max=0
    idx=0
    for i in range(len(a)):
        if a[i]>max:
            max=a[i]
            idx=i
    return idx

def utulitary_with_condition(total:float,subjects:list,preferences:list):
    """
    >>> utulitary_with_condition(500,["a","b","c","d"],[["a","b"],["a","c"],["a","d"],["b","c"],["a"]])
    citezen 0 gives 100.0 to a
    citezen 1 gives 100.0 to a
    citezen 2 gives 100.0 to a
    citezen 3 gives 50.0 to b50.0 to c
    citezen 4 gives 100.0 to a
    d= [a=400.0 b=50.0 c=50.0 d=0.0 ]

    >>> utulitary_with_condition(160,["a","b","c","d"],[["a"],["c"],["b"],["d"]])
    citezen 0 gives 40.0 to a
    citezen 1 gives 40.0 to c
    citezen 2 gives 40.0 to b
    citezen 3 gives 40.0 to d
    d= [a=40.0 b=40.0 c=40.0 d=40.0 ]
    >>> utulitary_with_condition(160,["a"],[["a"],["a"],["a"]])
    citezen 0 gives 53.333333333333336 to a
    citezen 1 gives 53.333333333333336 to a
    citezen 2 gives 53.333333333333336 to a
    d= [a=160.0 ]
    """
    money_for_each_player=total/len(preferences)
    d=np.zeros(len(subjects))
    num_of_votes_for_each_subject=np.zeros(len(subjects))
    for p in preferences:
        for subject in p:
            num_of_votes_for_each_subject[subjects.index(subject)]=num_of_votes_for_each_subject[subjects.index(subject)]+1
    c=0
    for p in preferences:
        preferences_of_p=np.zeros(len(subjects))
        for subject in p:
            preferences_of_p[subjects.index(subject)]=num_of_votes_for_each_subject[subjects.index(subject)]
        c1=0
        maximum=max(preferences_of_p)
        for p in preferences_of_p:
            if p==maximum:
                c1=c1+1
        str_p="citezen " + str(c) + " gives "
        for i in range(len(preferences_of_p)):
            if preferences_of_p[i]==maximum:
                d[i] = d[i] + money_for_each_player/c1
                str_p=str_p+str(money_for_each_player/c1)+" to " + subjects[i]
                #print("citezen " + str(c) + " gives " + str(money_for_each_player) + " to " + subjects[idx])
        # idx=find_max(preferences_of_p)
        # d[idx]=d[idx]+money_for_each_player
        print(str_p)
        c=c+1
        str_d="d= ["
        for i in range(len(subjects)):
            str_d=str_d+subjects[i]+"="+str(d[i])+" "
        str_d=str_d+"]"
    print(str_d)


doctest.testmod()
print("example:")
utulitary_with_condition(200,["build a bridge","build a basketball court","open a gallery"],[["build a bridge"],["build a basketball court"],["build a bridge","build a basketball court"],["open a gallery"],["open a gallery","build a basketball court"]])
