#Треба знайти НСК-----------------------------
n = int(input())

def least(n):
    nsk = 1
    for i in range(2, n + 1):
        nsk = (nsk * i) // gcd(nsk, i)
    return nsk

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

result = least(n)
print(result)

