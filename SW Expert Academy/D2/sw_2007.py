T = int(input())

for t in range(1, T + 1):
    N = input()

    for i in range(1, 10):
        if N[:i] == N[i: i * 2]:
            print(f'#{t} {i}')
            break