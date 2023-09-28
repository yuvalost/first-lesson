# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))
#
# for i in range(a, b):
#         print(f"Number {i}; power of 2 = {i ** 2}; power of 3 = {i **3} ")

# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))
#
# for i in range(a,b):
#     if i % 3 ==0:
#
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 ==0 and i % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(i)
# a = (input("Enter a first a text: "))
# b = int(input("Enter add number: "))
#
# for i in range (b):
#     print(a)

# num = [12, 75, 150, 180, 145, 525, 50]
#
# for i in num:
#     if i > 150:
#         continue
#     elif i > 500:
#         break
#     elif i % 5 == 0:
#         print(i)
# num = [10, 20, 30, 40, 50]
#
# a = reversed(num)
#
# for i in a:
#     print(i)
a = int(input("start= "))
b = int(input("end= "))

for i in range (a, b):
    if (a % i) == 0:
        print(i)