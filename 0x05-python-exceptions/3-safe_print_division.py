#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        float(result)
    except:
        result = None
    finally:
        print("Inside result: ", end='')
        print("{}".format(result))
        return result
