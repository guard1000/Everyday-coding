import heapq

def solution(operations):
    answer = []
    heapq.heapify(answer)

    for op in operations:
        print(answer)
        if op[0] == "I":
            heapq.heappush(answer, int(op[2:]))
        elif op[2] == '-' and len(answer) > 0:
            heapq.heappop(answer)
        elif len(answer) > 0:
            answer.pop(answer.index(max(answer)))

    if len(answer) == 0:
        return [0,0]
    return [max(answer),min(answer)]


o1 =['I 16','D 1']
o2 = ['I 7','I 5','I -5','D -1']
o3 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
o4 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

print(solution(o1))
print(solution(o2))
print(solution(o3))
print(solution(o4))
