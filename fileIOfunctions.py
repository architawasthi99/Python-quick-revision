#seek (sets the pointer)
#MOVE TO BEGINNING
with open("demotext2.txt","r") as f:
    print(type(f))
    print(f.read(5))
    f.seek(0)
    print(f.read(5))

#MOVE FORWARD
with open("demotext2.txt","r") as f:
    f.seek(10)
    print(f.read())
    print(f.tell()) #gives pointer location    

#TRUNCATE
with open("demotext2.txt","w") as f:
    f.write("archit awasthi")
    f.truncate(5)
with open("demotext2.txt","r") as f:
    print(f.read())    
