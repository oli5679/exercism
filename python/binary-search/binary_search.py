def binary_search(list_of_numbers, number):
    n = len(list_of_numbers)
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if list_of_numbers[m] < number:
            l = m + 1
        elif list_of_numbers[m] > number:
            r = m - 1
        else:
            return m
    raise ValueError('Number not in list')