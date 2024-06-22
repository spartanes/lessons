#Entering a number and action
numbers_1 = int(input('Enter the first number: '))
numbers_2 = int(input('Enter the second number: '))
action = input('Enter action: ')

if action not in ('+', '-', '*', '/'):
    result = 'Enter the desired action: "+", "-", "*", "/".'
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
# else:
#     result = ('Enter the desired action: "+", "-", "*", "/".')

print(result)
