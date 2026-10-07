import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        run = 0
        for j in range(N):
            if arr[i][j] == 1:
                run += 1
            else:
                if run == M:
                    cnt += 1
                run = 0
        if run == M:
            cnt += 1
    for j in range(N):
        run = 0
        for i in range(N):
            if arr[i][j] == 1:
                run += 1
            else:
                if run == M:
                    cnt += 1
                run = 0
        if run == M:
            cnt += 1

    print(f'#{tc} {cnt}')