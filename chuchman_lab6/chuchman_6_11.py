password = input()

criteria = 0
operations = "!\"#$%&'()*+"

if any(i.islower() for i in password):
    criteria += 1

if any(i.isupper() for i in password):
    criteria += 1

if any(i.isdigit() for i in password):
    criteria += 1

if any(i in operations for i in password):
    criteria += 1

if len(password) >= 8:
    criteria += 1

print(criteria)