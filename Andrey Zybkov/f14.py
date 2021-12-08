def f(a, b):
    counter = 0

    for i in range(a, b+1):
        if i % 12 == 0:
            counter += 1

    return counter

print(f(5, 100))