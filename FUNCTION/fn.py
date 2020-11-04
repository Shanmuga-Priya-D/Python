

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even=even+1
        else: 
            odd=odd+1
            
    
    return odd,even
    
    
lst=[]    
n=int(input("enter n"))
for i in range(0,n):
    ele=int(input("enter next value"))
    lst.append(ele)
print(lst)
even,odd=count(lst)
print("even:{} and odd:{}".format(even,odd))