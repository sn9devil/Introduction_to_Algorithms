def insertion_sort(A):
    for i in range(2, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] >key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key


A = [31, 41, 59, 26, 41, 58]
insertion_sort(A)
print(A)