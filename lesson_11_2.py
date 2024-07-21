def generate_cube_numbers(limit):
    n = 2
    while True:
        cube = n ** 3
        if cube >= limit:
            return
        yield cube
        n += 1

for cube in generate_cube_numbers(100):
    print(cube)

print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))
print(list(generate_cube_numbers(1000)))
