"""
这个问题要求实现一个函数，用于将一个单链表中的节点每 k 个一组进行翻转，如果链表的长度不是 k 的整数倍，
则最后剩余的节点保持原顺序。为了实现这个函数，我们可以采取以下步骤：

1. 检查链表长度：首先检查链表中是否至少有 k 个节点，如果不足 k 个，则不需要翻转。
2. 翻转一组节点：对于每一组长度为 k 的节点，我们需要进行翻转。这可以通过更改节点的 next 指针来实现。
3. 连接翻转后的部分与未翻转部分：翻转后，需要正确地连接翻转后的链表部分与其余未翻转的链表部分。
4. 重复上述步骤：对链表中的每一组长度为 k 的连续节点重复上述过程。
5. 处理边界情况：考虑当链表长度不是 k 的整数倍时，剩余的节点不进行翻转。
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 定义一个辅助函数，用于翻转链表的一部分
        def reverse(head, tail):
            prev = tail.next
            p = head
            while prev != tail:
                nex = p.next
                p.next = prev
                prev = p
                p = nex
            return tail, head

        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 检查剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = reverse(head, tail)
            # 把翻转后的链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next
