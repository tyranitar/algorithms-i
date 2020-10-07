def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Only works for numerical entries.
def swap_in_place(A, i, j):
    if A[i] != A[j]:
        A[i] = A[i] - A[j]
        A[j] += A[i]
        A[i] = A[j] - A[i]