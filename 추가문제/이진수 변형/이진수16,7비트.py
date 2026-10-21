import sys
sys.stdin = open("sample_input2.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, s = input().split()
    N = int(N)
    bits = f'{int(s, 16):0{N*4}b}'                        # 원래 문제 그대로
    bits = bits.ljust((len(bits) + 6) // 7 * 7, '0')     # 7의 배수까지 뒤에 0
    print(f'#{tc}', *[int(bits[i:i+7], 2) for i in range(0, len(bits), 7)])