#Hamming code(7,4): Encoding & decoding (correcting one noise) in python
import random 
from prettytable import PrettyTable 

def xor(i,j):            
    if i==j:
        xor=0
    if i!=j:
        xor=1   
    return int(xor)   

def Encoding(message):
    print("Alphabet={0,1}  ,  Alphabet size=2  ,  Message length=",4," --->     Block length=",7)
    print("\nSender-Encoding:")
    a=message   #a0,a1,a2,a3
    print("A = ",a)    
    p=[None]*3  #p0,p1,p2                   
    p[0]=xor(xor(a[0],a[1]),a[3])
    print("p0 = (a0+a1+a3) = ",p[0])      
    p[1]=xor(xor(a[0],a[2]),a[3])
    print("p1 = (a0+a2+a3) = ",p[1])         
    p[2]=xor(xor(a[1],a[2]),a[3])
    print("p2 = (a1+a2+a3) = ",p[2]) 
        
    C=[p[0],p[1],a[0],p[2],a[1],a[2],a[3]]
    print("c = [p0,p1,a0,p2,a1,a2,a3] \nc =",C)
    print("Sending message C ...")
    return C

def Noise(C):
    D=[]
    D.extend(C)
    insexes=[] #indexes
    for i in range(len(C)):
        insexes.append(i)
    Noise_num=1 #Number of noeses   
    picking_random_noise_index=random.sample(insexes, Noise_num) #picking random noese index
    print("\n",Noise_num,"noise/noises falling:") 
    for i in (picking_random_noise_index):                
        if D[i]==0:
            D[i]=1
        elif D[i]==1:
            D[i]=0  
        print("c[",i,"] changed! \nd = ",D)                           
    return D

def Decoding(d):
    print("\nReceiver-Decoding:  \nMessage d recevide! \nd =",d,"\nd = [d0,d1,d2,d3,d4,d5,d6] \n")
    
    k2=xor(xor(xor(d[3],d[4]),d[5]),d[6]);
    print("k2 = (d3+d4+d5+d6) = ",k2)
    k1=xor(xor(xor(d[1],d[2]),d[5]),d[6]);
    print("k1 = (d1+d2+d5+d6) = ",k1);
    k0=xor(xor(xor(d[0],d[2]),d[4]),d[6]);
    print("k0 = (d0+d2+d4+d6) = ",k0,"\n")
    
    l=[k2,k1,k0]
    print("(k2,k1,k0) = ",l,"\n")

    myTable = PrettyTable(["k2 k1 k0", "Error"]) 
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
        print("Noise happened on d" + str(Error-1))
        print("Correcting noise...")
        if d[Error-1]==0:
            d[Error-1]=1
        elif d[Error-1]==1:
            d[Error-1]=0 

    Decoded_Message=[d[2],d[4],d[5],d[6]]        
    print("The message was: A* = ",Decoded_Message)
    return Decoded_Message

Message=[1,1,1,0]   
Encoded_Message=Encoding(Message)
Noisy_Encoded_Message=Noise(Encoded_Message)
Decoding(Noisy_Encoded_Message)
#end

