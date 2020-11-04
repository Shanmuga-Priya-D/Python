# to copy elements from existing array to new array

from array import *

a1=array('i',[5,9,8,4,2])

newarr1=array(a1.typecode,(a for a in a1))

for e in newarr1:
    print(e)
    
    
print("-------------------------")    


from array import *

a2=array('i',[5,9,8,4,2])

newarr2=array(a1.typecode,(a*a for a in a2))

for e in newarr2:
    print(e)