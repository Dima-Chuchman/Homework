while True:
    p, q = map(int, input().split())

    if p < 0 and q < 0:
        break

    def suma(p):
        if p == 0:
            return 0
        F = p % 10
        return F * (1 + F) // 2 + p // 10 * 45 + suma(p // 10)

    def S(p, q):
        return suma(q) - suma(p - 1)

    result = S(p,q)
    print(result)