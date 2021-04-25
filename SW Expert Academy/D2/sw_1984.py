# T = int(input())
#
# for t in range(1, T + 1):
#     lst = list(map(int, input().split()))
#     lst.sort()
#     lst.pop(0)
#     lst.pop(-1)
#     ans = 0
#     for i in range(len(lst)):
#         ans += lst[i]
#     result = round(ans/8)
#     print(f'#{t} {result}')

for t in range(1, int(input()) + 1):
    lst = list(map(int, input().split()))

    lst.sort()
    lst.pop(0)
    lst.pop(-1)
    result = 0
    for i in range(len(lst)):
        result += lst[i]

    print(f'#{t} {round(result//8)}')