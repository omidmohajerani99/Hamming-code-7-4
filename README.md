## Hamming code(7,4): Encoding & decoding (correcting one noise) in python
### 0.What is hamming code(7,4)?
 Hamming(7,4) is a linear error-correcting code that encodes four bits of data into seven bits by adding three parity bits and after decoding can find two errors and fix one error. It is a member of a larger family of Hamming codes.
 ### 1.How the sender encodes four bits message in hamming code?
   What is XOR gate?
 
|input A|input B|XOR output|
| ---   |:--:   | -:|
| 0     | 0     | 0 |
| 1     | 0     | 1 |
| 0     | 1     | 1 |
| 1     | 1     | 0 |

 xor &rarr; + 
 + How to make three parity bits?\
(xor &rarr; +)\
$p_{0} = a_{0} + a_{1} + a_{3}$\
$p_{1} = a_{0} + a_{2} + a_{3}$\
$p_{2} = a_{1} + a_{2} + a_{3}$\


$d = [d_{0} , d_{1} , d_{2} , d_{3} , d_{4} , d_{5} , d_{6}]$ \
$d = [p_{0} , p_{1} , a_{0} , p_{2} , a_{1} , a_{2} , a_{3}]$



 ### 2.What is noise in channel? how it happend?

 ### 3.How messege reciver decodes & fixes one error in hamming code?
(xor &rarr; +)\
 $c_{2}=d_{3}+d_{4}+d_{5}+d_{6}$\
 $c_{1}=d_{1}+d_{2}+d_{5}+d_{6}$\
 $c_{0}=d0+d2+d4+d6$
|| $c_{2} c_{1} c_{0}$ |  Error index  |
| ---|:--:| -:|
|0|    000     | No Error |
|1|    001     |    $d_{0}$    |
|2|    010     |    $d_{1}$    |
|3|    011     |    $d_{2}$    |
|4|    100     |    $d_{3}$    |
|5|    101     |    $d_{4}$    |
|6|    110     |    $d_{5}$    |
|7|    111     |    $d_{6}$    |

 ### 4.History

$\frac{n!}{k!(n-k)!}$\
$\color{red}x$\
 a -xor&rarr;p\
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media