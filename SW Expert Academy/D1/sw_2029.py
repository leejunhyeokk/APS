T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    ans1, ans2 = N // M, N % M

    print(f'#{t} {ans1} {ans2}')