import time
def tml():
    t=list(time.localtime())
    t=[12,1,22]
    tm=''
    if t[0]<12:
        ap=' am'
    else:
        ap=' pm'
        if t[0]!=12:
            t[0]=t[0]-12
    for i in t:    
        if len(str(i))==1:
            t[t.index(i)]='0'+str(i)
    tm=str(t[0])+':'+str(t[1])+':'+str(t[2])+ap
    return tm

