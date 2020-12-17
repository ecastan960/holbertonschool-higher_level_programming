#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = 0
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}
    r_string = list(roman_string)
    for x in r_string:
        if x in r_string:
            roman = roman + roman_dictionary.get(x)
    return roman
