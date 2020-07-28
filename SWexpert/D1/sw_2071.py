T = int(input())

for t in range(1, T + 1):
    lst = list(map(int, input().split()))

    ans = 0
    for i in lst:
        ans += i

    print(f'#{t} {round(ans/len(lst))}')