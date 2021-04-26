for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [0] * 101
    score = list(map(int, input().split()))
    max_num = ans = 0
    for i in score:
        arr[i] += 1

    for i in range(0, 101):
        if max_num <= arr[i]:
            max_num = arr[i]
            ans = i

    print(f'#{t} {ans}')

