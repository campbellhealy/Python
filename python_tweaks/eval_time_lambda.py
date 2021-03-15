numbers = 'one', 'two', 'three'
print(type(numbers))  # For Information Only
funcs=[]
print(type(funcs))  # For Information Only
for n in numbers:
    funcs.append(lambda: print(n)) # Why is there an error?

# Run the code like this then run again indenting the following code
for f in funcs:
    f()
    