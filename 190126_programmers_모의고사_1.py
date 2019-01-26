def solution(arrA, arrB):
    answer = False
    n = len(arrA)
    for i in range(n):
        arrA = arrA[1:] + arrA[:1]
        if arrA == arrB:
            answer = True
            break
    return answer

print(solution([7, 8, 10],[7, 8, 10]))
print(solution([4, 3, 2, 1],[5, 4, 1, 2]))
