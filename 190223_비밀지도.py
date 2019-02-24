def solution(n, arr1, arr2):
    answer = [['#'for i in range(n)] for j in range(n)]
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:].zfill(n)
        arr2[i] = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if int(arr1[i][j]) + int(arr2[i][j]) == 0:
                answer[i][j]=' '
    for i in range(n):
        answer[i] = ''.join(answer[i])
    return answer