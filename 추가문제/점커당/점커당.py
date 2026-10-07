import sys
sys.stdin = open("carrot_sample_in.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_cnt = 1
    cnt = 1
    for i in range(N - 1):
        if arr[i] < arr[i + 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= max_cnt:
            max_cnt = cnt
    print(f"#{tc} {max_cnt}")


    # def dfs(r, c):
    #     if arr[r][c] == 'L':
    #         arr[r][c] = 1
    #         for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    #             nr = r + dr
    #             nc = c + dc
    #             if 0 <= nr < N and 0 <= nc < M:
    #                 dfs(nr, nc)
    #
    #
    # T = int(input())
    # for tc in range(1, T + 1):
    #     cnt = 0
    #     N, M = map(int, input().split())
    #     arr = [list(input()) for _ in range(N)]
    #     for i in range(N):
    #         for j in range(M):
    #             if arr[i][j] == 'L':
    #                 cnt += 1
    #                 dfs(i, j)
    #     print(f'#{tc} {cnt}')