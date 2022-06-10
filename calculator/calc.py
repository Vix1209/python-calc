import operator

operand = ''
while operand != 'quit':
    firstparam = float(input('num 1 > '))
    secondparam = float(input('num 2 > '))
    operand = input('operator > ')
    if operand == 'quit':
        break
    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '%' : operator.mod
    }

    result = ops[operand](firstparam, secondparam)
    print (result)