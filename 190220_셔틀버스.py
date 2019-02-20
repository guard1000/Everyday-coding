def solution(n, t, m, timetable):
    for i in range(len(timetable)): #timetable 분으로 정리
        time = timetable[i].split(':')
        timetable[i] = int(time[0])*60 + int(time[1])
    timetable.sort()

    N=len(timetable)
    time,pos=540,0
    for i in range(n-1):    #n-1번 일단 돌려
        j=0
        while m > j and pos < N:
            if timetable[pos] <= time:
                pos += 1
            j += 1
        time += t
    if pos >= N:    #만약 이미 다 타서 앞에 없다면 제일 막차시간에 나오면 됨
        return str(time//60).rjust(2,'0')+':'+str(time%60).rjust(2,'0')
    tmp = timetable[pos:]   #앞에 이미 타고 간 애들은 고려 X
    for j in range(len(tmp)-1,-1,-1):   #막차시간보다 늦게 올 애들도 고려 X
        if tmp[j] > time:
            tmp.pop(j)
        else:
            break

    if len(tmp) < m:    #짜피 m명 보다 적다면, 그냥 막차시간에 나오면 댐
        return str(time // 60).rjust(2, '0') + ':' + str(time % 60).rjust(2, '0')
    return str((max(set(tmp[:m]))-1) // 60).rjust(2, '0') + ':' + str((max(set(tmp[:m]))-1) % 60).rjust(2, '0')
    #그렇지 않다면, 그냥 앞에서부터 m명 슬라이싱 해서, set으로 중복 제거하고, 그중 젤 큰놈보다 1분 전에 나와버리자.

print(solution(1,1,5,['08:00', '08:01', '08:02', '08:03']))
print(solution(2,10,2,['09:10', '09:09', '08:00']))
print(solution(2,1,2,['09:00', '09:00', '09:00', '09:00']))
print(solution(1,1,5,['00:01', '00:01', '00:01', '00:01', '00:01']))
print(solution(1,1,1,['23:59']))
print(solution(10,60,45,['23:59', '23:59','23:59','23:59','23:59','23:59','23:59','23:59','23:59','23:59','23:59','23:59']))
print(solution(3,10,2,['09:10', '09:09', '08:00']))
