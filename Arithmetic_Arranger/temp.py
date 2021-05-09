operators = {
    '+': lambda pair: str(pair[0] + pair[1]),
    '-': lambda pair: str(pair[0] - pair[1]),
}

signk = operators.keys()
signv = operators.values()

print(signk,'\n', signv)