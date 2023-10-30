#Обчислити кількість арифметичних операцій
oper = input()
def count_operations(oper):
    operations = '*', '+', '-', '/' '**', '//'
    count = 0

    for i in oper:
        if i in operations:
            count += 1

    return count

oper_count = count_operations(oper)

print(oper_count)