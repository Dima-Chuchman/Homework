cs = 1
while True:
    k, n, t = map(int, input().split())
    if k == 0 and n == 0 and t == 0:
        break

    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * k) % (10 ** t)
        k = (k * k) % (10 ** t)
        n //= 2

    print(f"Case #{cs}: {result}")
    cs += 1
