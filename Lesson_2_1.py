#Введеня чисел

numbers = int(input('Введіть числа: '))
print('Ваші числа:', + numbers)

#Виводимо числа окремо

numbers_1 = numbers // 10000
numbers_2 = (numbers % 10000) // 1000
numbers_3 = (numbers % 1000) // 100
numbers_4 = (numbers % 100) // 10
numbers_5 = numbers % 10

#Перегоргаємо числа

numbers_reverse = numbers_5 * 10000 + numbers_4 * 1000 + numbers_3 * 100 + numbers_2 * 10 + numbers_1
print('Ваші числа навпаки:', + numbers_reverse)


