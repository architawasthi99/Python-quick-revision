#MAKE A VARIABLE AND USE IT AS A FUNCTION
double=lambda x: x*2
cube=lambda x: x*x*x
avg= lambda x,y: (x+y)/2
print(double(5))
print(cube(5))
print(avg(5,2))

#WE CAN PASS FUNCTION AS AN ARGUEMENT IN ANOTHER FUNCTION
def apply(fx,value):
    return 6+fx(value)
print(apply(lambda x:x*x*x,2))