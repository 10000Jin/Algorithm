#5장 연습문제 9번

def count_inversion(arr):                           # 억지기법 활용
    n = len(arr)
    inv_count = 0                                   # 역전 개수
    for i in range(n):                              # 이중 반복문을 돌며 한 수와 그 다음 수들
        for j in range(i+1, n):                     # 간의 역전 관계 확인
            if(arr[i] > arr[j]):                    # 앞의 수가 더 크면
                inv_count += 1                      # 역전 개수 1증가
    return inv_count                                # 역전 개수 반환



def merge_sort(arr, tmp, left, right):              # 병합 정렬
    inv_count = 0                                   # 역전 개수 0초기화
    if left < right:                                # 항목이 2개 이상일 때만
        mid = (left + right) // 2                   # 리스트를 분할할 위치
        inv_count += merge_sort(arr, tmp, left, mid)        # 왼쪽 부분 리스트 정렬
        inv_count += merge_sort(arr, tmp, mid+1, right)     # 오른쪽 부분 리스트 정렬
        inv_count += merge(arr, tmp, left, mid, right)      # 순환을 거치며 merge함수에서 병합하며
                                                            # 생긴 역전 개수를 모두 더함
    return inv_count                                # 역전 개수 반환


def merge(arr, tmp, left, mid, right):              # 병합
    k = left                                        # 임시 리스트의 인덱스
    i = left                                        # 왼쪽 리스트의 인덱스   
    j = mid + 1                                     # 오른쪽 리스트의 인덱스
    inv_count = 0                                   # 역전 개수 0초기화

    while i <= mid and j <= right:                  # i, j가 각 부분 리스트를 넘지 않으면
        if arr[i] < arr[j]:                         # 오른쪽(부분 리스트)이 왼쪽보다 크면
            tmp[k] = arr[i]                         # 작은 쪽(왼쪽)을 임시 리스트에 저장
            i, k = i+1, k+1                         # 작은 쪽과 임시리스트의 인덱스 1증가
       
        else:                                       # 왼쪽이 오른쪽 이상이면
            tmp[k] = arr[j]                         # 작은 쪽(오른쪽)을 임시리스트에 저장하고 이때 역전인 상황
            inv_count += (mid - i + 1)              # 각 부분리스트는 정렬돼있음으로 왼쪽 부분리스트에서 
            j, k = j+1, k+1                         # i이후의 수는 j보다 큼. 그만큼 역전이 생긴 것임
                                                    # 작은 쪽과 임시리스트의 인덱스 1증가

    if i > mid:                                     # 한쪽 리스트가 다 끝나면 나머지 리스트의 항목 일괄 복사
        tmp[k:k+right-j+1] = arr[j:right+1]         # 왼쪽이 먼저 끝났으면 오른쪽의 나머지 항목을 복사
    else:                                           # 오른쪽이 먼저 끝났으면
        tmp[k:k+mid-i+1] = arr[i:mid+1]             # 왼쪽의 나머지 항목을 복사

    arr[left:right+1] = tmp[left:right+1]           # 임시리스트를 arr에 다시 복사
    
    return inv_count                                # 역전 개수 반환


def count_inversion_dc(arr):                        # 병합정렬 역전개수 구하기
    n = len(arr)                                    
    tmp = [0]*n                                     # arr의 크기만큼 임시리스트 만듬
    return merge_sort(arr, tmp, 0, n-1)             # 병합 정렬 호출하고 그 값 반환


#arr = [1, 20, 6, 4, 5]
arr = [1, 20, 6, 4, 3, 9, 8, 5]
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
print("역전 개수(억지기법) : ", count_inversion(arr))
print("역전 개수(분할정복) : ", count_inversion_dc(arr))