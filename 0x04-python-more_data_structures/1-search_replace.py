#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = 0
    new = my_list.copy()
    for i in my_list:
        if i == search:
            new[a] = replace
            a = a + 1
        else:
            a = a + 1
    return new
