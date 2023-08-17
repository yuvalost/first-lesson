letters = "abcdefg"

print("the first element letter: ", letters[0])

name = "yuval ostrowsky"
print("the first element name: ", name[-1])
name_len = (len(name))
print("the first element name: ", name[name_len-1])
print("the first element name: ", name[::-1])
print("the first element name: ", name[::2])
print("the first element name: ", name[0]+name[:0:-1])
print("the first element name: ", name[0:-2:])
print("yuval".upper() )
print("yuval".lower() )
print("yuval".capitalize()  )
name = "moshe"
print(id(name))
print(id(name.upper()))
print(id(name))
print(name)
name = "yuval"
print("Yuval" in name)
print("Yuval".lower() in name)

a = int(input("enter number: "))
b = "d"
print(type(a))
print(type(b))
print(a.isalpha())
print(b.isalpha())
print(a.isdigit())
print(b.isdigit())