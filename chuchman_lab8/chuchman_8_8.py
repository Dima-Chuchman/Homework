n = int(input())

binary = bin(n)[2:]

area = []

for digit in binary:
    if digit == '1':
        area.append("SX")
    else:
        area.append("S")

result = ''.join(area)
result = result.replace("SX", "", 1)

print(result)