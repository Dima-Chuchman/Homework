total_sum = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        total_sum = total_sum + n

print(total_sum)