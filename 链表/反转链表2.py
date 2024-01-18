"""
要实现链表中指定区间的节点反转，我们可以通过几个关键步骤来完成。
下面是具体的实现方式：

1. 定位到反转区间的前一个节点和反转区间的第一个节点：
    首先，我们需要一个指针遍历链表，找到反转区间的前一个节点（称之为 pre_node）和反转区间的第一个节点（称之为 first_node）。
    在示例 1 中，pre_node 指向值为 1 的节点，而 first_node 指向值为 2 的节点。
2. 执行反转操作：接着，我们需要在反转区间内对节点进行反转。
    这可以通过迭代的方式完成，每次迭代将当前节点的 next 指针指向前一个节点。
    这个过程需要继续，直到我们到达区间的最后一个节点。
3. 链接反转后的链表部分与原链表的其他部分：
    反转完成后，我们需要将反转前的 pre_node 的 next 指针指向反转区间的最后一个节点，
    同时将反转区间的第一个节点（现在在反转区间的末尾）的 next 指针指向反转区间后面的第一个节点。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 创建一个哑节点
        dummy = ListNode(0, head)
        pre_node = dummy

        # 移动到反转的起点前一个位置
        for _ in range(left - 1):
            pre_node = pre_node.next

        # 开始反转
        current = pre_node.next
        prev = None
        for _ in range(right - left + 1):
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # 链接反转后的链表部分与原链表的其他部分
        pre_node.next.next = current
        pre_node.next = prev

        return dummy.next

