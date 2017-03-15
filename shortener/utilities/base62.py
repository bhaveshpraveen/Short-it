import string

possible_characters = tuple(string.digits + string.ascii_uppercase + string.ascii_lowercase)
dict = {v: k for k, v in enumerate(possible_characters)}

# The encode function is used to encode a number to a string
def encode(num):
    # if num is zero then invoke the if statement
    if not num:
        return possible_characters[0]
    encoding = ""
    while(num>0):
        rem = num%64
        encoding = possible_characters[rem] + encoding
        num //= 62
    return encoding

def base_decode(string):
    num = 0
    for char in string:
        num = num * 62 + dict[char]
    return num

# The original base 62 algorithm
#
#
# def encode(num, alphabet=BASE62):
#     """Encode a positive number in Base X
#
#     Arguments:
#     - `num`: The number to encode
#     - `alphabet`: The alphabet to use for encoding
#     """
#     if num == 0:
#         return alphabet[0]
#     arr = []
#     base = len(alphabet)
#     while num:
#         num, rem = divmod(num, base)
#         arr.append(alphabet[rem])
#     arr.reverse()
#     return ''.join(arr)
#
# def decode(string, alphabet=BASE62):
#     """Decode a Base X encoded string into the number
#
#     Arguments:
#     - `string`: The encoded string
#     - `alphabet`: The alphabet to use for encoding
#     """
#     base = len(alphabet)
#     strlen = len(string)
#     num = 0
#
#     idx = 0
#     for char in string:
#         power = (strlen - (idx + 1))
#         num += alphabet.index(char) * (base ** power)
#         idx += 1
#
#     return num