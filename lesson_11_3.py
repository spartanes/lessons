def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(limit):
    number = 2
    while number < limit:
        if is_prime(number):
            yield number
        number += 1

print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))
