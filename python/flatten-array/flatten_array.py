def flatten(iterable):
    flattened = []
    for i in iterable:
        if isinstance(i,list) or isinstance(i,tuple):
            flattened.extend(flatten(i)) 
        else:
            flattened.append(i)
    return [x for x in flattened if x is not None]
