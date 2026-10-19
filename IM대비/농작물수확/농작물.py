import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    a = N // 2
    sum_val = 0
    for i in range(N):
        for j in range(N):
            if abs(a - i) + abs(a - j) <= a:
                sum_val += arr[i][j]
    print(f'#{tc} {sum_val}')



