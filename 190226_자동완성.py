class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.cnt=0
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            curr_node.cnt +=1

        curr_node.data = string

    def count_trie(self, string):
        curr_node = self.head
        cnt=0
        for char in string:
            cnt +=1
            curr_node = curr_node.children[char]
            if curr_node.data == string or curr_node.cnt==1:
                return cnt

def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
    for word in words:
        answer += trie.count_trie(word)
    return answer


'''
def solution(words):
    answer = 0
    for word in words:
        l = len(word)
        i=0
        while i < l:
            cnt=0
            for w in words:
                if w[:l-i] == word[:l-i]:
                    cnt += 1
            if cnt > 1 and i != 0:
                answer += (l-i+1)
                break
            elif cnt > 1 and i == 0:
                answer += (l - i)
                break
            i += 1
        if i == l:
            answer += 1

    return answer
'''
print(solution(['war','word','world','warrior']))
#print(solution(['go','gone','guild']))
#print(solution(['go','wone','euild']))