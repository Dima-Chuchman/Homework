n = int(input())
m = list(map(int, input().split()))

#for i in m:
   # max_number = max(m)
   # min_number = min(m)
if n == 0:
    print()
else:
    max_number = max(m)
    min_number = min(m)
    
    for q in range(n):
        if m[q] == max_number:
            m[q] = min_number
        elif m[q] == min_number:
            m[q] = max_number

    for num in m:
        print(num, end=" ")