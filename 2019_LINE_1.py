# Nat = input().split()                   #나라 입력받음
# inp.append(list(input().split()))
# n, t, m, p = map(int, input().split())
# inp = list(input().upper())
# blist = copy.copy(alist)            #blist에 alist를 복제
# result = sorted(result, key=lambda x:x[1]) #1번 인덱스값을 기준으로 소팅할때 람다
alist = [11, 128, 15, 111 ,59 ,31 ,70 ,102, 50 ,172 ,88, 56 ,40, 41 ,12]

answer = 20000
    for distance in alist:
        distance = int(token)
            if distance < 4 or distance > 178:
              break
        elif distance <= 40:
            if answer-720 <0:
                break
            else:
                answer = answer - 720
        else:
            over=((distance-41)//8)+1
            if answer - (720+over*80) <0:
                break
            else:
                answer = answer - (720+over*80)
    print(answer)
