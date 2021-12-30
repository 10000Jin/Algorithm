import time

def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]
    while(low <= high):
        while low <= right and A[low] <= pivot : low += 1
        while high >= left and A[high] > pivot : high -= 1

        if low < high :
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high

def quick_sort(A, left, right):
    if left < right:
        mid = partition(A, left, right)
        quick_sort(A, left, mid-1)
        quick_sort(A, mid+1, right)

arr = [8, 1, 3, 6, 2, 7, 9, 5, 4, 0]
#arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
print("정렬전 : ", arr)

start = time.time()
quick_sort(arr, 0, n-1)
print("정렬후 : ", arr)
end = time.time()

print("실행 시간 : ", (end-start))