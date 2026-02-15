x=int(input("enter the value of x: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _:
        print(x)        
