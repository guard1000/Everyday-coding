#17년 카카오 3차_압축
def solution(inp):
    dic = {'A':'1', 'B':'2', 'C':'3', 'D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}
    inp = list(inp)
    answer = []
    while len(inp) > 0:

        if len(inp) > 1:
            while len(inp) >= 2 and ((inp[0]+inp[1]) in dic) : #디렉토리에 있는 키 값이라면 하나로 뭉쳐줘!
                inp[0] = inp[0]+inp[1]
                inp.pop(1)

            w = inp[0] #inp리스트 0번이 w 1번이 c에 변수 삽입

            if len(inp) >= 2:
                dic[(inp[0]+inp[1])] = len(dic.keys())+1 # dic에 추가
            answer.append(int(dic[w]))
            inp.pop(0)

        elif len(inp) == 1:
            w = inp[0]
            answer.append(int(dic[w]))
            inp.clear()
    return answer