from numpy import *



arr=array([1,2,3,4,5])
print(arr)
arr=arr+5
print(arr) 

arr0=arr
print(arr)
print(arr0)
print(id(arr))
print(id(arr0))

arr0=arr.view()
print(arr)
print(arr0)
print(id(arr))
print(id(arr0))

arr[1]=0
print(arr)
print(arr0)
print(id(arr))
print(id(arr0))

arr0=arr.copy()
print(arr)
print(arr0)
print(id(arr))
print(id(arr0))
arr[1]=1
print(arr)
print(arr0)
print(id(arr))
print(id(arr0))





arr1=array([2,3,4,5])
arr2=array([1,4,5,6])
arr3=arr1+arr2
print(arr3)
print(concatenate([arr1,arr2]))


print(sin(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))




















































































































































































































































