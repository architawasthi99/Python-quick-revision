class Person:
    name="Archit"
    occupation="Software Engineer"
    networth="100 billion"
a=Person() # a is object
#a.name="satya" we can edit by this
print(a.name, a.occupation, a.networth)   

#use of self keyword (object for which method is called)
class Person2:
    name="Aradhya"
    age=21
    occupation="Doctor"
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a1=Person2()
b1=Person2()
a.name="Tiwari"
a.occupation="Surgeon"
b1.name="Archit"
b1.occupation="Engineer"
a1.info()
b1.info()