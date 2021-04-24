T = int(input())

ans = 0

for i in range(4):
    x = T % 10
    ans += x
    T = T//10

print(ans)