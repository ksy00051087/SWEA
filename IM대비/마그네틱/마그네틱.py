import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        red = False
        for j in range(N):
            num = arr[j][i]
            if num == 1:
                red = True
            elif num == 2:
                if red:
                    cnt += 1
                    red = False
    print(f'#{tc} {cnt}')