#Entering a number and action
while True:
    numbers_1 = input('Enter the first number: ')
    if not numbers_1.isdigit():
        print('Not found! Try again!=)')
        continue
    numbers_1 = float(numbers_1)

    action = input('Enter action: ')
    if action not in ('+', '-', '*', '/'):
        print('Enter the desired action: "+", "-", "*", "/".')
        continue

    numbers_2 = input('Enter the first number: ')
    if not numbers_2.isdigit():
        print('Not found! Try again!=)')
        continue
    numbers_2 = float(numbers_2)

    result = 0

#Multiplication
    if action == '*':
        result = numbers_1 * numbers_2
#Divide
    elif action == '/' and numbers_2 == 0:
        result = 'ERROR 404 :('
    elif action == '/':
        result = numbers_1 / numbers_2
#Addition
    elif action == '+':
        result = numbers_1 + numbers_2
#Subtraction
    elif action == '-':
        result = numbers_1 - numbers_2

    print(result)

    cont = input('Continue? Y/N')
    if cont.lower() != 'y':
        print('Good bay!')
        break