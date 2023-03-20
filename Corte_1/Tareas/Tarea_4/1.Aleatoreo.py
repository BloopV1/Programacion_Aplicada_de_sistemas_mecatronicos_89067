from random import randint

def aleatoreo(num:int=10):
    num=[]
    while len (n)<num:
        rand=randint(100,120)
    if (rand!=110) and (rand!=115) and (rand!=119):
        if (len (n)%2)==0  and (rand%2==0):
            n.append(rand)
        elif (len(n)%2)==1 and (rand%2==1):
            n.append(rand)
    return n
n=aleatoreo()
print (n)