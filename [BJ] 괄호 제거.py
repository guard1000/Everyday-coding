import itertools
# 0. 입력
A = list(input())
answer = []
# 1.쌍이 되는 '(' 와 ')' 의 위치들을 후보군 리스트로 만듬
candidates = []
idx, stack = 0, []
while idx < len(A):
    if A[idx] == '(':
        stack.append(idx)
    elif A[idx] == ')':
        candidates.append([stack.pop(-1),idx])
    idx += 1

# 2. 조합 가능한 경우만큼 해당 위치를 제거한 answer들을 선정
idxs = [_ for _ in range(len(candidates))]
for n in range(1, len(candidates)+1):
    mycombination = itertools.combinations(idxs, n) # 조합 생성
    for mycomb in mycombination:
        del_list = []
        for _ in mycomb:
            del_list += candidates[_] # 출력하지 않을 index들 선정
        ans = ''
        for _ in range(len(A)):
            if _ not in del_list:
                ans += A[_]
        if ans not in answer: # 중복제거
            answer.append(ans)

answer.sort() # 사전순 정렬
for ans in answer:
    print(ans)


'''
(2+(2*2)+2)
(1+(2*(3+4)))
'''