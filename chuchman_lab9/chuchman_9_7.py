n = int(input())

if n % 2 == 0:
    print("Ok")
else:
    c = list(input())
    for i in range(n):
        counter = 0
        for j in range(n):
            if c[i] == c[j]:
                counter += 1
        if counter % 2 != 0:
            print(c[i])
            break
