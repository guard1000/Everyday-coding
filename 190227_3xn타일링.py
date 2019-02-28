def solution(n):
    A = [0] * (n + 1)
    B = [0] * (n + 1)
    A[0],A[1] = 1,0
    B[0],B[1] = 0,1
    for i in range(2, n+1):
        A[i] = A[i-2] + 2*B[i-1]
        B[i] = A[i-1] + B[i-2]
    return A[n] % 1000000007