#DECORATORS ARE THE FUNCTION WHICH RETURN ANOTHER FUNCTION AFTER UPDATING IT
def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this function")
    return mfx
@greet
def hello():
    print("helloworld")
hello()

#WHEN YOUR FUNCTION HAS ARGUEMENTS
def deco(fx):
    def mfx(*args,**kwargs):#args takes input as tuple and kwargs takes input as dicionary
        print("YOUR ADDITION IS:- ")
        fx(*args,**kwargs)
        print("ARE YOU SATISFIED")
    return mfx    
def add(a,b):
    print(a+b)
deco(add)(1,2)    
