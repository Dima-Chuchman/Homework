n = int(input())
n1 = list(map(int, input().split()))

m = int(input())
m1 = list(map(int, input().split()))

result = []

for i in n1:
    if i not in m1:
        result.append(i)

print(len(result))
for i in result:
    print(i, end="")