users = []
# q2=  Add 'kevin', 'bob', and 'alice' to the users list in that order without reassigning the variable.
users.insert(0, 'kevin')
users.insert(1, 'bob')
users.insert(2, 'alice')
print("Users =", users)

# q3= Remove 'bob' from the `users` list without reassigning the variable.
users.pop(1)
print("Users =",users)

# q4= Reverse the users list and assign the result to `rev_users`.
users.reverse()
print("rev_Users =",users)
# q5 = Add the user 'melody' to users where 'bob' used to be.
users.insert(1, 'melody')
print("Users =",users)
# q6 = Add the users 'andy', 'wanda', and 'jim' to the users list using a single command.
names_to_insert = ['andy', 'wanda', 'jim']
users+= names_to_insert
print(users)
# q7 = Slice the users lists to return the 3rd and 4th items and assign the result to `center_users`
center_users = users[2:4]

print(center_users)

# practice
# practice 1#
list_integers =  input("enter a list of numbers: ")

numbers =[int(x) for x in list_integers.split()]

print(sum(numbers)/ len(numbers))
# practice 2#

numbers = list((map(int, input("enter a list of numbers: ").split())))
if 777 in numbers:
    print("True")
else:
    print("there isnt 777 in the list so false")

# practice 3#

A = ['100', '-50', '15', '85', '5', '20', '-5']

print("sorted list: ", sorted(A))
print("reversed sorted list: ", sorted(A, reverse=True))

# practice 4#
a = list(map(int, input("please enter number here: ").split()))
print(a[-3:])