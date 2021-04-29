N = int(input())

arr = list(map(int, input().split()))

max_value = min_value = arr[0]

for i in range(len(arr)):
    if max_value < arr[i]:
        max_value = arr[i]
    if min_value > arr[i]:
        min_value = arr[i]

print(min_value, max_value)


