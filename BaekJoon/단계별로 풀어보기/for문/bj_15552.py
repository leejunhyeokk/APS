import sys

T = int(sys.stdin.readline())

for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(N + M)