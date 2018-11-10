def ToBinary(num):
    answer=''
    result=[0,0,0,0]    #BCD 변환되어 저장될 공간입니다.
    i=3                 #result리스트의 3번 인덱스부터 2로 나눈 나머지가 들어갑니다.
    while num > 0:
        result[i] = num%2
        num = num//2
        i  -= 1
    for i in range(4):
        answer = answer+str(result[i])  #4개 원소로 이루어진 리스트형이 아닌 4자리의 2진문자열로 바꿔줍니다.
    return answer


dividelist=[]
num = int(input('10진수 숫자를 입력하세요: '))    #사용자에게 숫자를 입력받습니다.

print('분할합니다.')             #Divide
while num >= 1:                     #입력받은 숫자를 10으로 나눈 나머지들을 dividelist에 넣어줍니다.
    dividelist.append(num%10)
    num = num //10

dividelist.reverse()            #dividelist의 순서를 뒤집어주어 순서를 맞춰줍니다.
print('분할된 결과는:', dividelist)

print('각 자릿수를 이진수로 변환한 결과입니다.')     #Conquer
for n in dividelist:
    print(ToBinary(n), end =' ')
