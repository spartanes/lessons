list_1 = [12, 3, 4, 10]
if len(list_1) >= 1:
    list_2 = list_1.pop()
    list_1.insert(0, list_2)
    print(list_1)
else:
    print([])