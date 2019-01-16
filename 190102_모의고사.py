def solution(answers):
    answer=[]
    answer2 = [0,0,0]
    list1=[1,2,3,4,5]
    list2=[2,1,2,3,2,4,2,5]
    list3=[3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if list1[i%5] == answers[i]:
            answer2[0] = answer2[0]+1
        if list2[i%8] == answers[i]:
            answer2[1] = answer2[1]+1
        if list3[i%10] == answers[i]:
            answer2[2] = answer2[2]+1
    if answer2[0] >= answer2[1] and answer2[0] >= answer2[2]:
        answer.append(1)
    if answer2[1] >= answer2[0] and answer2[1] >= answer2[2]:
        answer.append(2)
    if answer2[2] >= answer2[0] and answer2[2] >= answer2[1]:
        answer.append(3)
    return answer