n, k = map(int, input().split())
m = input().strip()

def convert(num, base):
    if num == 0:
        return ''
    result = ''
    digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while num > 0:
        result = digit[num % base] + result
        num = num // base

    return result

number = int(m, n)
convert_number = convert(number, k)
print(convert_number)