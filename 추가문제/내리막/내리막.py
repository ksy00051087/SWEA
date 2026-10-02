import sys
sys.stdin = open("sample_in.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 1
    cnt2 = 1
    for i in range(N - 1):
        if len(arr) == 1:
            break
        if arr[i] <= arr[i + 1]:
            cnt = 0
    print(f'#{tc} {cnt}')
