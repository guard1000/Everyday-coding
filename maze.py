from random import *
max_size = 20

matrix = [[0 for col in range(max_size)] for row in range(max_size)]    #미로 생성
cnt = 0
btcnt = 0
excnt=[]

def primsmaze(maze,cnt):
    mlist=[]
    if maze[max_size-1][max_size-1] == 1:   # or cnt == 1000:
        return maze

    for i in range(max_size):
        for j in range(max_size):
            if maze[i][j] >= 1:
                mlist.append([i,j]) #현재 1이상인 애들 리스트로 받아 둠
    if len(mlist)>3:
        ranpos = randint(len(mlist)-3,len(mlist)-1)
    else:
        ranpos = randint(0, len(mlist)-1)   #누구 기준으로
    randir = randint(0,5)   #어떤 방향으로 갈지! 0:오 1:왼 2:위 3:아래
    #maze[mlist[ranpos][0]][mlist[ranpos][1]] += 1

    if mlist[ranpos][0] == 0 and randir != 2 : #젤 윗줄 -> 더 위로 갈 순 없어.
        if randir == 0 and mlist[ranpos][1]< max_size-1 and maze[mlist[ranpos][0]][mlist[ranpos][1]+1] < 1: #오른쪽방향일때, 이미 기준의 오른쪽이 1이 아니면 바꿔줌.
            maze[mlist[ranpos][0]][mlist[ranpos][1]+1] = 1
        elif randir == 1 and mlist[ranpos][1]>0 and maze[mlist[ranpos][0]][mlist[ranpos][1]-1] < 1: #왼쪽 방향일때, 이미 기준의 왼쪽이 1이 아니면 바꿔줌
            maze[mlist[ranpos][0]][mlist[ranpos][1]-1] = 1
        elif randir == 3 and maze[mlist[ranpos][0]+1][mlist[ranpos][1]] < 1: #아랫쪽 방향일때, 이미 기준의 아래(다음줄이니까 +1)가 1이 아니면 바꿔줌
            maze[mlist[ranpos][0]+1][mlist[ranpos][1]] = 1

    elif mlist[ranpos][0] == max_size-1 and randir != 3 : #젤 아랫줄 -> 더 아래로 갈 순 없어.
        if randir == 0 and mlist[ranpos][1]<max_size-1 and maze[mlist[ranpos][0]][mlist[ranpos][1]+1] < 1: #오른쪽방향일때, 이미 기준의 오른쪽이 1이 아니면 바꿔줌.
            maze[mlist[ranpos][0]][mlist[ranpos][1]+1] = 1
        elif randir == 1 and mlist[ranpos][1]>0 and maze[mlist[ranpos][0]][mlist[ranpos][1]-1] < 1: #왼쪽 방향일때, 이미 기준의 왼쪽이 1이 아니면 바꿔줌
            maze[mlist[ranpos][0]][mlist[ranpos][1]-1] = 1
        elif randir == 2 and maze[mlist[ranpos][0]-1][mlist[ranpos][1]] < 1: #위쪽 방향일때, 기준의 위가 1이 아니면 바꿔줌
            maze[mlist[ranpos][0]-1][mlist[ranpos][1]] = 1

    elif mlist[ranpos][1] == max_size - 1 and randir != 0:  # 젤 오른쪽 줄 -> 더 오른쪽으로 갈 순 없어.
        if randir == 1 and maze[mlist[ranpos][0]][mlist[ranpos][1] - 1] < 1:  # 왼쪽 방향일때, 이미 기준의 왼쪽이 1이 아니면 바꿔줌.
            maze[mlist[ranpos][0]][mlist[ranpos][1] - 1] = 1
        elif randir == 2 and mlist[ranpos][0] > 0 and maze[mlist[ranpos][0]-1][mlist[ranpos][1]] < 1:  # 위쪽 방향일때, 이미 기준의 위쪽이 1이 아니면 바꿔줌
            maze[mlist[ranpos][0]-1][mlist[ranpos][1]] = 1
        elif randir == 3 and mlist[ranpos][0] < max_size-1 and maze[mlist[ranpos][0] + 1][mlist[ranpos][1]] < 1:  # 아래쪽 방향일때, 기준의 아래가 1이 아니면 바꿔줌
            maze[mlist[ranpos][0] + 1][mlist[ranpos][1]] = 1

    elif mlist[ranpos][1] == 0 and randir != 1:  # 젤 왼쪽 줄 -> 더 왼쪽으로 갈 순 없어.
        if randir == 0 and maze[mlist[ranpos][0]][mlist[ranpos][1] + 1] < 1:  # 오른쪽 방향일때, 이미 기준의 오른쪽이 1이 아니면 바꿔줌.
            maze[mlist[ranpos][0]][mlist[ranpos][1] + 1] = 1
        elif randir == 2 and mlist[ranpos][0] > 0 and maze[mlist[ranpos][0]-1][mlist[ranpos][1]] < 1:  # 위쪽 방향일때, 이미 기준의 위쪽이 1이 아니면 바꿔줌
            maze[mlist[ranpos][0]-1][mlist[ranpos][1]] = 1
        elif randir == 3 and mlist[ranpos][0] < max_size-1 and maze[mlist[ranpos][0] + 1][mlist[ranpos][1]] < 1:  # 아래쪽 방향일때, 기준의 아래가 1이 아니면 바꿔줌
            maze[mlist[ranpos][0] + 1][mlist[ranpos][1]] = 1

    else:
        if randir == 0 and mlist[ranpos][1] < max_size-1 and maze[mlist[ranpos][0]][mlist[ranpos][1] + 1] < 1:
            maze[mlist[ranpos][0]][mlist[ranpos][1] + 1] = 1
        elif randir == 1 and mlist[ranpos][1] > 0 and maze[mlist[ranpos][0]][mlist[ranpos][1] - 1] < 1:  # 왼쪽 방향일때, 이미 기준의 왼쪽이 1이 아니면 바꿔줌.
            maze[mlist[ranpos][0]][mlist[ranpos][1] - 1] = 1
        elif randir == 2 and mlist[ranpos][0] > 0 and maze[mlist[ranpos][0]-1][mlist[ranpos][1]] < 1:  # 위쪽 방향일때, 이미 기준의 위쪽이 1이 아니면 바꿔줌
            maze[mlist[ranpos][0]-1][mlist[ranpos][1]] = 1
        elif randir == 3 and mlist[ranpos][0] < max_size-1 and maze[mlist[ranpos][0] + 1][mlist[ranpos][1]] < 1:  # 아래쪽 방향일때, 기준의 아래가 1이 아니면 바꿔줌
            maze[mlist[ranpos][0] + 1][mlist[ranpos][1]] = 1
    cnt = cnt+1
    return primsmaze(maze,cnt)


def explore(pos):       #이게 맞냐
    if pos[0] == max_size-1 and pos[1] == max_size-1:
        return answer
    elif pos[0] < max_size-1 and pos[1] < max_size-1:
        if answer[pos[0]+1][pos[1]] == 1:
            answer[pos[0] + 1][pos[1]] = 5
            excnt.append(1)  # 1이면 아래로 이동
            # print('[',pos[0],pos[1],']','에서 excnt',excnt)   #
            return explore([pos[0]+1,pos[1]])
        elif answer[pos[0]][pos[1]+1] == 1:
            answer[pos[0]][pos[1] + 1] = 5
            excnt.append(2) # 2이면 오른쪽으로 이동
            # print('[',pos[0],pos[1],']','에서 excnt',excnt)   #
            return explore([pos[0], pos[1]+1])
        elif answer[pos[0]][pos[1]+1] == 0 and answer[pos[0]+1][pos[1]] == 0:
            if len(excnt)==0:
                print("미로가 잘못 생성되서 탈출이 불가능합니다! 다시 도전해 보아요")
                return 0
            recent = excnt.pop()
            answer[pos[0]][pos[1]] = 0
            if recent == 1:     #이전에 내려왔다라면,
                #  print('[', pos[0], pos[1], ']', '에서 excnt', excnt)  #
                return explore([pos[0]-1,pos[1]])
            elif recent == 2:
                #  print('[', pos[0], pos[1], ']', '에서 excnt', excnt)  #
                return explore([pos[0], pos[1]-1])

    elif pos[0] == max_size-1:
        if answer[pos[0]][pos[1]+1] == 1:
            answer[pos[0]][pos[1] + 1] = 5
            excnt.append(2)  # 2이면 오른쪽으로 이동
            # print('[',pos[0],pos[1],']','에서 excnt',excnt)   #
            return explore([pos[0], pos[1] + 1])
        elif answer[pos[0]][pos[1]+1] == 0 and answer[pos[0]-1][pos[1]] == 1:
            answer[pos[0]-1][pos[1]] = 5
            excnt.append(3)  # 3이면 위쪽으로 이동(이건 맨 아랫줄만가능)
            #  print('[', pos[0], pos[1], ']', '에서 excnt', excnt)  #
            return explore([pos[0]-1, pos[1]])
        elif answer[pos[0]][pos[1]+1] == 0:
            if len(excnt)==0:
                print("미로가 잘못 생성되서 탈출이 불가능합니다! 다시 도전해 보아요")
                return 0
            recent = excnt.pop()
            answer[pos[0]][pos[1]] = 0
            if recent == 1:  # 이전에 내려왔다라면,
                # print('[', pos[0], pos[1], ']', '에서 excnt', excnt) #
                return explore([pos[0] - 1, pos[1]])
            elif recent == 2:
                #  print('[', pos[0], pos[1], ']', '에서 excnt', excnt) #
                return explore([pos[0], pos[1] - 1])
            elif recent == 3:
                # print('[', pos[0], pos[1], ']', '에서 excnt', excnt) #
                return explore([pos[0]+1, pos[1]])

    elif pos[1] == max_size - 1:
        if answer[pos[0]+1][pos[1]] == 1:
            answer[pos[0] + 1][pos[1]] = 5
            excnt.append(1)  # 1이면 아래로 이동
            # print('[',pos[0],pos[1],']','에서 excnt',excnt)   #
            return explore([pos[0]+1,pos[1]])
        elif answer[pos[0]+1][pos[1]] == 0:
            if len(excnt)==0:
                print("미로가 잘못 생성되서 탈출이 불가능합니다! 다시 도전해 보아요")
                return 0
            recent = excnt.pop()
            answer[pos[0]][pos[1]] = 0
            if recent == 1:     #이전에 내려왔다라면,
                # print('[', pos[0], pos[1], ']', '에서 excnt', excnt)  #
                return explore([pos[0]-1,pos[1]])
            elif recent == 2:
                #  print('[', pos[0], pos[1], ']', '에서 excnt', excnt)  #
                return explore([pos[0], pos[1]-1])



matrix[0][0] = 1

answer = primsmaze(matrix,cnt)

print('조작 전 미로')
for i in range(max_size):
    print(answer[i])
print()

print('프림슨 알고리즘으로 미로 생성')
for i in range(max_size-1, 0, -1):
    for j in range(max_size-2, 0, -1):
        if answer[i][j] == 1 and answer[i][j+1] == 1 and answer[i][j-1] == 1 and answer[i-1][j] == 1 and answer[i-1][j+1] == 1 and answer[i-1][j-1] == 1:
            ran = randint(0, 3)
            if i == max_size-1 and ran<=2:
                answer[i][j] = 0
            elif ran <= 1 and i< max_size-2 and not (answer[i+1][j] == 1 and answer[i+1][j-1] == 0  and answer[i+1][j] == 0):
                answer[i][j] = 0

for i in range(max_size):
    print(answer[i])
print()

answer = explore([0,0])
answer[0][0] = 5
print("백트래킹을 이용한 미로 탈출 경로(5를 따라 가면 탈출)")
for i in range(max_size):
    print(answer[i])


