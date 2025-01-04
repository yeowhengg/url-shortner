from . import convert_base62, convert_base64

def to_shorten(link: str):
    base64 = convert_base64.str2int(link)
    print(convert_base62.convertToBase62(base64))
    return convert_base62.convertToBase62(base64)