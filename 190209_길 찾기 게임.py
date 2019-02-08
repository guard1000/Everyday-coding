import sys
sys.setrecursionlimit(10**6)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                answer[0].append(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)

        _pre_order_traversal(self.root)

    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                answer[1].append(root.data)

        _post_order_traversal(self.root)

answer = [[],[]]
def solution(nodeinfo):
    dic = {}
    for i in range(1, len(nodeinfo)+1):
        dic[nodeinfo[i-1][0]] = i
    nodeinfo = sorted(nodeinfo, reverse=True, key=lambda x: (x[1], -x[0]))
    bst = BinarySearchTree()
    for x in nodeinfo:
        bst.insert(x[0])

    bst.pre_order_traversal()
    bst.post_order_traversal()
    for i in range(2):
        for j in range(len(answer[0])):
            answer[i][j] = dic[answer[i][j]]
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
