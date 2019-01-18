def bsearch(s,e,rocks,n):
    mid = (s+e)//2
    #print(s,mid,e)
    if s > e:
        return mid
    num = n
    tmp = rocks[0]
    i=1
    while i < len(rocks):
        if mid > rocks[i]-tmp:
            num -= 1
            if num < 0:
                break
        else:
            tmp = rocks[i]
        i += 1
    # while문을 break 없이 무사히 통과했다면 -> mid보다 작은게 n개 이하로 있었다
    if i == len(rocks):     # -> start를 mid+1로 키우자
        return bsearch(mid+1,e,rocks,n)
    #아니라면 end를 mid -1로 내리자
    return bsearch(s,mid-1,rocks,n)

def solution(distance, rocks, n):
    #다 없애기 가능할 경우
    if n == len(rocks):
        return distance
    #이분탐색 - 인접한 바위간 떨어진 거리가 기준(mid)보다 작은게 n개 있도록 찾아가자
    rocks = [0]+sorted(rocks)+[distance] #출발 ~ 도착 까지
    return bsearch(rocks[0],rocks[-1],rocks,n)

d=25
r=[2, 14, 11, 21, 17]
n=2

print(solution(d,r,n))
