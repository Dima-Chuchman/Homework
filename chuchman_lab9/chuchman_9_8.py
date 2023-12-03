n = int(input())
m = list(map(int, input().split()))

numbers = set()

for i in range(n):
    numbers.add(abs(m[i]))

print(len(numbers))
