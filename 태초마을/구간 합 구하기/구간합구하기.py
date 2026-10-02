import sys
sys.stdin = open("input.txt", "r")


N, M = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(M):
    sum_val = 0
    r, c = map(int, input().split())
    for i in range(r - 1, c):
        sum_val += arr[i]
    print(sum_val)

