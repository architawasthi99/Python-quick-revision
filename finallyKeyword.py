#code written  inside fianlly keyword execute everytime
try:
    l=[1,2,3,4,5,6,]
    i=int(input("ENTER THE INDEX: "))
    print(l[i])
except:
    print("SOME ERROR OCCURED")

finally:
    print("i am always executed")        