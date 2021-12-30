def Hoare_partition(A, left, right):
    low = left+1
    high = right
    pivot=A[left]
    while(low<=high):           #low 와 high가 역전되지 않는 한 계속 반복
        while low <=right and A[low] < pivot : low += 1     #low가 high보다 작거나 같으면서 A[low]의 값이 pivot보다 작으면 low를 오른쪽으로 계속 움직임
        while low >=right and A[high] > pivot : high -= 1   #high가 low와 역전되지 않는 동안 A[high]의 값이 pivot값보다 크면 high를 왼쪽으로 계속 움직임

        if low < high:                  #이때 만약 low가 high 보다 작으면
            A[low],A[high] = A[high],A[low]     #low와 high의 값을 바꿈.

    A[left], A[high] = A[high], A[left] #마지막으로 high와 pivot 값을 교체
    return high

def Lomuto_partition(A, low, high):
    pivot = A[high]
    i = low -1 #i >> A의 low보다 한칸 왼쪽 인덱스

    for j in range(low, high):          #j는 인덱스 0~high(n-1)-1 까지 이동
        if A[j]<=pivot:                  # A[j]가 피벗보다 작으면
            i += 1                      # i를 오른쪽으로 한칸 이동
            A[i], A[j] = A[j], A[i]     # 그리고 i를 j와 교체
        j +=1
    A[i+1], A[high] = A[high], A[i+1]   # A[i+1]과 A[high]를 교체 >> 피벗 아님
    return i+1          #한번 로무토 분할을 한 후 피벗의 위치는 i 다음임. 즉 i+1


def quick_select(A, left, right, k):
    x = left
    pos = Lomuto_partition(A, left, right)
    while(pos+1 != x+k):
      
      
        pos = Lomuto_partition(A, left, right)

        if(pos+1<x+k):         #피벗보다 찾고자하는 수가 더 크면 >> 오른쪽 리스트에서 탐색
            left = pos+1
            k = k-(pos+1)+left
        else:
            right = pos-1
    return A[pos]           #k : 몇번째로 작은 수를 찾을지


A = [3,1,4,6,5,2,9,8,7]
n = len(A)
print('초기 리스트 : ', A)
print('Lomuto 정렬 1회 후 피벗의 인덱스 : ', Lomuto_partition(A, 0, n-1))
#print('Lomuto 정렬 후 : ', quick_sort(A, 0, n-1))
print(quick_select(A, 0, n-1, 3))
#quick_sort(0, n-1)
#for i in range(0, n):
#    print(A[i], end = ' ')