def uppercase(str):
    for letter in str:
        x = ord(letter)
        if letter >= 'a' and letter <= 'z':
            letter = chr(x - 32)
        print("{}".format(letter), end='')
    print()
