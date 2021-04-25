N = int(input())
M = int(input())

ans1 = N * (M % 100 % 10)

ans2 = N * (M % 100 // 10)

ans3 = N * (M // 100)

print(ans1)
print(ans2)
print(ans3)
print(N * M)