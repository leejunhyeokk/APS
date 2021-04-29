arr = []

max_value = 0
ans = 0

for i in range(1, 10):
    input_value = int(input())
    if input_value > max_value:
        max_value = input_value
        ans = i

print(max_value)
print(ans)