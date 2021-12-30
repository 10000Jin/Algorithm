
def insetion_sort_recur(A, n):
    if n == 1:
        return A

    else:
        B = insetion_sort_recur(A, n-1)
        for i in range(1, n):
            key = A[n-1]
            j = i-1
            while key < B[j]:
                A[i] = A[i-1]
                A[i+1] = A[i]
            


         



date = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original : ", data)
insertion_sort_recur(date, len(data))
print("Insertion : ", data)
