import keyword

string = input('Type in the words: ')
result = False

if string.count('_') == len(string) and len(string) > 1:
    result = False

if string in keyword.kwlist:
    result = False

if string.isidentifier():
    if string == '_' or string.islower():
        result = True

print(result)

