import math
def euclidean_dist(x,y):
    temp=[]
    for a,b in zip(x,y):
        z=a-b
        temp.append(z**2)
    dist=math.sqrt(sum(temp))
    return dist
#dist=math.sqrt(sum([(a-b)**2 for a,b in zip(x,y)]))
