n = int(input())

if n == 1:
    total_sum = 0
    for i in range(100, 1000):
        digit1 = i // 100
        digit2 = (i // 10) % 10
        digit3 = i % 10
        if digit1 % 2 == 0 and digit2 % 2 == 0 and digit3 % 2 == 0:
            total_sum += i
    print(total_sum)

elif n == 2:
    count = 0
    for i in range(100, 1000):
        digit1 = i // 100
        digit2 = (i // 10) % 10
        digit3 = i % 10
        if digit1 < digit2 < digit3:
            count += 1
    print(count)

elif n == 3:
    total_sum = 0
    for i in range(100, 1000):
        digit1 = i // 100
        digit2 = (i // 10) % 10
        digit3 = i % 10
        if digit1 % 2 != 0 and digit2 % 2 != 0 and digit3 % 2 != 0:
            total_sum += i
    print(total_sum)

elif n == 4:
    count = 0
    for i in range(100, 1000):
        digit1 = i // 100
        digit2 = (i // 10) % 10
        digit3 = i % 10
        if digit1 > digit2 > digit3:
            count += 1
    print(count)

elif n == 5:
    total_sum = 0
    for i in range(100, 1000):
        digit1 = i // 100
        digit2 = (i // 10) % 10
        digit3 = i % 10
        if i == digit1**3 + digit2**3 + digit3**3:
            total_sum += 1
    print(total_sum)

elif n == 6:
    count = 0
    for i in range(100, 1000):
        digit1 = i // 100
        digit2 = (i // 10) % 10
        digit3 = i % 10
        if digit1 != digit2 and digit2 != digit3 and digit1 != digit3:
            count += 1
    print(count)

else:
    print()