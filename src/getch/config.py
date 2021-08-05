def loads(data: str) -> dict:
    d = data.replace(' ', '') 
    c = dict()
    k = ''
    for x in d.split():
        if (x[0] == '[') and (x[-1] == ']'):
            k = (x[1:-1])
            if not (k in c.keys()):
                c[k] = dict()
        else:
            x = x.split('=')
            x[1] = x[1].replace('\'', '')
            if (len(x) >= 2) and (x[0][0] != '#'):
                x = iter(x)
                y = zip(x, x)
                if (x == ''):
                    c.update(dict(y))
                else:
                    c[k].update(dict(y))
    return (c)

def load(file: str) -> dict:
    with open(file, 'r') as f:
        return loads(f.read())

def dumps(data: str) -> str:
    return '\n'.join(
        ['%s = %s' % (k, v) for k, v in data.items()]
    )

def dump(data: str, file: str) -> None:
    with open(file, 'w') as f:
        f.write(dumps(data))

__all__ = [
    'loads', 'load', 
    'dumps', 'dump'
]
