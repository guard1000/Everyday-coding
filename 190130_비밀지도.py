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

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[2, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))