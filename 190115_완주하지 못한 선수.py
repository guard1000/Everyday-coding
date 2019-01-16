def solution(participant, completion):
    participant.sort()
    completion.sort()
    i,n = 0,len(completion)
    while i < n:
        if participant[i] != completion[i]:
            return participant[i]
        i += 1
    return participant[n]


p1 = (['mislav', 'stanko', 'mislav', 'ana'])
c1 = (['stanko', 'ana', 'mislav'])
print(solution(p1, c1))

'''
#객체는 빼기가 가능하다!
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

'''