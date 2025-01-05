chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_:/#."


def str2int(s, row):
    i = 0
    for c in reversed(s):
        i *= len(chars)
        i += chars.index(c)
    return i + row


def int2str(i):
    s = ""
    while i:
        s += chars[i % len(chars)]
        i //= len(chars)
    return s
