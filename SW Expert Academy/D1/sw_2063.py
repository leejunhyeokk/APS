T = int(input())

lst = list(map(int, input().split()))

lst.sort()

print(lst[T//2])