import re
def BasicScore(word,page):    #기본점수 카운팅
    p = re.compile('[^a-zA-Z]' + word + '[^a-zA-Z]')
    b = p.findall(page)
    cnt = 0
    cnt += len(b)   #중간에 있는 경우
    if word == page[:len(word)]: #처음에 있는거임
        cnt += 1
    if word == page[-len(word):]:    #끝에 있는 경우임
        cnt += 1
    return cnt

def myAddress(page):    #자기주소를 찾아보자
    p = re.compile('<meta property="og:url" content=' + '[a-zA-Z0-9!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+' + '/>')
    ad = p.findall(page)
    return ad[0][33:-3]

def connection(page):
    p = re.compile('<a href=' + '[a-zA-Z0-9!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+' + '">')
    con = p.findall(page)
    connect =[]
    for c in range(len(con)):
        connect.append(con[c][9:-2])
    return connect

def solution(word, pages):
    pagenum=len(pages)
    answer = [[i,0,0] for i in range(pagenum)]    #[index,기본점수,링크점수]꼴
    dic={}
    i=0
    for page in pages:  #한바퀴 돌면서 기본점수와 [자기주소:페이지인덱스] 꼴의 딕셔너리 생성
        answer[i][1] += BasicScore(word.lower(),page.lower())
        dic[myAddress(page.lower())] = i
        i += 1
    i=0

    for page in pages:  #연결상태에 따른 링크점수 부여
        connect = connection(page.lower())
        n = len(connect)
        if n != 0:
            plus = answer[i][1]/n
        for c in connect:
            if c in dic:
                answer[dic[c]][2] += plus
        i += 1

    answer = sorted(answer, reverse=True, key= lambda x: (x[1]+x[2],-x[0]))
    print(dic)

    return answer[0][0]


print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
))



print()
print()
print('=======여기부터 mudule 구현================')
#갯수세기 -> 정규식으로 해결
w='abc'
a='adfhgioeabcasdf08abcd3abc asdf2abc# ab c abc'
#중간부분 찾아주기
p = re.compile('[^a-zA-Z]'+w+'[^a-zA-Z]')
b = p.findall(a)
print(b)
#첫부분 끝부분이 있는지 찾아주기
cnt=0
print(a[:len(w)],a[-len(w)-1:])
cnt += len(b)
if w == a[:len(w)]:
    print('처음')
    cnt += 1
if w == a[-len(w):]:
    print('끝')
    cnt += 1
print('총 몇개: ', cnt)
print()

#자기주소 찾기 -> 먼저 한바퀴 돌려야겠다
sample="<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>"
print(sample)
print()
p2=re.compile('<meta property="og:url" content='+'[a-zA-Z0-9!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'+'/>')
ad = p2.findall(sample)
print('자기주소:',ad[0][33:-3])
print()

#연결상태확인 - a href로 체크
p3=re.compile('<a href='+'[a-zA-Z0-9!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'+'">')
con = p3.findall(sample)
print('연결된 애들')
for c in range(len(con)):
    print(con[c][9:-2])




