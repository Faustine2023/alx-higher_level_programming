#!/usr/bin/python3
def add_tuple(tuple_t=(), tuple_r=()):
    e = list(tuple_t)  # conveet tuples to list for modification
    f = list(tuple_r)

    while len(e) < 2:
        e.append(0)
    while len(f) < 2:
        f.append(0)

    e = e[:2]  # only two elements per tuple to be used
    f = f[:2]
    return (e[0] + f[0], e[1] + f[1])
