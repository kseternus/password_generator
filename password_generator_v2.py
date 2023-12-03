import random
import string

# v2 a shorter and more simplified version of the password generator which, unlike v1, generates any password length
# instead of the base 4 length and its multiples


def password_gen_v2(lenght):
    chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
    password = ''.join(random.choice(chars) for _ in range(lenght))
    return password


print(password_gen_v2(16))
