#List
list_1 = [1, 2, 3, 4, 5, 6]
list_2 = len(list_1)
result = []
if list_2 == 0:
    result = [[], []]
elif list_2 % 2 == 0:
    middle = list_2 // 2
    result = [list_1[:middle], list_1[middle:]]
else:
    middle = (list_2 // 2) + 1
    result = [list_1[:middle], list_1[middle:]]
print(result)