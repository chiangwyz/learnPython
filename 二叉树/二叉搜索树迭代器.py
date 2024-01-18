"""
为了实现这个二叉搜索树迭代器 BSTIterator，我们需要利用二叉搜索树（BST）的中序遍历的特性。中序遍历一个BST会得到一个升序的元素序列。

我们的目标是在 O(h) 的空间复杂度下实现 next() 和 hasNext() 操作，其中 h 是树的高度。
这意味着我们不能简单地将树的所有元素存入一个数组中然后迭代这个数组，因为这样的空间复杂度是 O(n)，其中 n 是树中节点的数量。

解决方案是使用一个栈来模拟递归过程中的系统调用栈，实现中序遍历。我们的迭代器将会遍历树并将节点按需压入栈中。具体来说：

1. 在构造函数中，我们从根节点开始，将所有左子节点添加到栈中。
2. next() 函数将返回栈顶元素的值，并将指针（栈顶元素）移动到其中序后继。
3. hasNext() 函数仅检查栈是否为空。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        """
        从给定节点开始，将所有左子节点添加到栈中。
        """
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        返回栈顶元素的值，并将指针移动到其中序后继。
        """
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        返回栈是否非空。
        """
        return len(self.stack) > 0

# 示例代码，展示如何使用 BSTIterator
root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
iterator = BSTIterator(root)
print(iterator.next())    # 输出 3
print(iterator.next())    # 输出 7
print(iterator.hasNext()) # 输出 True
print(iterator.next())    # 输出 9
# ...
