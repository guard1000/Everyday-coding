def solution(array, commands):
    answer = []
    for c in commands:
        alist = array[c[0]-1:c[1]]
        alist.sort()
        answer.append(alist[c[2]-1])
    return answer