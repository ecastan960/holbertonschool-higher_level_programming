#!/usr/bin/python3
def weight_average(my_list=[]):
    w1 = 0
    w2 = 0
    if my_list == []:
        return 0
    for x in range(len(my_list)):
        w1 = w1 + (my_list[x][0] * my_list[x][1])
        w2 = w2 + my_list[x][1]
    average = w1 / w2
    return average
