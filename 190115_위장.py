def solution(clothes):
    answer = 1
    n = len(clothes)
    alist=[]
    #각 의상 종류별 몇개의 옷이 있는지를 저장한 리스트 alist
    clothes =sorted(clothes, key=lambda x : x[1])
    i = 0
    while i < n:
        j = i
        while j < n and clothes[i][1] == clothes[j][1]:
            j += 1
        alist.append(j-i)
        i = j

    #각 의상별 안입을 수 있는 경우까지 고려해 모두 곱함
    for c in alist:
        answer *= (c+1)

    return answer-1

c1 = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
c2 = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]
print(solution(c1))
print(solution(c2))

