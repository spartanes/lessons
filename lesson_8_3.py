def find_unique_value(numbers):
    for number in numbers:
        if numbers.count(number) == 1:
            return number

print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3, 5, 5]))
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))

