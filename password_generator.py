import random
import string


def password_generator(length):
    password = []
    for i in range(length):
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
    random.shuffle(password)
    password = ''.join(password)
    return password


print(password_generator(5))
