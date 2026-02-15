#COLLECTION OF UNORDERED ITEMS ,IMMUTABLE,UNIQUE
nums={1,2,3,4,5}
print(type(nums))
nums1=set() #empty set

set1={1,1,2,2,3,4,5,6,7,5}
print(set1) #only unique

for val in set1:
    print(val,end=",")

#SET METHODS
s1={1,2,3,"archit","awasthi",45}
s2={"satya","arjun","keju","archit","awasthi"}

print(s1,s2)
print(s1.union(s2))

print(s1.intersection(s2))

s1.add(99)
print(s1)

s1.remove("archit")
print(s1)

s1.pop()
print(s1)

s1.clear()
print(s1)