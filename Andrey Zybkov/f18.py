def f (n):
    n = str(n)
    for i in range(10):
        if n.count(str(i)) > 1:
            print(i, n.count(str(i)))

f(14315733)