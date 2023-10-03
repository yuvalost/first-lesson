

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

def calculate(x: float, y: float , operation: str):

    while operation == "":
        choice = input("options: \n1.+\n2.-\n3.*\n4./")
        if choice == "1":
            _add()
        elif

    match operation:
        case '+':
            return _add(x, y)
        case '-':
            return _subtract(x, y)
        case '*':
            return _multiplay(x, y)
        case '/':
            return _divide(x, y)


        case _:
            raise ValueError("its is an invalid operation, please try agin...")
