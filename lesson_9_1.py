def difference(*args):
    if not args:
        return 0
    max_value = max(args)
    min_value = min(args)
    return max_value - min_value

assert difference(1, 2, 3)
assert difference(5, -5)
assert difference(10.2, -2.2, 0, 1.1, 0.5)
print('OK')
