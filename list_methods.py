list=[23,12,45,98,10]

list.append(11)
print(list)

list.sort()
print(list)

list.reverse()
print(list)

list.extend([1,2,3,4])
print(list)

list.insert(2,99)
print(list)

list.remove(98)
print(list)

list1=[1,2,3]
list1.pop()
print(list1)
list1.pop(1)
print(list1)

list2=[1,2,3,4,5,6,7,8]
list2.clear()
print(list2)

list3=[1,2,3,4,5,6,7,8]
list3.sort(reverse=True)
print(list3)


list8=[1,2,3]
new_list=list8.copy()
print(new_list)