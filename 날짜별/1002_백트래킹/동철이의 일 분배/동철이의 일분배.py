import sys
sys.stdin = open("input.txt", "r")

def solve(idx, rate):
    global max_rate

    if rate <= max_rate:
        return

    if idx == N:
        max_rate = rate
        return

    for i in range(N):
        if not check[i]:
            check[i] = 1
            solve(idx + 1, rate * arr[idx][i])
            check[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100
    max_rate = 0
    check = [0] * N
    solve(0, 1)
    print(f'#{tc} {max_rate * 100:.6f}')

