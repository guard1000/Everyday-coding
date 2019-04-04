def opener(world,L,R):
    cnt,visit = 0,[]
    for i in range(1,len(world)-1):
        for j in range(1,len(world)-1):
            if world[i][j][1] == 0:
                cnt += 1
                tmp=[[i,j]]
                while len(tmp) != 0:
                    nxt = tmp.pop(0)
                    visit.append(nxt)
                    world[i][j][1] = cnt
                    if world[nxt[0]-1][nxt[1]][0] != -100 and L <= abs(world[nxt[0]-1][nxt[1]][0] - world[nxt[0]][nxt[1]][0]) <= R and [nxt[0]-1,nxt[1]] not in visit:    #상
                        world[nxt[0] - 1][nxt[1]][1] = cnt
                        tmp.append([nxt[0]-1,nxt[1]])
                    if world[nxt[0]+1][nxt[1]][0] != -100 and L <= abs(world[nxt[0]+1][nxt[1]][0] - world[nxt[0]][nxt[1]][0]) <= R and [nxt[0]+1,nxt[1]] not in visit:    #하
                        world[nxt[0] + 1][nxt[1]][1] = cnt
                        tmp.append([nxt[0]+1,nxt[1]])
                    if world[nxt[0]][nxt[1]-1][0] != -100 and L <= abs(world[nxt[0]][nxt[1]-1][0] - world[nxt[0]][nxt[1]][0]) <= R and [nxt[0],nxt[1]-1] not in visit:    #좌
                        world[nxt[0]][nxt[1]-1][1] = cnt
                        tmp.append([nxt[0],nxt[1]-1])
                    if world[nxt[0]][nxt[1]+1][0] != -100 and L <= abs(world[nxt[0]][nxt[1]+1][0] - world[nxt[0]][nxt[1]][0]) <= R and [nxt[0],nxt[1]+1] not in visit:    #우
                        world[nxt[0]][nxt[1]+1][1] = cnt
                        tmp.append([nxt[0],nxt[1]+1])
    if cnt == (len(world)-2)**2:    return -1
    return cnt

def move(world, num):
    for n in range(1, num+1):
        position,possum = [],0
        for i in range(1, len(world)-1):
            for j in range(1, len(world)-1):
                if world[i][j][1] == n:
                    position.append([i,j])
                    possum += world[i][j][0]
        for pos in position:
            world[pos[0]][pos[1]][0] = possum//len(position)
            world[pos[0]][pos[1]][1] = 0

N,L,R = map(int, input().split())
answer = 0
world=[]
world.append([-100 for i in range(N+2)])
for n in range(N):
    world.append([-100]+list(map(int,input().split()))+[-100])
world.append([-100 for i in range(N+2)])
for i in range(N+2):
    for j in range(N+2):
        world[i][j] = [world[i][j],0]
while True:
    num =  opener(world,L,R)
    if num == -1: break
    answer += 1
    move(world, num)

print(answer)

'''
3 5 10
10 15 20
20 30 25
40 22 10
'''