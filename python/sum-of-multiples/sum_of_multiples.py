def sum_of_multiples(limit, multiples):
    '''
    Given a number, find the sum of all the unique multiples of 
    particular numbers up to but not including that number.
    '''
    mult_set = set()
    for m in multiples:
        nums = set([x for x in range(1, limit) if x % m == 0])
        mult_set = mult_set.union(nums)

    return sum(mult_set)
    
