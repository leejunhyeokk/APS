N = check = int(input())
cnt = 0
while True:
    temp = N // 10 + N % 10
    new = int(str(N % 10) + str(temp % 10))
    cnt += 1
    N = new
    if new == check:
        break
print(cnt)