def wrap(n):
    def f():
        print(n)
    return f

numbers='one', 'two', 'three'
print(type(numbers))  # For Information Only
funcs=[]
print(type(funcs))  # For Information Only
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()
    