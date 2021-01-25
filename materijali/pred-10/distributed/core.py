from math import sqrt


def is_prime(num):
    if num <= 2:
        return True

    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False

    return True

def gen_input_params(max_num):
    for x in range(1, max_num+1):
        for y in range(1, max_num+1):
            num = x * y + 1
            yield x, y, num
