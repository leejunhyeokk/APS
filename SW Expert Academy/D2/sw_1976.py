for t in range(1, int(input()) + 1):
    time = list(map(int, input().split()))
    hour, minute = [], []
    for i in range(len(time)):
        if i % 2 != 0:
            minute.append(time[i])
        else:
            hour.append(time[i])
    hour, minute = sum(hour), sum(minute)

    if minute > 60:
        hour = hour + 1
        minute = minute - 60
    if hour > 12:
        hour = hour - 12

    print(f'#{t} {hour} {minute}')