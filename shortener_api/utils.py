import random
import string


def code_generator(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6, recursive_count=0):
    new_code = code_generator(size=size)
    Url_class = instance.__class__
    code_exist = Url_class.objects.filter(shortcode=new_code).exists()
    if code_exist:
        if recursive_count > 10:
            size += 1
        return create_shortcode(instance, size, recursive_count + 1)
    return new_code
