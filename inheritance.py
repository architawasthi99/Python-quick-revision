#WHEN A CLASS IS DERIVED FROM ANOTHER CLASS
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"THE NAME OF EMPLOYEE IS {self.name} AND HIS ID IS {self.id}")
#now if we want to change the class name then it would cause errors so we use inheritance
class Programmer(Employee):
    def show(self):
        print("THE DEFAULT LANGUAGE IS PYTHON")

class Software(Programmer):
    def pro(self):
        print("hello everyone")
e=Software("Archit",2234)
e.showdetails()   
e.show()
e.pro()         
        