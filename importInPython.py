import math
#or
from math import sqrt,pi #IT IS IMPORTING ONLY SQRT AND PI
#from math import * #all functions and variables are available
ans=math.sqrt(9)*pi
print(ans)
print(pi)

#or
from math import sqrt as s,pi
#import math as m
result=s(100)
print(result)

#DIR function
import math
print(dir(math))

#import from another file
from archit import archit,awasthi
archit()
print(awasthi)