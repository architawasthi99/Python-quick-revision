tup=(1,2)
print(type(tup))
tup1=(1,)
print(type(tup1))
print(tup[0])

if 34 in tup:
    print("yes")
else:
    print("no")    

tup2=(i for i in range(10))
print(tup2)    

#tuples operaton

countries=("india","china","russia","vietnam","england")
temp=list(countries)
temp.append("bharat")
print(temp)
temp.pop(4)
print(temp)
temp[2]="finland"
print(temp)
countries=tuple(temp)
print(countries)
print(countries.count("bharat"))