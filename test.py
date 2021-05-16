def fill(n):
    a = [0] * n
    lo = (n - 1) // 2
    hi = (n - 1) - lo
    for i in range(1, lo + 1):
        a[i] = 2 * i

    for i in range(1, hi + 1):
        a[n - i] = 2 * i - 1

    print(a)

fill(10)
fill(11)
