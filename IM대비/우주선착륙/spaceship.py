import sys
sys.stdin = open("input2.txt", "r")

def low(r, c):
    val = 0
    for dr, dc in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M and