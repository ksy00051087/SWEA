arr = [6, 8, 1, 3, 4, 5, 9, 2, 7]
N = len(arr)
def partition(s, e):
    # i = s, j = e
    # i 랑 j 가 찾으러 다닌다
    # i는 자기보다 큰값을 찾아서
    # j 는 자기보다 작은 값을 찾아서
    # 서로 스위칭
    # 그래서 최대한 값을 쪼이다가 피봇이랑 i랑 위치 바꿈
    # 이 자식은 피봇을 기준으로 작으값과 큰값을 분리하고
    # 피벗 위치 반환
    pivot = arr[s]
    # 큰값을 찾을 변수
    i = s + 1
    # 작은 값을 찾을 변수
    j = e

    while i <= j:
        # i를 증가 시키면서 pivot 보다 큰 값 찾기
        while i <= j and arr[i] <= pivot:
            i += 1
        # j를 감소시키면서 pivot 보다 작은값 찾기
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            # 큰 값은 뒤로보내고 작은 값은 앞으로 보내기
            arr[i], arr[j] = arr[j], arr[i]
    # 피봇 제자리 찾아주기
    arr[s], arr[j] = arr[j], arr[s]
    return j

def quick_sort(s, e):
    if s >= e:
        return # 값이 역전 되면 그만해라
    # 1. 피벗보다 큰 값과 작은값으로 나누기 : partition
    pivot = partition(s, e) # 피벗 위치 반환
    quick_sort(s, pivot - 1)
    quick_sort(pivot + 1, e)

quick_sort(0, N - 1)
print(arr)

