import sys
sys.stdin = open("algo2_sample_in.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for r in range(N - 2):
        for c in range(N - 2):
            val = 0
            for i in range(3):
                for j in range(3):
                    if arr[r + i][c + j] == 1:
                        val += 1
            if val >= 7:
                cnt += 1
    print(f'#{tc} {cnt}')