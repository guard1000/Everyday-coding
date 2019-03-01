# https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3
# level 3
def solution(dirs):
    answer = 0
    dic=set()
    pos = (0,0)
    for next in dirs:
        if next =='U': nxt = (pos[0],pos[1]+1)
        elif next =='D': nxt = (pos[0],pos[1]-1)
        elif next =='R': nxt = (pos[0]+1,pos[1])
        else: nxt = (pos[0]-1,pos[1])
        if -5 <= nxt[0] <= 5 and -5 <= nxt[1] <= 5 and (pos,nxt) not in dic:
            answer += 1
            dic.add((pos,nxt))
            dic.add((nxt,pos))
            pos = nxt
        elif -5 <= nxt[0] <= 5 and -5 <= nxt[1] <= 5:
            pos = nxt
    return answer