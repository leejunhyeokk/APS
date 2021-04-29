for t in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:])/arr[0]
    count = 0
    for i in arr[1:]:
        if i > avg:
            count += 1
    ans = count/arr[0] * 100

    print(str('%.3f' % round(ans, 3)) + '%')