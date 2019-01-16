def solution(people, limit):
    answer = len(people)
    people = sorted(people)
    i=0
    j=answer-1
    cnt=0
    # n명의 사람이 있을때 m쌍이 생길 수 있다면, 총 n-m번 이동해야 한다.
    while i < j:
        if people[i]+people[j]<=limit: #짝
            cnt += 1
            i += 1
            j -= 1
        else: #혼자
            j -= 1
    answer -= cnt

    return answer


p1 = [70, 50, 80, 50]
l1 = 100
p2 = [70, 80, 50]
l2 = 100

print(solution(p1, l1))
print(solution(p2, l2))