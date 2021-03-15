numbers = 'one', 'two', 'three'
funcs=[]
for n in numbers:
    funcs.append(lambda: print(n))

for f in funcs:
    f()
    