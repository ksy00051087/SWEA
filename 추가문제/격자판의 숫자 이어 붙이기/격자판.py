import sys
sys.stdin = open("sample_input.txt", "r")

def dfs(r, c, num):
    if len(num) == 7:
        ans.add(num)
        return
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, num + arr[nr][nc])
T = int(input())
for tc in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])
    print(f'#{tc} {len(ans)}')