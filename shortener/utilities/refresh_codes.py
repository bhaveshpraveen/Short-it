from shortener.models import shortit
import random
import string


possible_characters = tuple(string.digits + string.ascii_uppercase + string.ascii_lowercase)


def random_code_generator():
    length = random.randrange(7, 16)
    code = ''
    for _ in range(length):
        code += random.choice(possible_characters)
    return code


def refresh_codes():
    codes_generated = 0
    objs = shortit.objects.all()
    count = shortit.objects.count()
    for obj in objs:
        obj.code = random_code_generator()
        obj.save()
        codes_generated += 1
    return "Total number of codes present {}.\nThe number of codes refreshed = {}".format(count, codes_generated)
