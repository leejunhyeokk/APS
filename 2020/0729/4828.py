def max_result(x):
    max_m = x[0]
    for i in range(1, len(x)):
        if x[i] > max_m:
            max_m = x[i]
    return max_m

def min_result(x):
    min_x = x[0]
    for i in range(1,len(x)):
        if x[i] < min_x:
            min_x = x[i]
    return min_x

T = int(input())
for t in range(1, T+1):
    z = int(input())
    x = list(map(int, input().split()))
    result = max_result(x) - min_result(x)

    print(f'#{t} {result}')
