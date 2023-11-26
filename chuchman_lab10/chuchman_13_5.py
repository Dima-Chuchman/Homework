#Дано текстовий файл, компоненти якого є цілими числами. Скласти підпрограми для обчислення:
#a)    кількості парних чисел серед компонент;
#b)    кількості квадратів непарних чисел серед компонент;
#c)    різниці між найбільшим парним і найменшим непарним числами з компонент;
#d)    кількості компонент у найдовшій зростаючій послідовності компонент файла.


with open('text_13_5', 'r') as file:
    lines = file.readlines()
    components = []

    for line in lines:
        numbers = line.split()

        for number in numbers:
            try:
                num = int(number)
                components.append(num)
            except ValueError:
                pass


#A)-------------------------------->

def even_numbers(components):
    suma = 0
    for num in components:
        if num % 2 == 0:
            suma += num
    return suma

suma = even_numbers(components)
print(f"Сума парних чисел: {suma}")


#B)-------------------------------->

def odd_numbers(components):
    odd_count = 0
    for odd in components:
        if odd % 2 != 0 and odd >= 0 and int(odd ** 0.5 ) ** 2 == odd:
            odd_count += 1
    return odd_count

odd_numbers_count = odd_numbers(components)
print(f"Кількість квадратів непарних чисел: {odd_numbers_count}")


#C)-------------------------------->


def difference(components):
    even = []
    for num in components:
        if num % 2 == 0:
            even.append(num)

    odd = []
    for num in components:
        if num % 2 != 0:
            odd.append(num)
    if even:
        max_even = max(even)
    else:
        max_even = None

    if odd:
        min_odd = min(odd)
    else:
        min_odd = None

    if max_even is not None and min_odd is not None:
        gap = max_even - min_odd
    else:
        gap = None

    return gap

result = difference(components)

print(f"Різниця між найбільшим парним і найменшим непарним числами: {result}")


#D)-------------------------------->

def sequence(components):
    longest_sequence = 1
    current_sequence = 1

    for i in range(1, len(components)):
        if components[i] > components[i - 1]:
            current_sequence += 1
        else:
            if current_sequence > longest_sequence:
                longest_sequence = current_sequence
            current_sequence = 1

    return max(longest_sequence, current_sequence)

result_sequence = sequence(components)
print(f"Кількість компонент у найдовшій зростаючій послідовності: {result_sequence}")