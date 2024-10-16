#Hamming(7,4) encoding & decoding 
import random
from prettytable import PrettyTable 

def xor(i,j):            
    if i==j:
        xor=0
    if i!=j:
        xor=1   
    return int(xor)   

def Incoding(message):
    print("Alphabet={0,1}  ,  Alphabet size=2  ,  Message length=",4," --->     Block length=",7)
    print("\nSender-Incoding:")
    a=message   #a0,a1,a2,a3
    p=[None]*3  #p0,p1,p2                 
    p[0]=xor(xor(a[0],a[1]),a[3])
    p[1]=xor(xor(a[0],a[2]),a[3])
    p[2]=xor(xor(a[1],a[2]),a[3])
    C=[p[0],p[1],a[0],p[2],a[1],a[2],a[3]]
    print("a =",a,"--xor-->  p =",p,"\nc = [p0,p1,a0,p2,a1,a2,a3] \nc =",C)
    print("Sending message...")
    return C

def Noise(C):
    d=[]
    d.extend(C)
    insexes=[] #indexes
    for i in range(len(C)):
        insexes.append(i)
    Noise_num=1 #Number of noeses   
    picking_random_noise_index=random.sample(insexes, Noise_num) #picking random noese index
    print("\n",Noise_num,"noise/noises falling:") 
    for i in (picking_random_noise_index):                
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
    
    l=[c2,c1,c0]
    print("(c2,c1,c0) =",l)

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
  
    Error = int("".join(str(x) for x in l), 2)
    if Error== 0:
        print ("No noise has occurred.")
    else:    
        print("Noise happened in = d" + str(Error-1))
        print("Correcting noise...")
        if d[Error-1]==0:
            d[Error-1]=1
        elif d[Error-1]==1:
            d[Error-1]=0 

    Decoded_Message=[d[2],d[4],d[5],d[6]]        
    print("The message was : ",Decoded_Message)
    return Decoded_Message

Message=[0,0,0,0]   
Incoded_Message=Incoding(Message)
Noisy_Incoded_Message=Noise(Incoded_Message)
Decoding(Noisy_Incoded_Message)
#end