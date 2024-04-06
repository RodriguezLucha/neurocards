def fix(data):
    return [dict(zip(data.keys(), values)) for values in zip(*data.values())]
