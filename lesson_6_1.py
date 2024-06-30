import string

str = input('Type in the word: ')

str_1, str_2 = str.split('-')

all_letters = string.ascii_letters

start = all_letters.index(str_1)
end = all_letters.index(str_2)

result = all_letters[start:end + 1]
print(result)