marks=[12,34,56,78,122,88]
index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("ARCHIT IS BRILLIANT STUDENT")
    index+=1 


print("\n")

# USING ENUMERATE FUNCTION

for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("ARCHIT IS BRILLIANT STUDENT")

#
fruits=["apple","banana","mango","leeche","berries"]
for index,fruit in enumerate(fruits):
    print(index,fruit) 
print("\n")
#
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)    
