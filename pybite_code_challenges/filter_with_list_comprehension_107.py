numbers = list(range(-10, 11))
numbers = [2, 4, 51, 44, 47, 10]
numbers = [0, -1, -3, -5]



def filter_positive_even_numbers(numbers):
    """
    Receives a list of numbers, 
    Returns a filtered list
    Numbers that are both positive and even (divisible by 2)
    try to use a list comprehension.
    """


    filtered_list = [number for number in numbers if (number % 2 == 0 and number > 0)]
    return filtered_list

print(filter_positive_even_numbers(numbers))   

