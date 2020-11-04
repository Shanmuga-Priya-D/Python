

from array import *

a1=array('i',[])
n=int(input("enter length of array"))

for i in range(n):
    x=int(input("enter next value"))
    a1.append(x)    
print(a1)

print("search")
s=int(input("enter search element"))
k=0
for e in a1:
    if s==e:
        print(k)
        break
    k=k+1
print("or")
print(a1.index(s))    



print("delete")
d=int(input("enter element to delete"))
count=0

        
i=0
while i<=n:
   if i==d:
       j=0
       while j<=n-1:
           a1[j]=a1[j+1]
           j=j+1
       count=count+1
       break
   i=i+1
        


if count==0:
    print("element not found")
else:
    print("element deleted successfully")
    print("new array is")
    for k in a1:
        print(k)

            
       
    
