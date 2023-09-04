# q1
day_dic = {
    1:31,
    2:28,
    3:31,
    4:31,
    5:31,
    6:31,
    7:31,
    8:31,
    9:31,
    10:31,
    11:31,
    12:31,
}
month = int(input("please enter the number if month: "))
print(type(month))

print(day_dic.get(month , f"{month} is not a month"))
# Q2
d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
d2.update(d1)
print(d2)
# q3

user = {
    "id": 4170,
    "uid": "4fkajflk-fafaf-faf-fafa-af",
    "password": "dsadsad",
    "first_name": "Yuval",
    "last_name": "ostrowsky",
    "user_name": "yuval_ostrowsky",
    "secret": "jimmy"
}

print(user)
print(user.pop("password"))
print(user.pop("last_name"))


user["id"] = user.pop('id')
user["last_name"] = user.pop('uid')
user["first_name"] = user.pop('secret')
print(user)
