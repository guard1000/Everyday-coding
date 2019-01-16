def available(a, b, n): #변환 가능한지 여부를 반환
    cnt = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt += 1
    if cnt == n-1:
        return True
    return False

def bfs(begin, target, words, answer):
    answer += 1
    tmp =[]
    n = len(begin)      #단어 길이
    if begin in words:
        words.remove(begin)
    for i in words:
        if available(begin, i, n):
            tmp.append(i)
    if target in tmp:
        return answer
    for i in tmp:
        return bfs(i, target, words, answer)

def solution(begin, target, words):
    answer = 0
    begin = list(begin)
    target = list(target)
    num = len(words)    #단어 갯수
    for i in range(num):     #word 리스트 정리
        words.append(list(words[0]))
        words.pop(0)

    answer = bfs(begin, target, words,answer)
    if not answer:
        answer = 0
    return answer


b1 = 'hit'
t1 = 'cog'
w1 = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
b2 = 'hit'
t2 = 'cog'
w2 = ['hot', 'dot', 'dog', 'lot', 'log']
print(solution(b1, t1, w1))
print(solution(b2, t2, w2))

