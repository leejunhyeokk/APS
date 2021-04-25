for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            ans = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    ans += arr[x][y]
            result.append(ans)

    print(f'#{t} {max(result)}')