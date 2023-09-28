print(range(5))
print(type(range(5)))
print(list(range(5)))

range_iter = iter(range(5))
print(range_iter)

print(next(range_iter))
print(next(range_iter))
print(next(range_iter))
print(next(range_iter))
print(next(range_iter))
print(next(range_iter))

this_list = [1, "name", True]
v = iter(this_list)
print(v)

print(next(v))
print(next(v))
print(next(v))
