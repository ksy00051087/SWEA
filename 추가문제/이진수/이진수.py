import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, s = input().split()
    N = int(N)
    n = int(s, 16)
    print(f'#{tc} {n:0{N*4}b}')