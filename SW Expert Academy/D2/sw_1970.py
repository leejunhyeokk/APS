for t in range(1, int(input()) + 1):
    money = int(input())
    pay = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    ans = [0] * 8
    for i in range(len(pay)):
        if money != 0:
            ans[i] = money // pay[i]
            money = money % pay[i]
    print(f'#{t}')
    print(f'{ans}')