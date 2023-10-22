n = int(input())
m = list(map(float, input().split()))

posnumber = []

for i in m:
    if i > 0:
        posnumber.append(i)


if len(posnumber) <= 0:
    print("Not Found")
else:
    summa = sum(posnumber) / len(posnumber)
    print("{:.2f}".format(summa))