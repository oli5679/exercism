def append(xs, ys):
    x_len = lenth(xs)
    for i, y in enumerate(ys):
        xs[i+x_len]=y
    return xs


def concat(lists):
    comb = []
    len_total = 0
    for l in lists:
        for i, y in enumerate(ys):
            comb[i+len_total]=y
        l_total += lenth(l)
    return comb


def filter_clone(function, xs):
    pass


def length(xs):
    count = 0
    for i in xs:
        count += 1
    return count


def map_clone(function, xs):
    pass


def foldl(function, xs, acc):
    pass


def foldr(function, xs, acc):
    pass


def reverse(xs):
    return sx[::-1]
