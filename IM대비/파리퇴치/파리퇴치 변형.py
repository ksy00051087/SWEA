import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            fly = 0

            for i in range(M):
                for j in range(M):
                    if arr[i][j] >= 10:
                        fly += 1
            if fly >= M:
                max_fly += 1

    print(f"#{tc} {max_fly}")
