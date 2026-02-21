#OPEN AND WRITE
f=open("demo.txt","w")
f.write("VS Code works with local files on your computer")
f.close()

#REOPEN AND READ
f=open("demo.txt","r")
print(f.read())
f.close()

#WRITE IN FILE
f=open("demo.txt","w")
f.write("hello everyone chill")
f.close()

#APPEND
f=open("demo.txt","a")
f.write(" hello,hello")
f.close()

# READ + WRITE
f=open("demo.txt","w+")
f.write("TODAY IS SATURDAY")
f.seek(0)  #brings cursor at beginning
print(f.read())
f.close()