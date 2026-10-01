import sys
sys.stdin = open("algo1_sample_in.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 1
    for i in range(N // 2 - 1):
        f_arr = arr[i] + arr[N - 1 - i]
        next_arr = arr[i + 1] + arr[N - 2 - i]
        if f_arr >= next_arr:
            cnt = 0
    print(f'#{tc} {cnt}')

