'''
import re
explain = """
ITU-T(국제전기통신연합 전기통신표준화부문)는 전화‧인터넷 등 네트워크와 사물인터넷(IoT), 빅데이터 등 관련 정보통신기술 및 활용, 요금 정산 등 분야의 국제 표준 권고를 제정하는 정부간 국제기구다.
연구그룹 SG13은 네트워크 품질 및 신뢰성, 클라우드컴퓨팅 및 빅데이터 등 미래 네트워크 관련 ITU-T 권고 표준의 제정 또는 개정 활동을 수행하고 있다.
이번 회의에서 채택된 빅데이터 이력 관리 표준(Y.3602)은 자료의 출처와 변경 이력, 사용된 분석 기법 등을 저장, 관리하는데 적용되어 자료의 신뢰성을 높이고 일반인들도 저장된 자료 분석 기법을 사용해 쉽게 빅데이터를 활용할 수 있도록 지원하는 기술이다.
이 표준기술은 서로 다른 빅데이터 분석 시스템 간의 협업을 가능하게 하고, 분석 절차의 자동화와 자료 감리 및 저작권 보호 등 다양한 분야에 활용된다.
클라우드 환경에서의 빅데이터 적용 기술 표준은 지난 2015년도에 우리나라 주도로 개발했던 클라우드 환경에서의 빅데이터 요구사항 및 기능에 관한 표준(ITU-T Y.3600)을 바탕으로, 클라우드 기반에서 빅데이터를 활용한 서비스를 제공할 때 필요한 기능의 구조를 상세하게 제공하고 있다.
"""
word = input("관심있는 단어는: ")
count = expla

in.count(word)
pattern = re.compile(word)
chk = pattern.finditer(explain)
print("선택된 단어", word, "의 사용 빈도수는:", count)
for i in chk:
    print(i.span())
'''

'''
#재귀
def factorial(n):
    if n == 1:
        return 1
    elif n > 0:
        return n * factorial(n-1)
print(factorial(3))
'''

'''
#실습1번
def sequential_search(target, a):
    index = 0
    while index < len(a):
        if target == a[index]:
            print (index, '인덱스에서', target, '를 찾았어요~!!')
            return index
        print(index, '인덱스에', target, '가 없네요!!')
        index += 1
    return -1

a = [37, 53, 23, 76, 14, 91, 89, 32, 42, 10]
sequential_search(32, a)
'''
graph = {'1': ['8','7','2'],
         '2': ['1', '6', '3'],
         '3': ['2', '5', '4'],
         '4': ['3'],
         '5': ['3'],
         '6': ['2'],
         '7': ['1'],
         '8': ['1', '12', '9'],
         '9': ['8', '11', '10'],
         '10': ['9'],
         '11': ['9'],
         '12': ['8'] }

def dfs(graph, root, search):
    visited = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == search:
                break
            stack.extend([x for x in graph[node] if x not in visited])
    return visited

def bfs(graph, root, search):
    visited = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node == search:
                break
            queue.extend([x for x in graph[node] if x not in visited])
    return visited

print(dfs(graph, '1', '9'))
print(bfs(graph, '1', '9'))