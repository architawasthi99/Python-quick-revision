marks=[1,2,3,4,5]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[-2])
print('\n')

list=["archit","awasthi",45,90]
print(list[0][0])
print(list[0][3])
print(type(list[0])) #printing type of 1st character of list
 
 #CHECK ITEM IN LIST OR NOT
list2=[1,2,3,4,6,0]
if 7 in list2:
    print("yes")
else:
    print("no")    

#LIST SLICING
list3=["archit","awasthi","arjun","aradhya"]
print(list3[:]) #[start indx:end indx:jump]
print(list3[0:4:2])
print(len(list3))

#LIST COMPREHENSION
#can create list from list,tuples,dict,array,strings
lst=[i for i in range (10)] #new_list=[expression for item in iterable]
print(lst)

#print squares in new list
lst1=[1,2,3,4,5,6,7,8,9,10]
lst2=[num*num for num in lst1]
print(lst2)
lst3=[num for num in lst1 if num%2==0]
print(lst3) #printing only even

#with string
names=["archit","awasthi","saloni","satya"]
names1=[name[0] for name in names]
print(names1)

#else-if in list comprehension
numbers9=[1,2,3,4,5,6,7,8,9,10]
result=["even" if num%2==0 else "odd" for num in numbers9]
print(result)