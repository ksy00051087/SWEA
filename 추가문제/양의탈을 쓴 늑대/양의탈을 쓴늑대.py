import sys
sys.stdin = open("algo2_sample_in.txt", "r")

def dfs(r, c):
    arr[r][c] = 0
    cnt = 1
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0),
                   (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
            cnt += dfs(nr, nc)
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    wolf = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if dfs(i, j) >= 5:
                    wolf += 1

    print(f"#{tc} {wolf}")
