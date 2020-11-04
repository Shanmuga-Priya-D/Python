#filter
#map
#reduce
from functools import reduce

nums=[1,2,3,4,5]

evens=list(filter(lambda n:n%2==0,nums))
print(evens)

doubles=list(map(lambda n:n+2,evens))
print(doubles)

def add_all(a,b):
    return a+b


sum=reduce(add_all,doubles)
print(sum)

print("or")

sums=reduce(lambda a,b:a+b,doubles)
print(sums)