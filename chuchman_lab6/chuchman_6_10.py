n = input()

doubled_letters =''
for i in n:
    if i.islower():
        doubled_letters += i * 2
    else:
        doubled_letters += i

print(doubled_letters)