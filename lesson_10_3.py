def sequence_generator(func, first_value, n):
    current_value = first_value
    for _ in range(n):
        yield current_value
        current_value = func(current_value)

def arithmetic_progression(x):
    return x + 2

gen = sequence_generator(arithmetic_progression, 1, 5)
print(list(gen))

def geometric_progression(x):
    return x * 3

gen = sequence_generator(geometric_progression, 1, 5)
print(list(gen))

def square(x):
    return x ** 2

gen = sequence_generator(square, 2, 3)
print(list(gen))
