from numpy import *

arr=array([
[1,2,3],
[4,5,6]
])

print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)

arr1=arr.flatten()
print(arr1)

arr2=array([
[1,2,3,4,5,6],
[11,22,33,44,55,66]
])

arr3=arr2.flatten()
print(arr3)
arr4=arr3.reshape(3,4)
print(arr4)
arr5=arr3.reshape(2,2,3)
print(arr5)

m=matrix(arr2)
print(m)

m1=matrix('1,2,3,4;5,6,7,8')
print(m1)

m2=matrix('1,2;3,4;5,6;7,8')
print(m2)

m3=matrix('1,2,3;4,5,6;7,8,9')
print(m3)

print(diagonal(m3))

print(m3.max())

ma=matrix('1,2,3;4,5,6;7,8,9')
print(ma)

mb=matrix('1,2,3;4,5,6;7,8,9')
print(mb)

mc=ma+mb
print(mc)

