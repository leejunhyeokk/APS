# for t in range(1, int(input()) + 1):
#     N = str(input())
#     ans = 1
#     for i in range(len(N) // 2):
#         print(N[i])
#         if N[i] != N[-i-1]:
#             ans = 0
#
#     print(ans)

for t in range(1, int(input()) + 1):
    N = input()
    ans = 1
    for i in range(len(N)//2):
        if N[i] != N[-i-1]:
            ans = 0
            break
    print(f'#{t} {ans}')