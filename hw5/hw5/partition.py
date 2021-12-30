
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

def quick(A, left, right, k):
    pos = partition(A, left, right)

    if(pos+1 == left+k):
        return A[pos]
    elif(pos+1 > left +k):
        return quick(A, left, pos-1, k)
    else:
        return quick(A, pos+1, right, k-(pos+1-left))

arr = [12, 3, 5, 7, 4, 19, 26, 23, 15]
n = len(arr)
print(quick(arr, 0, n-1, 3))
print(quick(arr, 0, n-1, 6))