# Example 1
# the_list = list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))

# Example 2
# the_list = list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))

# Example 3
from functools import reduce
the_list = reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])

print(the_list)
