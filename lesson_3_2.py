#Entering a number and action
numbers_1 = int(input('Enter the first number: '))
numbers_2 = int(input('Enter the second number: '))
action = input('Enter action: ')
#Multiplication
if action == '*':
    print('Result:', numbers_1 * numbers_2)
#Divide
elif action == '/':
    print('Result:', numbers_1 / numbers_2)
#Addition
elif action == '+':
    print('Result:', numbers_1 + numbers_2)
#Subtraction
elif action == '-':
    print('Result:', numbers_1 - numbers_2)
else:
    print('Enter the desired action: "+", "-", "*", "/".')
