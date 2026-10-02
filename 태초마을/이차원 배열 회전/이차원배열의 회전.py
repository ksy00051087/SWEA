import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(M):
    for j in range(N - 1, -1, -1):
        print(arr[j][i], end=' ')
    print()
#
# 20
# 10
# 00
#
# 21
# 11
# 01
#
# 22
# 12
# 02
#
# 23
# 13
# 03