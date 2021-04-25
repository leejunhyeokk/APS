for t in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]
    ans = 0
    maxValue = lst[0]

    for i in range(1, N):
        if maxValue > lst[i]:
            ans += maxValue - lst[i]
        else:
            maxValue = lst[i]

    print(f'#{t} {ans}')