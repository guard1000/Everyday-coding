def solution(citations):
    i = 0
    citations = sorted(citations, reverse=True)
    while i < len(citations) and citations[i] > i:
            i += 1
    return i

c=[3, 0, 6, 1, 5]
print(solution(c))