# https://programmers.co.kr/learn/courses/30/lessons/12987?language=python3
# level 3
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            answer += 1
            A.pop(0)
            B.pop(0)
        else:
            A.pop(0)

    return answer