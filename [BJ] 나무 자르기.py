# 이진탐색으로 풀어보자
N, M = map(int, input().split())
A = list(map(int, input().split()))
answers = []

l, r = 0, max(A)
while not r < l:
    answer = int((l + r) / 2)
    tmp = sum(_-answer if _ > answer else 0 for _ in A)
    if tmp == M:
        answers.append(answer)
        break

    elif tmp > M:
        answers.append(answer)
        l = answer+1
    else:
        r = answer-1

print(max(answers))


'''
4 7
20 15 10 17

5 20
4 42 40 26 46
'''