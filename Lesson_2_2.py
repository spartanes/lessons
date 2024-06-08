#Entering numbers
numbers = int(input('Введіть числа: '))
print('Ваші числа:', + numbers)
print('Ваші числа у стовбці: ')
print(numbers // 1000)
print((numbers % 1000) // 100)
print((numbers % 100) // 10)
print(numbers % 10)
