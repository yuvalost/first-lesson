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
slice_users = users[2:4]
print(slice_users)
