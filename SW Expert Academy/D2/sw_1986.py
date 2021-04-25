for t in range(1, int(input()) + 1):
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            ans -= i
        else:
            ans += i
    print(f'#{t} {ans}')