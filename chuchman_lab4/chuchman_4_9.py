n = int(input(""))


for _ in range(n):
    x = int(input(""))
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")