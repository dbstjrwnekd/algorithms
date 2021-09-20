import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, index = 0, val=0, left=None, right=None):
        self.index = index
        self.val = val
        self.left = left
        self.right = right

def solution(nodeinfo):
    if not nodeinfo:
        return [[],[]]
    
    index = {}
    for i, val in enumerate(nodeinfo):
        x, y = val
        index[(x,y)] = i+1
    
    nodeinfo.sort(key = lambda x : -x[1])
    root = Node(index[(nodeinfo[0][0],nodeinfo[0][1])], nodeinfo[0][0])
    for i, val in enumerate(nodeinfo[1:]):
        makeNode(root, Node(index[(val[0],val[1])], val[0]))
    answer = []
    answer.append(preorder(root))
    answer.append(postorder(root))
    
    return answer

def makeNode(root, node):
    if root.val < node.val:
        if not root.right:
            root.right = node
        else:
            makeNode(root.right, node)
    else:
        if not root.left:
            root.left = node
        else:
            makeNode(root.left, node)
            
def preorder(root):
    answer = []
    
    def dfs(node):
        if not node:
            return
        answer.append(node.index)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return answer

def postorder(root):
    answer = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        answer.append(node.index)
    dfs(root)
    return answer
    