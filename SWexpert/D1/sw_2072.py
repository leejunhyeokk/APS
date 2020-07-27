T = int(input())

for t in range(1, T + 1):
    lst = list(map(int, input().split()))

    ans = 0
    for i in lst:
        if i % 2 != 0:
            ans += i

    print(f'#{t} {ans}')
