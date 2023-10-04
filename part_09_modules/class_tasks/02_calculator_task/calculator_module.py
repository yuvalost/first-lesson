

def _add(x,y):
    return x + y

def _subtract(x,y):
    return  x - y

def _multiplay(x,y):
   return x * y

def _divide(x,y):
    if y == 0:
        raise ValueError("sorry cant be zero try again")
    return x / y

def calculate(x:float , y: float ,operation: str ):

    match operation:
        case '+':
            return _add(x, y)
        case '-':
            return _subtract(x, y)
        case '*':
            return _multiplay(x, y)
        case '/':
            return _divide(x, y,)

        case _:
            raise ValueError("its is an invalid operation, please try agin...")

# def calculate(x: float, y: float , operation: str):

    # operation = int(input("options: \n1.+\n2.-\n3.*\n4./"))
    # while operation < 1 or operation > 4:
    #     print("Wrong choice! please try again")
    #     choice = int(input("options: \n1.+\n2.-\n3.*\n4./"))
    # if choice == "1":
    #         _add(x, y)
    # elif choice == "2":
    #         _subtract(x, y)
    # elif  choice == "3":
    #         _multiplay(x, y)
    # elif  choice == "4":
    #         _divide(x, y)


