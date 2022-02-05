A, B = map(str, input().split())

if A != B and '0' not in A and '0' not in B:
    A = int(A[2] + A[1] + A[0])
    B = int(B[2] + B[1] + B[0])
    print(max(A,B))