for t in range(10):
    T = int(input())
    data = list(map(int, input().split()))
    result = 0
    for i in range(2, T-2):
        around = max([data[i - 2], data[i - 1], data[i + 1], data[i + 2]])
        if (data[i] > around):
            result += data[i] - around
    print('#{} {}'.format(t, result))
