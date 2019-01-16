def solution(weight):
    answer = 0
    weight.sort()
    for i in range(len(weight)-1):
        answer += weight[i]
        if weight[i+1]-answer > 1:
            return answer+1

    return answer+weight[len(weight)-1]+1


'''
def solution(weight):
    answer = 0
    weight.sort()
    for i in range(len(weight)-1):
        if weight[i+1] - sum(weight[:i+1]) > 1:
            return sum(weight[:i+1])+1

    return sum(weight)+1
'''
w = [3, 1, 6, 2, 7, 30, 1]
print(solution(w))