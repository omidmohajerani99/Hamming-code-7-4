## Hamming code(7,4): Encoding & decoding (correcting  any single-bit error) in python

### Objectives:
This document provides a comprehensive overview of the Hamming(7,4) code, including its history, encoding and decoding processes, and a simulation of a Binary Symmetric Channel (BSC) that introduces noise into transmitted codewords. Additionally, Python code examples are included to illustrate these concepts, followed by a practical example for enhanced understanding.
<!--Here we will give explanations about the history and coding and decoding(correction of an error) of Hamming(7,4) and we will also simulate a Binary symmetric channel(BSC) that is capable of creating a noise in the transmitted codewords. We have also provided Python code at the end of each section. Finally, we have discussed an example for better understanding.
-->
---

### Hamming code history
From [https://www.techtarget.com/whatis/definition/Hamming-code ] :

"Before Hamming code, there were several error correction methods in use that were not as efficient or effective. The simplest method involves adding a single parity bit. This can detect a single error but not detect two-bit errors nor correct the error. Another method was repeating each bit three times. This could detect and correct a single bit error but not errors in two bits. Repeating the bits was also very inefficient.\
Richard Hamming worked for Bell Labs in the 1940s and 1950s. During that time, computers used relays and read information from punched paper tape. These systems were often prone to errors relating to the paper tape being misread or relays getting stuck. If an operator was on hand when the error occurred, the program could be restarted; if the error occurred outside of working hours, the computer would skip the entire program, losing time and work.\
Hamming reasoned that, if a computer can detect an error, it could also correct the error. So, he began working on an error correcting algorithm, and in 1950, he published the Hamming code."

---

### What is hamming code(7,4)?
 In coding theory, Hamming(7,4) is a linear error-correcting code and it is a member of a larger family of Hamming codes that encodes four bits of data into seven bits by adding three parity bits and after decoding can correct any single-bit error ($t=1$), or detect all single-bit and two-bit errors ($\rho=2$). The minimum Hamming distance between any two correct codewords is three ($d_{min}=3$). This means that for transmission medium situations where burst errors do not occur, Hamming's(7,4) code is effective.
 * $d_{min}\ge2t+1$ 
 * $d_{min}\ge \rho+1$

---

 <!--### How does sender encode four bits data in hamming(7,4)?-->
 ### Encoding Process
 <!--0. Suppose we want to transmit this 4 bits data $A = (a_{0},a_{1},a_{2},a_{3})$ over a binary symmetric channel(BSC) and we need to find 3 parity bits $P = (p_{0},p_{1},p_{2})$.-->
0. Data Bits: The original message consists of 4 bits.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  $A = (a_{0},a_{1},a_{2},a_{3})$<br>
 
1. Parity Bits: Three additional bits are calculated based on specific parity checks.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
$p = ( p_{0} , p_{1} , p_{2} )$ <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
$p_{0} = a_{0} \oplus a_{1} \oplus a_{3}$<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
$p_{1} = a_{0} \oplus a_{2} \oplus a_{3}$<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
$p_{2} = a_{1} \oplus a_{2} \oplus a_{3}$
<br>

<!-- * Now we have to know xor gate (the xor symbol is $\oplus$): -->
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The $\oplus$ is XOR gate symbol:
 <br> 

|input A|input B|XOR  output|
| ---   |:--:   | -:|
| 0     | 0     | 0 |
| 1     | 0     | 1 |
| 0     | 1     | 1 |
| 1     | 1     | 0 |
 <br> 

```RUBY
#Python
def xor(i,j):            
    if i==j:
        xor=0
    if i!=j:
        xor=1   
    return int(xor) 
```
2. Codeword Formation: The resulting 7-bit codeword is formed by combining the 4 data bits and 3 parity bits.
<!-- 1. Second we will sit four bits of data into seven bits block(with $C$ as a Hamming codeword symbol) :<br> -->
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
$C = (p_{0} , p_{1} , a_{0} , p_{2} , a_{1} , a_{2} , a_{3})$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
$C = (c_{0} , c_{1} , c_{2} , c_{3} , c_{4} , c_{5} , c_{6})$
<br>

3. Send the C codeword over the channel.

```RUBY
#Python
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
```
---
 <!-- ### How simulate a Binary symmetric channel(BSC) that is capable of creating a noise in the transmitted codewords?-->
 ### Binary Symmetric Channel (BSC)
 * First of all, pay attention to the  basic mathematical model for a communication system:
<br><br>
  <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/3e5366c809cb41ab57f4364b475895f13a9dd328" class="mwe-math-fallback-image-inline mw-invert skin-invert" title="Channel model" aria-hidden="true" style="vertical-align: -3.146ex; margin-bottom: -0.525ex; width:61.869ex; height:7.843ex;" alt="{\displaystyle {\xrightarrow[{\text{Message}}]{W}}{\begin{array}{|c| }\hline {\text{Encoder}}\\f_{n}\\\hline \end{array}}{\xrightarrow[{\mathrm {Encoded \atop sequence} }]{A}}{\begin{array}{|c| }\hline {\text{Channel}}\\p(y|x)\\\hline \end{array}}{\xrightarrow[{\mathrm {Received \atop sequence} }]{Y^{n}}}{\begin{array}{|c| }\hline {\text{Decoder}}\\g_{n}\\\hline \end{array}}{\xrightarrow[{\mathrm {Estimated \atop message} }]{\hat {W}}}}"> 
 <br><br>
Image from [https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem] 

* Similarly we have:<br>
A &rarr; Encoding &rarr; C &rarr; Falling noise &rarr;  D &rarr; Decoding &rarr; A* 
* In simple terms, it can be said that four events can happen in a symmetric binary channel (BSC):\
Sending 0 and receiving 0.\
Sending 0 and receiving 1 (error).\
Sending 1 and receiving 1.\
Sending 1 and receiving 0 (error).

* During the time of sending the C codeword in the channel, a noise may be created on C codeword and the C codeword becomes to new D codeword. We simulate a BSC in python that has the ability to create a random noise on one of the seven bits of the C codeword.<br>
$D = (d_{0} , d_{1} , d_{2} , d_{3} , d_{4} , d_{5} , d_{6})$\
$D = (p_{0} , p_{1} , a_{0} , p_{2} , a_{1} , a_{2} , a_{3})$

```RUBY
#Python
import random 
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
```
---

  <!--### How does reciver decode and correct an error in hamming(7,4)?-->
  ### Decoding Process
0. The reciver recived 7bits D codeword:\
$D = (d_{0} , d_{1} , d_{2} , d_{3} , d_{4} , d_{5} , d_{6})$\
$D = (p_{0} , p_{1} , a_{0} , p_{2} , a_{1} , a_{2} , a_{3})$

 1. For decoding we need to find $k_{2} k_{1} k_{0}$ :\
 $k_{2}=d_{3}\oplus d_{4}\oplus d_{5} \oplus d_{6}$\
 $k_{1}=d_{1}\oplus d_{2}\oplus d_{5}\oplus d_{6}$\
 $k_{0}=d_{0} \oplus d_{2} \oplus d_{4} \oplus d_{6}$
 

 ```RUBY
 #Python
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
 ```

 2.  Find that one error with The table below:
   
|  $k_{2} k_{1} k_{0}$ |  Error |
|  :--:| -:|
|    000     | No Error |
|    001     |    $d_{0}$    |
|    010     |    $d_{1}$    |
|    011     |    $d_{2}$    |
|    100     |    $d_{3}$    |
|    101     |    $d_{4}$    |
|    110     |    $d_{5}$    |
|    111     |    $d_{6}$    |

```RUBY
from prettytable import PrettyTable 

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
```
3. Correct the error in D:\
If error was 0 change it to 1. \
If error was 1 change it to 0.

4. The $(a_{0},a_{1},a_{2},a_{3})$ in $D = (p_{0} , p_{1} , a_{0} , p_{2} , a_{1} , a_{2} , a_{3})$ is the message.\
 (The $(d_{2},d_{4},d_{5},d_{5})$ in $D = (d_{0} , d_{1} , d_{2} , d_{3} , d_{4} , d_{5} , d_{6})$ is the message.)  

```RUBY
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
```
---
### For example:
Encoding:\
$A = (1, 1, 1, 0)$\
$P_{0} =0$\
$P_{1} =0$\
$P_{2} =0$\
$P = (0,0,0)$\
$C = (0, 0, 1, 0, 1, 1, 0)$

Noise:\
$c_{6}$ changed!\
$D =(0, 0, 1, 0, 1, 1, 1)$

Decoding:\
$K =(1,1,1)$  &nbsp;&nbsp;&nbsp;&nbsp;  in table:&nbsp;&nbsp;&nbsp;&nbsp;  111 &rarr; d6\
Noise happened on d6\
$A* =(1, 1, 1, 0)$

```ruby
Message = [1,1,1,0]   
Encoded_Message = Encoding(Message)
Noisy_Encoded_Message = Noise(Encoded_Message)
Decoding(Noisy_Encoded_Message)
#end
```

```RUBY
Terminal:

Alphabet={0,1}  ,  Alphabet size=2  ,  Message length= 4  --->     Block length= 7

Sender-Encoding:
A =  [1, 1, 1, 0]
p0 = (a0+a1+a3) =  0
p1 = (a0+a2+a3) =  0
p2 = (a1+a2+a3) =  0
c = [p0,p1,a0,p2,a1,a2,a3]
c = [0, 0, 1, 0, 1, 1, 0]
Sending message C ...

 1 noise/noises falling:
c[ 6 ] changed!
d =  [0, 0, 1, 0, 1, 1, 1]

Receiver-Decoding:
Message d recevide!
d = [0, 0, 1, 0, 1, 1, 1]
d = [d0,d1,d2,d3,d4,d5,d6]

k2 = (d3+d4+d5+d6) =  1
k1 = (d1+d2+d5+d6) =  1
k0 = (d0+d2+d4+d6) =  1

(k2,k1,k0) =  [1, 1, 1]

+----------+----------+
| k2 k1 k0 |  Error   |
+----------+----------+
|   000    | No Error |
|   001    |    d0    |
|   010    |    d1    |
|   011    |    d2    |
|   100    |    d3    |
|   101    |    d4    |
|   110    |    d5    |
|   111    |    d6    |
+----------+----------+
Noise happened on d6
Correcting noise...
The message was: A* =  [1, 1, 1, 0]
```
