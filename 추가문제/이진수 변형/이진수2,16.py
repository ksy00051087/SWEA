import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, s = input().split()
    N = int()
    n = int(s, 2)
    L = (N + 3) // 4
    print(f'#{tc} {n:0{L}X}')