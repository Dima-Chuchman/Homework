a = set(input())
b = set(input())

difference = b - a

if not difference:
    print("Ok")
else:
    print("No")
