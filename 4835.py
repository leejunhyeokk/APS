T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    lst = []

    for i in range((N+M)-1):
        count = 0
        for j in range(i, i+M):
            count += num[j]
        lst.append(count)

    max_value = lst[0]
    for k in range(1, len(lst)):
        if max_value <= lst[k]:
            max_value = lst[k]

    min_value = lst[0]
    for k in range(1, len(lst)):
        if min_value >= lst[k]:
            min_value = lst[k]

    print(f'#{t} {max_value-min_value}')
