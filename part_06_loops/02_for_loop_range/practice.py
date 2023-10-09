# for i in range(a+1):
#     print(i)


# a = input("please enter a text")
# b = int(input("please enter integer: "))
# for i in range(b):
#     print(a)

num_start = int(input("enter start number: "))
num_end = int(input("enter end number: "))

for i in range(num_start, num_end):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 == 0:
        print("Bizz")
    else:
        print(i)