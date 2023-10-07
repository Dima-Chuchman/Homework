n = int(input())

result = 1

while result**3 < n:
    print(result**3, end=' ')
    result = result + 1

print()
