# for t in range(1, int(input()) + 1):
#     N = input()
#     for i in range(len(N)//2):
#         if N[i] != N[-i-1]:
#             ans = 0
#     print(f'#{t} {ans}')

for t in range(1, int(input()) + 1):
    N = input()
    ans = 1
    if N != N[::-1]:
        ans = 0
    print(f'#{t} {ans}')