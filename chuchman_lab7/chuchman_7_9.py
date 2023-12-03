k = int(input())

num = 2
count = 0

if num > 10**6:
    print(-1)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 1/2) + 1):
        if num % i == 0:
            return False
    return True

while num < 10**6:
    if is_prime(num):
        reverse_num = int(str(num)[::-1])
        if num != reverse_num and is_prime(reverse_num):
            count = count + 1
            if count == k:
                print(num)
                break
    num = num + 1

