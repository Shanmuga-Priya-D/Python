from numpy import *

#1.array()
#2.linspace()
#3.logspace()
#4.arange()
#5.zeros()
#6.ones()
print("---------------------1.ARRAY------------------------")
arr=array([1,2,3,4,5])
print(arr)
print(arr.dtype)

arr1=array([1,2,3,4,5],float)
print(arr1)
print(arr1.dtype)


print("-------------------2.LINSPACE-----------------------")
arr2=linspace(0,15,16)
print(arr2)

arr3=linspace(0,15,20)
print(arr3)

print("-------------------3.LOGSPACE-----------------------")
arr4=logspace(1,40,5)
print(arr4)
print('%2.f' %arr[4])


print("-------------------4.ARANGE-------------------------")
arr5=arange(1,15,2)
print(arr5)
print("-------------------5.ZEROS--------------------------")
arr6=zeros(5)
print(arr6)
print("-------------------6.ONES---------------------------")
arr7=ones(5)
print(arr7)
arr8=ones(5,int)
print(arr8)
