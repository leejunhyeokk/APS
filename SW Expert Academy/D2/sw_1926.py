# T = int(input())
#
# for i in range(1, T + 1):
#
#     if i % 3 == 0 and i < 10:
#         print('-', end=" ")
#     elif (i % 10 == 3 and i % 3 == 0) or (i % 10 == 6 and i % 3 == 0) or (i % 10 == 9 and i % 3 == 0):
#         print('--', end = " ")
#
#     elif (i % 10 == 3 or i % 10 == 6 or i % 10 == 9) or (i // 10 == 3 or i // 10 == 6 or i // 10 == 9):
#         print('-', end = " ")
#     else:
#         print(i, end = " ")

T = int(input())

for i in range(1, T + 1):
    i = str(i)
    ans = i.count('3') + i.count('6') + i.count('9')

    if ans >= 1:
        print('-' * ans, end = " ")
    else:
        print(i, end = " ")