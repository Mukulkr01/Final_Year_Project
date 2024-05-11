# users/utils.py
import string
import random

def generate_auto_id():
    prefix = 'SMj'
    suffix = ''.join(random.choices(string.digits, k=5))
    return f"{prefix}{suffix}"
def generate_auto_c_id():
    prefix = 'CMD'
    suffix = ''.join(random.choices(string.digits,k=5))
    return f"{prefix}{suffix}"
