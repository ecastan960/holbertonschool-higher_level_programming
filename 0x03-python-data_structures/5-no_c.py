#!/usr/bin/python3
def no_c(my_string):
    i = 0
    Lmy_string = list(my_string)
    for x in my_string:
        if 'c' == x:
            Lmy_string.pop(i)
        elif 'C' == x:
            Lmy_string.pop(i)
        else:
            i = i + 1
    my_string = ''.join(Lmy_string)
    return my_string
