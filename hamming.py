#hamming encoding & decoding(7,4)
import random
from prettytable import PrettyTable 

def xor(i,j):            
    if i==j:
        xor=0
    if i!=j:
        xor=1   
    return int(xor)   

def Incoding(message):
    print("Alphabet={0,1}    Alphabet size=2    Message length=",4,"      Block length=",7)
    print("\nSender-Incoding:")
    a=message   #a0,a1,a2,a3
    p=[None]*3  #p0,p1,p2                 
    p[0]=xor(xor(a[0],a[1]),a[3])
    p[1]=xor(xor(a[0],a[2]),a[3])
    p[2]=xor(xor(a[1],a[2]),a[3])
    c=[p[0],p[1],a[0],p[2],a[1],a[2],a[3]]
    print("a =",a,"--xor-->  p =",p,"\nc = [p0,p1,a0,p2,a1,a2,a3] \nc =",c)
    print("Sending message...")
    return c

def Noise(c):
    print("\nNoise falling:") 
    d=[]
    d.extend(c)
    list0=[] 
    for i in range(len(c)):
        list0.append(i)
    picking_random_index=random.sample(list0, 1) #picking 1 random index
    #print(picking_random_index)
    for i in (picking_random_index):                
        if d[i]==0:
            d[i]=1
        elif d[i]==1:
            d[i]=0  
        print("c[",i,"] changed! \nd = ",d)                           
    return d

def Decoding(d):
    print("\nReceiver-Decoding:  \nd =",d,"\nd = [d0,d1,d2,d3,d4,d5,d6] \nd = [p0,p1,a0,p2,a1,a2,a3]")
    
    c2=xor(xor(xor(d[3],d[4]),d[5]),d[6]);
    print("c2 = (d3+d4+d5+d6) = ",c2)
    c1=xor(xor(xor(d[1],d[2]),d[5]),d[6]);
    print("c1 = (d1+d2+d5+d6) = ",c1);
    c0=xor(xor(xor(d[0],d[2]),d[4]),d[6]);
    print("c0 = (d0+d2+d4+d6) = ",c0)
    
    print("(c2,c1,c0) =",c2,c1,c0)

    E_LIST = [c2,c1,c0]
    Error = int("".join(str(x) for x in E_LIST), 2)
    print("The converted integer value is : d" + str(Error-1))

    myTable = PrettyTable(["(c2 c1 c0)", "Error"]) 
    myTable.add_row(["000", "No Error"]) 
    myTable.add_row(["001", "d0"]) 
    myTable.add_row(["010", "d1"]) 
    myTable.add_row(["011", "d2"]) 
    myTable.add_row(["100", "d3"]) 
    myTable.add_row(["101", "d4"]) 
    myTable.add_row(["110", "d5"])
    myTable.add_row(["111", "d6"])  
    print(myTable)

#dic={"000":"No Error","001":"d0","010":"d1","011":"d2","100":"d3","101":"d4","110":"d5","111":"d6"}
#print(str(c2),str(c1),str(c0))

message=[0,1,1,0] 
c=Incoding(message)
d=Noise(c)
Decoding(d)