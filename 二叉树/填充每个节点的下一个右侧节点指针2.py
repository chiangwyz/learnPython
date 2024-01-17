"""
要解决这个问题，我们可以使用层序遍历（也称为广度优先搜索）的方法。在遍历每一层的时候，我们将每个节点的 next 指针指向它的右侧节点。
如果右侧没有节点，则保持 next 指针为 NULL。由于要求只使用常量级额外空间，我们不能使用额外的数据结构来存储每层的节点。
因此，我们需要巧妙地利用 next 指针来进行层级遍历。

我们的策略是这样的：首先，为了访问每一层的第一个节点，我们需要一个指向每一层最左侧节点的指针（称之为层头指针）。
然后，对于每一层，我们使用另一个指针（称之为当前指针）从左向右遍历，同时更新每个节点的 next 指针。

2024年1月17日10:04:44
该题解法并不好，待优化。
"""

from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: Node = None, right: Node = None, next: Node = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        # 当前层的第一个节点
        head = root

        while head:
            # 使用虚拟节点作为下一层的前置节点
            dummy = Node(0)
            tail = dummy
            current = head

            # 遍历当前层
            while current:
                # 如果左子节点存在，链接到下一层
                if current.left:
                    tail.next = current.left
                    tail = tail.next

                # 如果右子节点存在，链接到下一层
                if current.right:
                    tail.next = current.right
                    tail = tail.next

                # 移动到当前层的下一个节点
                current = current.next

            # 移到下一层
            head = dummy.next

        return root


# test
# 构建二叉树的辅助函数
def build_tree(values: list[int]):
    if not values:
        return None

    root = Node(values[0])
    queue = [root]

    i = 1
    while i < len(values):
        current = queue.pop(0)

        if values[i] is not None:
            current.left = Node(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = Node(values[i])
            queue.append(current.right)
        i += 1

    return root

# 打印层序遍历结果的辅助函数
def print_tree(root: Node):
    queue = [root]
    while queue:
        current = queue.pop(0)
        next_val = current.next.val if current.next else '#'
        print(current.val, '->', next_val, end=' , ')

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# 构建二叉树
root = build_tree([1,2,3,4,5,None,7])

# 应用 connect 方法
sol = Solution()
sol.connect(root)

# 打印结果，以验证输出
print_tree(root)
