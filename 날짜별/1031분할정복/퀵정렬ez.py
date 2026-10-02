# 기준점(피봇)보다 작은값, 큰 값으로 나누기
# 나누다 보면 정렬이 된다
arr = [6, 8, 1, 3, 4, 5, 9, 2, 7]

def quick_sort(target):
    l = len(target)
    if l < 1:
        return target
    # 임의의 값 하나 잡고, 작은애들 큰애들 모으기
    left = [] # 피봇보다 작은
    right = [] # 피봇보다 큰
    # 큰값 작은 값 나누기
    pivot = target[0]
    for i in range(1, l):
        if target[i] < pivot: # 작으면 left
            left.append(target[i])
        else: #크거나 같으면
            right.append(target[i])
    # 근데 왼, 오 둘다 정렬이 안된 상태
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [pivot] + right

print((quick_sort(arr)))
