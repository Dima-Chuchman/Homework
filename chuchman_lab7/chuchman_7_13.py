n, m = map(int, input().split())

result = []

for number in range(n, m + 1):
    number_str = str(number)
    if len(number_str) == 4:
        digits = set(number_str)
        if len(digits) == 4:
            result.append(number_str)

print(' '.join(result))
