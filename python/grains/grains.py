def on_square(integer_number):
    if integer_number % 1 != 0:
        raise ValueError('must be integer, not {}'.format(integer_number))
    if integer_number > 64 or integer_number < 1:
        raise ValueError('must be between 1 and 64, not {}'.format(integer_number))
    else:
        return 2 ** (integer_number - 1)


def total_after(integer_number):
    if integer_number % 1 != 0:
        raise ValueError('must be integer, not {}'.format(integer_number))
    if integer_number > 64 or integer_number < 1:
        raise ValueError('must be between 1 and 64, not {}'.format(integer_number))
    else:
        return 2 ** (integer_number) - 1

