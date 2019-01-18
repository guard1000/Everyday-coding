#아래부터 기댓값을 더해가며 올라가자.
def dp(triangle, layer):
    if layer == 0:
        return triangle[0][0]
    for i in range(len(triangle[layer])-1):
        triangle[layer-1][i] += max(triangle[layer][i],triangle[layer][i+1])
    layer -= 1
    return dp(triangle,layer)

def solution(triangle):
    if len(triangle) == 1 : return triangle[0][0]
    return dp(triangle,len(triangle)-1)

'''
#BF로 풀면 이런식이겠다. - 매우 시간복잡도 엄청남
def solution(triangle):
    n = len(triangle)
    now=[[0,triangle[0][0]]]
    nxt=[]
    for layer in range(1,n):
        for num in now:
            nxt.append([num[0],triangle[layer][num[0]]+num[1]])
            nxt.append([num[0]+1, triangle[layer][num[0]+1] + num[1]])
        now = nxt[:]
        nxt = []
    return max([x[1] for x in now])
'''

'''
#Greedy로 풀었으나 함수이름을 dp라 해버림ㅋㅋㅋㅋㅋㅋ
#그리디라서 최적해를 보장 안해!
def dp(triangle,layer,nxt,answer):
    #nxt의 자손 추가
    tmp=[]
    for n in nxt:
        if triangle[layer-1][n] not in tmp:
            tmp.append(n)
        if triangle[layer-1][n+1] not in tmp:
            tmp.append(n+1)
    nxt = []

    #nxt의 인덱스들 중 값이 젤 큰 녀석들만 남겨
    tmp = sorted(tmp, reverse=True, key=lambda x : triangle[layer-1][x])
    for i in tmp:
        if triangle[layer-1][i] == triangle[layer-1][tmp[0]]:
            nxt.append(i)
        else:
            break

    #nxt의 인덱스에 해당하는 값을 더해줌
    answer += triangle[layer-1][nxt[0]]
    #layer == len(triangle)이면, 맨 아래층임. return
    print(layer, answer, nxt)   #
    if layer == len(triangle): return answer
    #layer+1해줌
    layer += 1
    return dp(triangle,layer,nxt,answer)

def solution(triangle):
    if len(triangle) == 1: return triangle[0][0]
    nxt=[0]
    print(1, triangle[0][0])    #
    return dp(triangle,2, nxt, triangle[0][0])
'''
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))