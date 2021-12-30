# 5장 연습문제 13번
import time

def partition(A, left, right):                              # Hoare 방법
    low = left + 1
    high = right

    mid = (left + right) // 2                               # 중간값
    mid_pos = three_sort(A, left, mid, right)               # 양 옆과 중간값을 정렬
    A[left], A[mid_pos] = A[mid_pos], A[left]               # 정렬후 중간값을 맨 왼쪽과 교환
    print("three_sort 후 => ", A)                           # 3가지 수 정렬한 결과 출력 

    pivot = A[left]                                         # 맨 왼쪽(중간값)을 피벗으로
    while(low <= high):
        while low <= right and A[low] <= pivot : low += 1   # low가 피벗보다 클 때까지
        while high >= left and A[high] > pivot : high -= 1  # high가 피봇보다 작을 때까지

        if low < high :                                     # low와 high 교환
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]                     # 역전되면 피벗과 high교환
    print("partition 후  => ", A)                            # Hoare 종료후 결과 출력
    return high


def three_sort(A, left, mid, right):                        # 맨 왼쪽, 오른쪽과 중간값 정렬  
    if A[left] > A[mid]:                                    # 왼쪽이 중간보다 크면
        A[left], A[mid] = A[mid], A[left]                   # 교환
    if A[mid] > A[right]:                                   # 중간이 오른쪽보다 크면    
        A[mid], A[right] = A[right], A[mid]                 # 교환
    if A[left] > A[mid]:                                    # 중간과 오른쪽이 바뀔수도 있으니 다시 왼쪽과 중간 비교
        A[left], A[mid] = A[mid], A[left]                   # 교환

    return mid                                              # 정렬후 중간값 반환


def median_quick_sort(A, left, right):                      # 퀵 정렬
    if left < right:                                        # 정렬 범위가 2개 이상인 경우
        pos = partition(A, left, right)                     # 좌우 분할 
        median_quick_sort(A, left, pos-1)                   # 왼쪽 부분리스트 퀵 정렬 
        median_quick_sort(A, pos+1, right)                  # 오른쪽 부분리스트 퀵 정렬
    

#arr = [8, 1, 3, 6, 2, 7, 9, 5, 4, 0]
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n = len(arr)
print("원래 array    => ", arr)
print()
start = time.time()
print(median_quick_sort(arr, 0, n-1))
end = time.time()
print("실행 시간 : ", end-start)
