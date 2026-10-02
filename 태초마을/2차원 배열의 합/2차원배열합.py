import sys
sys.stdin = open("input.txt", "r")
sum_val = 0
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        sum_val += arr[i][j]
print(sum_val)