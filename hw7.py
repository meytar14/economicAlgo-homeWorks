import doctest


def options(avaible,l,o:list):
    if len(avaible)==0:
        o.append(l)
        #print(l)
    else:
        for i in avaible:
            avaibleCopy=avaible.copy()
            lCopy=l.copy()
            avaibleCopy.remove(i)
            lCopy.append(i)
            options(avaibleCopy,lCopy,o)

arr=[1,2,3,4,5]
l=[]
opt=[]
options(arr,l,opt)
print(opt)
print(len(opt))
