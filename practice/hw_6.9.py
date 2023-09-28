# q1: There is a calculated tax of 13% on the salary of 20000 NIS and more.
# Write the program that will get a salary as an input and will
# calculate and print a salary after a tax (in case of salary of 20000 and more), or will just print a salary.

# a = input("please enter word: ")
#
# if a == "python":
#     print("yes")
# else:
#     print("no")
# q2:
# a = int(input("enter salary: "))
#
# if a >= 20000:
#     print(f"this is your salary before tax: {a}")
#     print(f"this is your salary after tax: {abs(a * 0.13 - a)}")
# elif a <= 20000:
#     print(f"this is your salary: {a}")
# q3:
# a = int(input(" enter first number: "))
# b = int(input(" enter second number: "))
#
# if a >= b:
#     print(a)
# else:
#     print(b)
#
# a,b = map(int, input("Enter 2 numbers: ").split())
#
# if a > b:
#     print(a)
# else:
#     print(b)
# q3:
# a = input("enter first words please: ")
# b = input("enter second words please: ")
#
# c = b[::-1]
#
# if a == c:
#     print("yes")
# else:
#     print("no")
# q4:
# a = int(input("enter number: "))
# b = a % 2
# if b == 0:
#     print("even")
# else:
#     print("even")
# a,b = map(int,input("enter two number: ").split())
#
# if a > b:
#     print(f"{b} {a}")
# else:
#     print(f"{a} {b}")
# q5:
# q = input("enter question: ")
#
# if "?" in q:
#     print("question")
# else:
#     print("regular")
# q6:
# a,b,c = map(int,input("enter three numbers: ").split())
#
# if a == b and c:
#     print("3")
# elif a == b or c:
#     print("2")
# else:
#     print("0")
#q7:
a = int(input("enter number of month: "))
match a:
    case "1":
        print("Jan")
    case "2":
        print("feb")
    case "3":
        print("mar")
    case "4":
        print("apr")
    case "5":
        print("may")
    case "6":
        print("jun")
    case "7":
        print("jul")
    case "8":
        print("aug")
    case "9":
        print("sep")
    case "10":
        print("oct")
    case "11":
        print("nov")
    case "12":
        print("dec")
    case _:
        print("only 12 months in a year")



