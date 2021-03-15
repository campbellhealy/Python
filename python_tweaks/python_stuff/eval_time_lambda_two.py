numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda x=n: print(x))

for f in funcs:
    f()
