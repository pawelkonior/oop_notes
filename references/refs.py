x = {'x': 42}


def magic(param):
    param['x'] += 1
    print(param)


magic(x)
print(x)
