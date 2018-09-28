import sys
sys.setrecursionlimit(1000000)
#
# def merge(A,p,q,r):
#     n1 = q-p+1
#     n2 = r-q
#     L = []
#     R = []
#     for i in range(n1):
#         L.append(A[p+i])
#     for i in range(n2):
#         R.append(A[q+i+1])
#     print(L, R)
#     L.append(float("inf"))
#     R.append(float("inf"))
#
#     i = 0
#     j = 0
#     for k in range(p,r+1):
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i += 1
#         else:
#             A[k] = R[j]
#             j += 1


def merge(A,p,q,r):
    L = A[p:q+1] + [float("inf")]
    R = A[q+1:r+1] + [float("inf")]
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1



def merge_sort(A,p,r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

A = [8, 7, 6, 5, 4, 3, 2, 1]
merge_sort(A, 0, 7)
print(A)


