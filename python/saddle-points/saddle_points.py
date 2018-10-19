def saddle_points(matrix):
    if matrix == []:
        return set()
    if min([len(r) for r in matrix]) != max([len(r) for r in matrix]):
        raise ValueError('Irregular Matrix size')
    saddle_points = set()
    for i, r in enumerate(matrix):
        for j, c in enumerate(r):
            if c == max(r):
                if c == min([r_[j] for r_ in matrix]):
                    saddle_points.add((i, j))
    
    return saddle_points
