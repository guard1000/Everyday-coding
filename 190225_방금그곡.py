def solution(m, musicinfos):
    answer=[]
    dic = {'C#': 'H', 'D#': 'I', 'F#': 'J', 'G#': 'K', 'A#': 'L', 'B#': 'M', 'E#': 'N'} # #들은 다른 음으로 아예 바꿔주자
    ml = len(m)
    i=ml-1
    m = list(m) #m을 음을 끊어서 리스트로
    while i > -1:
        if m[i] =='#':
            m[i-1] = dic[m[i-1]+'#']
            m.pop(i)
            i -= 1
        i -=1

    for i in range(len(musicinfos)):
        musicinfos[i] =musicinfos[i].split(',')
        musicinfos[i][3] = list(musicinfos[i][3])
        j = len(musicinfos[i][3])-1
        while j > -1:   #musicinfo 안에 있는 음악들도 음별로 바꿔서 넣어주자
            if musicinfos[i][3][j] == '#':
                musicinfos[i][3][j-1] = dic[musicinfos[i][3][j-1]+'#']
                musicinfos[i][3].pop(j)
                j -= 1
            j -= 1
        time = (int(musicinfos[i][1][:2])*60 + int(musicinfos[i][1][-2:])) - (int(musicinfos[i][0][:2])*60 + int(musicinfos[i][0][-2:]))    #총 들은시간
        l = len(musicinfos[i][3])
        mok = time // l
        nam = time % l
        target = mok*musicinfos[i][3] + musicinfos[i][3][:nam]  #들은시간동안 어떤 음들이 나왔는지 리스트
        target=''.join(target)
        m = ''.join(m)
        if m in target: #타겟에 있었다면 answer list에 넣어주자
            answer.append([musicinfos[i][2],time,int(musicinfos[i][0][:2])*60 + int(musicinfos[i][0][-2:])])
    if len(answer) == 0: return "(None)"    #아무것도 없었다면 none 리턴
    answer=sorted(answer, reverse = True, key=lambda x: (x[1], (1440-x[2])))    #여러개 있다면, 시간과, 시작시간 기준으로 정렬해서 젤 앞에꺼
    return answer[0][0]

print(solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF'] ))