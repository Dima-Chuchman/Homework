n = int(input())
m = list(map(int, input().split()))

if len(m) != n:
    print()
else:
    mimimum = min(m)
    print(mimimum)