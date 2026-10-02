import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_val = 0
sum_val = 0
for i in range(N - 2):
    sum_val = arr[i] + arr[i+1] + arr[i+2]
    if sum_val > max_val:
        max_val = sum_val
print(max_val)

