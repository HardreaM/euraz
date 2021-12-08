def f (n):
    paths = 0

    for i in n:
        paths += len(i)

    n = n[1::]

    for i in n:
        if len(i) == 1:
            n.remove(i)

    return paths - len(n)

n = [
    {'a': {'c':1, 'd':1, 'e':1}},
    {'c': {'f':1, 'd':1}},
    {'d': {'f':1, 'g':1, 'e':1}},
    {'e': {'g':1}},
    {'f': {'g':1}},
    {'g': {'b':1}}
]

print(f(n))



'''
a = [
    {b: 1, c: 1, h:1}, #a
    {e:1, d:1}, #b
]
'''