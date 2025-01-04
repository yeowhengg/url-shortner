base62Digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def convertToBase62(decimal):
    base62 = ""
    number = decimal
    while int(number) > 0:
        remainder = number % 62
        base62 = base62Digits[int(remainder)] + base62
        number /= 62
    return base62
    