def immutable(string, n):
    #A1F
    lst = ' '.join(string).split()
    if len(n) > 1:
        new = ' '.join(n).split()
        return lst + new
    return lst + [n]
