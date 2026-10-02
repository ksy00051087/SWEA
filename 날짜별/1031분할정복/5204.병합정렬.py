import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    def merge_sort(s, e):
        global cnt

        # 원소가 하나면 더 이상 나눌 필요 없음
        if s == e:
            return

        # arr 길이가 홀수일떄 왼쪽 보다 오른쪽길이가 길어야 함
        mid = s + (e - s + 1) // 2 - 1
        # 왼쪽 정렬
        merge_sort(s, mid)

        # 오른쪽 정렬
        merge_sort(mid + 1, e)

        # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 크면 카운트
        if arr[mid] > arr[e]:
            cnt += 1

        # 병합
        sorted_arr = []

        i = s
        j = mid + 1

        while i <= mid and j <= e:

            if arr[i] < arr[j]:
                sorted_arr.append(arr[i])
                i += 1

            else:
                sorted_arr.append(arr[j])
                j += 1

        # 왼쪽에 남은 값 붙이기
        while i <= mid:
            sorted_arr.append(arr[i])
            i += 1

        # 오른쪽에 남은 값 붙이기
        while j <= e:
            sorted_arr.append(arr[j])
            j += 1

        # 원본 배열에 다시 저장
        b = 0

        for a in range(s, e + 1):
            arr[a] = sorted_arr[b]
            b += 1

    merge_sort(0, N - 1)

    print(f'#{tc} {arr[N // 2]} {cnt}')