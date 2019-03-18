def transform(legacy_data):
    results = {}
    for k in legacy_data.keys():
        for v in legacy_data[k]:
            results[v.lower()] = k

    return results
