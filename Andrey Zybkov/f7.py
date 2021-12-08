def f ():
    out = 1
    count = 0
    nums = list(map(int, input().split()))
    print(nums)
    for i in nums:
        if i >= 0:
            out *= i
            count += 1
    return count, out

while True:
    print(f())