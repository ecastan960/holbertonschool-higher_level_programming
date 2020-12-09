def uppercase(str):
    for letter in str:
        x = ord(letter)
        if x > 96 and x < 123:
            x = x - 32
        print("{:c}".format(x), end='')
    print()
