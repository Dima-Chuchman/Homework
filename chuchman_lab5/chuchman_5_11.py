n = int(input())
m = list(map(int, input().split()))

array = [0] * n

for i in range(n):
    array[(i + 1) % n] = m[i]

print(*array)