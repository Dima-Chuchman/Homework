A, B = map(int, input().split())

def nsk_nsd(A, B):
    while B:
        A, B = B, A % B
    return A

count = 2

for P in range(1, A + 1):
    Q = A // nsk_nsd(A, P)
    R = (A * B) // nsk_nsd(A, P)
    if P * Q == A:
        if P * R == A * B:
            count += 1

print(count)
