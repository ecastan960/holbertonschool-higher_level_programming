#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    y = 0
    new_list = my_list.copy()
    if my_list == []:
        return None
    for x in range(len(my_list)):
        if my_list[y] % 2 == 0:
            new_list[x] = True
        else:
            new_list[x] = False
        y = y + 1
    return new_list
