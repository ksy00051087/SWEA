import sys
sys.stdin = open("algo1_sample_in.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 1
    if len(arr) % 2 == 0:
        for i in range(N // 2):
            if arr[i] + arr[N - 1 - i] >= arr[i] + arr[N - 2 - i]:
                cnt = 0
    else:
        for i in range(N // 2 - 1):
            if arr[i] + arr[N - 1 - i] >= arr[i] + arr[N - 2 - i]:
                cnt = 0

    print(f"#{tc} {cnt}")
