import string
import random


def rand_str(n: int = 6):
    """ 生成随机字符串 """
    population = string.ascii_letters
    letters = random.choices(population=population, k=n)
    return ''.join(letters)
