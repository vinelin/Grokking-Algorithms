def count(list):
    if list == []:
        return 0
    else:
        return 1+count(list[1:])


print(count([1, 2, 3, 4]))