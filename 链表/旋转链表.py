""""
1. 计算链表长度：首先遍历链表以计算其长度，并在此过程中找到尾节点。
2. 处理特殊情况：如果链表为空或只有一个节点，或者 k 为 0，则不需要旋转，直接返回原链表。
  如果 k 大于链表长度，我们可以通过取 k 与链表长度的模得到等效的较小的 k 值。
3. 找到旋转的起点：要将链表向右旋转 k 个位置，我们需要找到从尾部数第 k + 1 个节点，并将其作为新的头节点。
4. 执行旋转：将链表的尾部与头部连接，形成一个环，然后在新的头节点前断开环，完成旋转。
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 计算链表长度并找到尾节点
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1

        # 使链表形成环
        old_tail.next = head

        # 计算新的头节点和尾节点的位置
        new_tail = head
        for i in range(length - k % length - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # 断开环，形成新的链表
        new_tail.next = None

        return new_head
