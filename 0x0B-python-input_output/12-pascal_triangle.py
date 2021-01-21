#!/usr/bin/python3
"""[summary]
"""


def pascal_triangle(n):
    """[summary]

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    main_list = []
    for i in range(n):
        temp_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(main_list[i-1][j-1]+main_list[i-1][j])
        main_list.append(temp_list)
    return main_list
