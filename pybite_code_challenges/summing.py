#summing.py

def sum_numbers(numbers=None):
    if numbers == []:  
        return 0
    elif numbers:
        return sum(numbers)
    else:
        return sum(range(1,101))

print(sum_numbers([]))
print(sum_numbers(range(1, 11)))
print(sum_numbers([1, 2, 3]))
print(sum_numbers((1, 2, 3)))
# print(sum_numbers())
# print(sum_numbers())
# print(sum_numbers())