#string = "this is test string"
#print (string.find("test"))

def solution(phone_book):
    answer = True
    pb= sorted(phone_book, key=lambda x: len(x))
    for i in range(len(pb)-1):
        for j in range(1, len(pb)-i):
            if pb[i+j].find(pb[i]) == 0:
                answer = False
                break
    return answer

a=['119', '97674223', '1195524421']
print(solution(a))