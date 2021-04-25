N, M = map(int, input().split())

if M >= 45:
    print(N, M-45)

else:
    if N == 0:
        print(23, M+15)
    elif N == 1:
        print(0, M+15)
    else:
        print(N-1, M+15)