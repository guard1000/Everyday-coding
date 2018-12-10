from turtle import*

penup()
금액 = numinput("지불액",'얼마를 받아야 합니까? ')
goto(0,260)
msg1 = str(int(금액))+'원 받아야 합니다!'
write(msg1,align = "left", font=('Arial', 15,"bole"))
낸돈 = numinput("받은돈",'얼마를 받았습니까? ')
goto(0,290)
msg2 = str(int(낸돈))+'원 받았습니다!'
write(msg2,align = "left", font=('Arial', 15,"bold"))

if 낸돈 < 금액:
    goto(200,260)
    write("돈이 충분하지 않습니다.", font=('Arial', 15,"italic", "underline"))
elif 낸돈 ==  금액:
    goto(200,260)
    write("거스름돈 없습니다.", font=('Arial', 15,"italic", "underline"))
    exitonclick()
else:
    change =낸돈 - 금액
    msg3 = str(int(change))+'원 거슬러 드리겠습니다!'
    goto(0,2250)
    write(msg3, align="left", font=('Arial', 15, "bold"))


def make_change(change):
    c50000 = int(change/50000)
    change = change%50000
    c10000 = int(change / 10000)
    change = change % 10000
    c5000 = int(change / 5000)
    change = change % 5000
    c1000 = int(change / 1000)
    change = change % 1000
    c500 = int(change / 500)
    change = change % 500
    c100 = int(change / 100)
    change = change % 100
    c50 = int(change / 50)
    change = change % 50
    c10 = int(change / 10)
    change = change % 10
'''
#6,7분반

from tkinter import *

def BMI():
    h = float(h_value.get())
    w = float(w_value.get())
    bmi = w/((h/100)*(h/100))

    if bmi < 18.5:
        result_value='저체중'
    elif bmi >= 18.5 and bmi < 23.0:
        result_value = '정상체중'
    elif bmi >= 23.0 and bmi < 25:
        result_value = '과체중'
    else:
        result_value = '비만'
    result.set(result_value)

window = Tk()   #윈도우 창 생성
h_value = DoubleVar()   #변수 지정
w_value = DoubleVar()
result = StringVar()

lbl = Label(window, text='BMI 프로그램: ')  #윈도우에 표시할 레이블 설정
lbl.grid(row=0, column=0, columnspan=2) #레이블 위치 설정

h_lbl = Label(window, text='키를 입력하세요: ')    #키 레이블 위젯 설정
h_lbl.grid(row=1, column=0)   #키 레이블 위젯 위치 설정

h_entry = Entry(window, textvariable = h_value) #키 한줄 텍스트 위젯 속성 설정
h_entry.grid(row=1, column=1)

w_lbl = Label(window, text='몸무게를 입력하세요: ')    #몸무게
w_lbl.grid(row=2, column=0)

w_entry = Entry(window, textvariable = w_value)
w_entry.grid(row=2, column=1)

result_value_lbl = Label(window, text='판단 결과: ')
result_value_lbl.grid(row=3, column=0)

result_value_lbl = Label(window, textvariable=result)   #결과 한줄 텍스트 위젯 속성 설정
result_value_lbl.grid(row=3, column=1)

calc_btn = Button(window, text='계산!', command=BMI)
calc_btn.grid(row=4, column=1)
window.mainloop()     #윈도우 창의 이벤트 메시지 처리 루프

'''


'''
#5분반-이진탐색

def binary_search(list, target):
    first = 0
    last = len(list)-1
    found = -1

    while(first <= last and found == -1):
        mid = (first+last)//2

        if target == list[mid]:
            found = mid
        else:
            if list[mid] > target:
                last = mid -1
            else:
                first = mid + 1
    if found == -1:
        print('이분탐색 실패: 찾고자 하는', target, '이 없네요!!')
        return False
    else:
        print('이분탐색 성공:', mid, '인덱스에서', target, '을 찾았어요~!!')
        return True

list = [6,13,14,25,33,43,51,53,64,72,84,93,95,96,97]
print(binary_search(list,33))
print(binary_search(list,90))
'''
'''
#5분반-이진탐색 with GUI
from tkinter import *
def binary_search(list, target):
    first = 0
    last = len(list)-1
    found = -1
    search_process_txt.delete(1.0, END) #멀티라인 텍스트 위젯의 첫줄 삭제

    while(first <= last and found == -1):
        mid = (first+last)//2
        if target == list[mid]:
            found = mid
        else:
            if list[mid] > target:
                last = mid -1
            else:
                first = mid + 1
    if found == -1:
        not_find_print = str(mid) + ' 인덱스에 ' + str(target) + '가 없네요!!\n'
        search_process_txt.insert(1.0, not_find_print)

    else:
        find_print = str(mid) + ' 인덱스에서 ' + str(target) + '를 찾았어요~!!\n'
        search_process_txt.insert(1.0, find_print)

list = [6,13,25,33,43,53,64,72,84,97]

window =Tk()
window.title('이분탐색')
window.geometry('400x300+100+100')

lbl = Label(window, text='입력된 자료들')
lbl.grid(row='0', column='0', padx='10', pady='10', sticky='e')

list_print_txt = Label(window, text=list, width='35', relief='solid')
list_print_txt.grid(row='0', column='1', columnspan='2', padx='0')

target_txt = Entry(window, width='20')
target_txt.grid(row='1', column='1', pady=10)

btn = Button(window, text = '이분탐색 시작', command = lambda:binary_search(list, int(target_txt.get())))
btn.grid(row='1', column='2', padx='10', pady='10', sticky='w')

search_process_txt = Text(window, width='47', height='10', relief='solid')
search_process_txt.grid(row='2', columnspan='3', padx='10', pady='10')

window.mainloop()
'''