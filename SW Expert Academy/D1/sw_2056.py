md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for t in range(1, T + 1):
    N = input()
    year = N[:4]
    month = int(N[4:6])
    day = int(N[6:])
    ans = -1

    if 0 < month < 13 and 0 < day <= md[month - 1]:
        ans = year + '/' + N[4:6] + '/' + N[6:]

    print(f'#{t} {ans}')