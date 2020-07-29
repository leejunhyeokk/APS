T = int(input())

for t in range(1, T + 1):
    lst = list(map(int, input().split()))

    max_value = 0
    for i in lst:
        if i > max_value:
            max_value = i

    print(f'#{t} {max_value}')