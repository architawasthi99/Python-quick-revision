#READLINES
f=open("demo.txt","r")
while True:
    line=f.readline()
    if not line:
        break
    print( line)
f.close() 

#USING SPLIT
f=open("demotext2.txt","r")
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Marks of student {i} in Maths is: {m1}")
    print(f"Marks of student {i} in english is: {m2}")
    print(f"Marks of student {i} in physics is: {m3}")

#WRITELINES
f=open("demotext2.txt","w")
lines=["hello\n","world\n","hell\n"]
f.writelines(lines)
f.close()