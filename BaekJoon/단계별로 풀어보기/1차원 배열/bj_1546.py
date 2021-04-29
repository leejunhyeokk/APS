N = int(input())
lst = list(map(int, input().split()))
max_score = max(lst)

ans = []

for i in lst:
    ans.append(i/max_score*100)

print(sum(ans)/N)