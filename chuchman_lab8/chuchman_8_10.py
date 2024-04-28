#8.10
#За заданим натуральним числом n вивести усі перестановки
# з цілих чисел від 1 до n у лексикографічному порядку.

def generate_permutations(n):
    def next_permutation(arr):
        k = -1
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                k = i

        if k == -1:
            return False

        l = -1
        for i in range(n):
            if arr[k] < arr[i]:
                l = i

        arr[k], arr[l] = arr[l], arr[k]

        arr[k+1:] = arr[k+1:][::-1]

        return True

    numbers = list(range(1, n + 1))

    print(" ".join(map(str, numbers)))

    while next_permutation(numbers):
        print(" ".join(map(str, numbers)))

n = int(input())
generate_permutations(n)