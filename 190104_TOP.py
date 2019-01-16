def solution(heights):
    answer = [0]    #어차피 1번탑은 수신 없음

    for i in range(1, len(heights)):    #어차피 1번탑은 수신 없음
        j = i-1
        while j > -1:
            if heights[j] > heights[i]:
                answer.append(j+1)
                break
            j -= 1
        if j == -1:
            answer.append(0)
    return answer


h1=[6,9,5,7,4]
h2=[3,9,9,3,5,7,2]
h3=[1,5,3,6,7,6,5]

print(solution(h1))
print(solution(h2))
print(solution(h3))