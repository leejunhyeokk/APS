T = int(input())

for t in range(1, T+1):
    z = input()
    num = input()
    data = [0]*10
    for i in num:
        data[int(i)] += 1

    max_value = 0
    counter = 0

    for i in range(10):
        if counter <= data[i]:
            counter = data[i]
            max_value = i

    print(f'#{t} {max_value} {counter}')    