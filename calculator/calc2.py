guide = '''
OPERATION           KEY
   +                Add
   -              Subtract
   *              Multiply
   /               Divide
   %              Remainder
  Quit        Turn Off Calculator
   '''
print (guide)
operation = ''
while operation != 'quit':
    operation = input('Enter Key: ')
    if operation == 'quit':
        break
    first_number = float(input('1st number: '))
    second_number = float(input('2nd number: '))

    if operation == 'add':
        print(f"{first_number} + {second_number} = {first_number + second_number}")
        
    elif operation == 'subtract':
        print(f"{first_number} - {second_number} = {first_number - second_number}")

    elif operation == 'multiply':
        print(f"{first_number} * {second_number} = {first_number * second_number}")

    elif operation == 'divide':
        if second_number == float('0'):
            print('Error: not divisible!!')
        else:
            print(f"{first_number} / {second_number} = {first_number / second_number}")

    elif operation == 'remainder':
        if second_number == float('0'):
            print('Error: not divisible!!')
        else:
            print(f"The remainder of {first_number} / {second_number} = {int(first_number) % int(second_number)}")
    
    else: 
        print('Invalid entry')