#8.9.З десяткової у тринадцяткову
#Задано число n у десятковій системі числення. Переведіть це число у тринадцяткову систему числення.

n = int(input())

def base13(n):
    if n == 0:
        return 0

    digits = "0123456789ABC"
    number = " "

    while n > 0:
        ostacha = n % 13
        number = digits[ostacha] + number
        n = n // 13

    return number
result = base13(n)

print(result)