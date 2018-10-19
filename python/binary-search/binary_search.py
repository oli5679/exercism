def binary_search(list_of_numbers, number):
    l, r = 0, len(list_of_numbers) - 1
    while l <= r:
        m = (l + r) // 2
        if list_of_numbers[m] < number:
            l = m + 1
        elif list_of_numbers[m] > number:
            r = m - 1
        else:
            return m
    raise ValueError('Number not in list')