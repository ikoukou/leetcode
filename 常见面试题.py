################################################
# 解释并实现深度优先搜索（DFS）和广度优先搜索（BFS）   #
################################################
# 示例
# 构建一个二叉树
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#         \   /
#          8 9
class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree = Tree(1)
tree.left = Tree(2)
tree.right = Tree(3)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.left.right.right = Tree(8)
tree.right.left = Tree(6)
tree.right.right = Tree(7)
tree.right.right.left = Tree(9)

# dfs的实现，期望输出 1,2,4,5,3,6,7
def dfs(root):
    res = []
    if root is None:
        return None
    res.append(root.value)
    if root.left is not None:
        res.extend(dfs(root.left))
    if root.right is not None:
        res.extend(dfs(root.right))
    return res
print(dfs(tree))

# bfs的实现，期望输出 1,2,3,4,5,6,7
def bfs(root):
    res = []
    li = []
    if root is None:
        return None
    li.append(root)
    while li:
        node = li.pop(0)
        res.append(node.value)
        if node.left is not None:
            li.append(node.left)
        if node.right is not None:
            li.append(node.right)
    return res
print(bfs(tree))


###################################
#     判断一个链表是否存在环形结构     #
###################################
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while fast or fast.next:
        if slow == fast:
            return True
        if fast.next.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return False

# 示例
# 构建一个有环的链表
# 1 -> 2 -> 3 -> 4 -> 5
#           ^         |
#           |         v
#          8 <- 7 <- 6
head_with_cycle = ListNode(1)
head_with_cycle.next = ListNode(2)
head_with_cycle.next.next = ListNode(3)
head_with_cycle.next.next.next = ListNode(4)
head_with_cycle.next.next.next.next = ListNode(5)
head_with_cycle.next.next.next.next.next = ListNode(6)
head_with_cycle.next.next.next.next.next.next = ListNode(7)
head_with_cycle.next.next.next.next.next.next.next = ListNode(8)
head_with_cycle.next.next.next.next.next.next.next.next = head_with_cycle.next.next

# 构建一个无环的链表
# 1 -> 2 -> 3 -> 4 -> 5
head_without_cycle = ListNode(1)
head_without_cycle.next = ListNode(2)
head_without_cycle.next.next = ListNode(3)
head_without_cycle.next.next.next = ListNode(4)
head_without_cycle.next.next.next.next = ListNode(5)

print(has_cycle(head_with_cycle))  # 输出 True
print(has_cycle(head_without_cycle))  # 输出 False


# ###############################
# #     实现最近最少使用的算法      #
# ###############################
class Lru():
    def __init__(self, max):
        self.max_len = max
        self.dir = {}
    def set(self, k, v):
        if k in list(self.dir.keys()):
            self.dir.pop(k)
        if len(self.dir) >= self.max_len:
            self.dir.pop(list(self.dir.keys())[0])
        self.dir[k] = v
        return True
    def get(self, k, v):
        v = self.dir[k]
        self.dir.pop(k)
        self.dir[k] = v
        return True

lru = Lru(3)
lru.set('a', 1)
print(lru.dir)
lru.set('b', 2)
print(lru.dir)
lru.set('c', 3)
print(lru.dir)
lru.set('d', 4)
print(lru.dir)
lru.set('c', 33)
print(lru.dir)
lru.set('e', 5)
print(lru.dir)
