T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(i + 1):
            arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]
            arr[0][0] = 1

    print(f'#{t}')
    for i in arr:
        for j in i:
            if j:
                print(j, end = " ")
        print()