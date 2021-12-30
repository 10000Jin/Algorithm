
def merge(arr, left, mid, right):
    k = left
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            sorted[k] = arr[i]
            i, k = i+1, k+1
        else:
            sorted[k] = arr[j]
            j, k = j+1, k+1

    if i > mid:
        sorted[k:k+right-j+1] = arr[j:right+1]
    else:
        sorted[k:k+mid-i+1] = arr[i:mid+1]

    arr[left:right+1] = sorted[left:right+1]

def merge_sort(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
