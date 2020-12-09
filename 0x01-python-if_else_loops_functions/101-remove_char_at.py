def remove_char_at(str, n):
    if n < 0:
        return str
    s = str[0:n]+str[n + 1:]
    return s