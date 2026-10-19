import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = 0
    sum_val = 0
    for i in range(N - 1, -1, -1):
        if arr[i] > max_val:
            max_val = arr[i]
        else:
            sum_val += max_val - arr[i]
    print(f'#{tc} {sum_val}')
