T = int(input())

for t in range(1, T + 1):
    N, M = input().split()
    ans = ''
    if N < M:
        ans = '<'

    elif N == M:
        ans = '='

    else:
        ans = '>'

    print(f'#{t} {ans}')