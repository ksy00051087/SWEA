import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(3):
    sen = str(input())
    print(sen[::-1])
