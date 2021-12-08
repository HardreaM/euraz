def f (n):
    n1 = 0
    n2 = 1
    print(fib(n1, n2, n-3))

def fib (n1, n2, n):
    if n == 0:
        return n1+n2
    else:
        return fib(n2, n1+n2, n-1)

f(5)