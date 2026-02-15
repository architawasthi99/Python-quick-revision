dict={
    "name":"archit awasthi",
    "cgpa":8.2,
    "marks":[98,99,100]
}
print(dict)
print(type(dict))
print(dict["name"])
print(dict.get("name"))
print(dict.keys())
print(dict.values())

for key in dict.keys():
    print(f" THE VALUE CORRESPONDING TO THE KEY {key} is {dict[key]}")
#list and tuples can also be stored
print(dict.items())
for key,value in dict.items():
    print(f"THE VALUE CORRESPONDING TO THE KEY {key} is {value}")

#  nested dict
students={
    "name":"satya",
    "score":{
        "che":98,
        "phy":93
    }
}
print(students)
print(students["name"])
print(students["score"])
print(students["score"]["phy"])