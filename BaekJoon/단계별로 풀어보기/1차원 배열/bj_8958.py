for t in range(1, int(input()) + 1):
    N = list(str(input()))
    ans = 0
    score = 0
    for i in N:
        if i == 'O':
            score += 1
            ans += score
        else:
            score = 0

    print(ans)