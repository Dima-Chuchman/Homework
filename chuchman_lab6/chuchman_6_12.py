password = input().strip()

k = int(input())

text = ''

for i in password:
    if 'A' <= i <= 'Z':
        shift = chr(((ord(i) - ord('A') - k) % 26) + ord('A'))
    else:
        shift = i

    text += shift

print(text)