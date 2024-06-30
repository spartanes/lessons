number = int(input('Enter the number: '))

while number > 9:
    cnt = 1
    while number > 0:
        digit = number % 10
        cnt *= digit
        number //= 10
    number = cnt

print(number)