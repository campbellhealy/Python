def arithmetic_arranger(problems, result=False):
    """
    Receives a list of strings that are arithmetic problems, (horizontal format)
    Return the problems arranged vertically a well as side-by-side. 
    If result is set to True, the answers are displayed.

    Situations that will return an error:
        `Error: Too many problems.`
            **too many problems** supplied to the function. The limit is **five**
        `Error: Operator must be '+' or '-'.`
            The function will accept are **addition** and **subtraction** operators. 
            Multiplication and division will return an error. 
            Other operators not mentioned in this bullet point will not need to be tested.
        `Error: Numbers must only contain digits.`
            Each number (operand) should only contain digits.
        `Error: Numbers cannot be more than four digits.`
            Each operand has a max of four digits in width.

    The conversion should return:
        There should be a single space between the operator and the longest of the two operands, 
        The operator will be on the same line as the second operand, 
        Both operands will be in the same order as provided
        Numbers should be right-aligned.
        There should be four spaces between each problem.
        There should be dashes after the second_operand of each problem. The dashes should run along the entire length of each problem individually.
    
    Note: Do not change the default result value in arithmetic_arranger as this breaks the unit tests
        Add a second parameter to the request in main.py
    """
    # Too many problems - Count the number of items supplied to the function If this is greater than five then console log an error.
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialise the dict for the operators and lists for the item strings
    operators = {
        '+': lambda pair: str(pair[0] + pair[1]),
        '-': lambda pair: str(pair[0] - pair[1]),
        # '*': lambda pair: str(pair[0] * pair[1]), # Error Checking
        # '/': lambda pair: str(pair[0] / pair[1]), # Error Checking
    }
    arranged_problems = []
    first_operands = []
    second_operands = []
    lines = []
    results = []

    for problem in problems: # Separate each problem
        items = problem.split() # Split the problem into the three components
        max_len = len(max(items, key=len))
        # print(f'Max Length is {max_len}')
        if not all([i.isnumeric() for i in items[::2]]):
            return "Error: Numbers must only contain digits."
        elif items[1] not in operators.keys(): # Check the operator is either +/- against the dict
            return "Error: Operator must be '+' or '-'."
        elif max_len > 4:
            return "Error: Numbers cannot be more than four digits."

        line_len = max_len + 2 # This give a value the length of the largest operand plus two to cover operator and space

        line = '-' * line_len
        first_num = items[0].rjust(line_len, ' ')
        second_num = f"{items[1]}{' ' * (line_len - len(items[2]) - 1)}{items[2]}"

        # Build lists
        first_operands.append(first_num)
        second_operands.append(second_num)
        lines.append(line)

        if result:
            res = operators[items[1]]([int(i) for i in items[::2]])
            results.append(f"{res.rjust(line_len, ' ')}")

    # Output to be returned
    arranged_problems = '\n'.join(['    '.join(i)
                                   for i in (first_operands, second_operands, lines)])

    if results:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems