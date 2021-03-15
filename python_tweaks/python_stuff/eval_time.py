def wrap(n):
    def f():
        print(n)
    return f

numbers='one', 'two', 'three'
funcs=[]
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()
    