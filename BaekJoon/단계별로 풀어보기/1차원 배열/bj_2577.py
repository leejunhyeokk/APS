A = int(input())
B = int(input())
C = int(input())
result = list(str(A * B * C))

for i in range(10):
    print(result.count(str(i)))

# A = int(input())
# B = int(input())
# C = int(input())
#
# sumABC = str(A * B * C)
#
# ans = [0] * 9
#
# for i in sumABC:
#     i = int(i)
#     ans[i] += 1
#
# for i in ans:
#     print(str(i))
#
