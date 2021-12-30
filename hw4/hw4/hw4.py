
def Lomuto_Partition(arr, low, high):
    p = arr[high]                                       # 제일 마지막 값을 피벗으로 사용
    i = low - 1                                         # 첫번째 값의 번지수 - 1을 i에 저장

    for j in range(low, high):                          # j가 첫번째 값부터 피벗까지 돌면서
        if arr[j] <= p:                                 # 만약 j번지의 값이 피벗보다 작거나 같으면
            i += 1                                      # i의 값 1증가
            arr[i], arr[j] = arr[j], arr[i]             # 그리고 i번지 값과 j번지 값 교환
        j += 1                                          # j번지 값이 피벗보다 크다면 j만 1증가

    arr[i+1], arr[high] = arr[high], arr[i+1]           # j가 피벗까지 도달해 반복이 종료되면 i+1번지 값과 피벗 교환
    return i+1                                          # 피벗이 저장되어있는 번지수 반환



def quick_select_iter(a, left, right, k):
    O_left = left                                       # 원래의 left값 저장

    while left <= right:                                # left값이 right값보다 커지면 반복 종료
        pos = Lomuto_Partition(a, left, right)          # lomuto_Partition함수 호출해 피벗의 번지수 pos에 저장
        
        if pos + 1 == O_left + k:                       # pos+1이 원래의 left+k 값과 같다면
            return a[pos]                               # 더 정렬할 필요없이 피벗이 찾는 수 이므로 반환
        elif pos + 1 > O_left + k:                      # 왼쪽 부분 리스트에 답이 존재하므로
            right = pos - 1                             # 새로운 피벗을 기존 피벗 하나 앞의 항목으로 설정
        else:                                           # 오른쪽 부분 리스트에 답이 존재하므로
            left = pos + 1                              # left값을 피벗 다음 항목으로 설정하고
            k = k - (pos + 1 - left)                    # k값을 k에서 피벗의 번지수+1에 left값을 빼서
                                                        # 오른쪽 부분 리스트에서의 새로운 k설정
    return -1                                          


arr = [10, 4, 5, 8, 11, 6, 26]
n = len(arr)
k = 5
print()
print("%d-th smallest element is %d" % (k, quick_select_iter(arr, 0, n-1, k)))