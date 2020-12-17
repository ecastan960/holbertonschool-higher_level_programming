#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    k = 0
    sum1 = 0
    for i in my_list:
        for j in my_list:
            if j == i and a == 0:
                sum1 = sum1 + j
                a = 1
            elif j == i and a == 1:
                my_list[k] = 0
            k = k + 1
        a = 0
        i = 0
        k = 0
    return sum1
