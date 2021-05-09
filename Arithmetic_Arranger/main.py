# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main

'''
To obtain the result to each problem add the second argument 'True'
Otherwise leave blank as the default for result is False
'''
print(arithmetic_arranger(["23 + 998", "3671 - 244", "56 + 243", "432 + 94"], True))
print()
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main(module='test_module', exit=False)