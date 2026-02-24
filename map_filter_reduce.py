#WITHOUT MAP
def cube(x):
    return x*x*x
l=[1,2,3,4,5,6,7,8,9,10]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)    

#THIS CAN BE DONE USING MAP
l=[1,2,3,4,5,6,7,8,9,10]
newl=list(map(lambda x:x*x*x,l))
print(newl)

#FILTER
def filter_function(a):
    return a>5
newnewl=list(filter(filter_function,l))
print(newnewl)

#print only even using filter
l2=[1,2,3,4,5,6,7,8,9,10,11,12,24]
even=list(filter(lambda x:x%2==0,l2))
print(even)

#REDUCE FUNCTION (TAKE 2 INPUT GIVES 1 OUTPUT)
from functools import reduce
numbers=[11,12,13,14,15,16,17,18,19,20]
sum=reduce(lambda x,y:x+y,numbers)
print(sum)