import openpyxl         #데이터를 엑셀파일로 받았으므로, openpyxl 외부 패키지를 설치해 사용합니다.

#딕셔너리로 사용자 입력에 해당하는 식품을 찾아갑니다.
dic = {'난류': 1, '우유': 2, '메밀': 3, '땅콩': 4,'대두':5,'밀': 6,'고등어':7,'게':8,'새우':9,'돼지고기':10,'복숭아':11,'토마토':12,'아황산염':13}

inp = input('못먹는 음식이 있나요?: ').split()  # 인풋받습니다.
wb = openpyxl.load_workbook('데이터_셋완성.xlsx') #엑셀파일 열기
ws = wb.active          #파일내 Active Sheet로 접근

for r in ws.rows:   #엑셀을 한줄한줄 읽습니다.z
    flag = 0        #먹을 수 있는지 없는지를 판단해주는 flag변수를 이용합니다.
    for i in inp:   #사용자가 입력한 못먹는게 있나 일일히 확인
        for j in range(2,len(r)):   # 2번 열부터 음식 번호들이 나오므로!
            if dic[i] == r[j].value:    #딕셔너리상에 매치되는 음식이 만약 해당 식품에 있다면 flag를 1로 바꿉니다.
                flag = 1
    if flag ==0:                #한 행의 검사를 마쳤을때까지 flag값이 0이라면, 먹을 수 있는 음식입니다.
        print(r[0].value,'번째날의',r[1].value,'을(를) 먹을 수 있어요.')