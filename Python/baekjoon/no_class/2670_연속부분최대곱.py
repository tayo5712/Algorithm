# def LCA(root, p, q):
#     if root == None:
#         return None
#
#     left = LCA(root.left, p, q)
#     right = LCA(root.right, p ,q)
#     if root == p or root == q:
#         return root
#     elif left and right:
#         return root
#     return left or right
#
# LCA([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4)

from collections import deque

def maxDepth(root):
    if root is None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1

    # max_depth = 0
    # if root is None:
    #     return max_depth
    #
    # q = deque()
    # q.append((root, 1))
    # visited = set()
    # visited.add(root)
    # while q:
    #     cur_node, cur_depth = q.popleft()
    #     max_depth = cur_depth
    #     if cur_node.left:
    #         q.append((cur_node.left, cur_depth + 1))
    #     if cur_node.right:
    #         q.append((cur_node.right, cur_depth + 1))
    # return max_depth

# root = [3, 9, 20, None, None, 15, 7]

class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v


root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

print(maxDepth(root))

