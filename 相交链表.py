# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 创建两个指针，分别指向两个链表的头节点
        pointerA, pointerB = headA, headB
        # 标记两个链表是否已经遍历到对方的尾部
        switchedA, switchedB = False, False

        # 遍历两个链表
        while pointerA is not pointerB:
            # 如果当前指针不为空，则移动到下一个节点
            if pointerA is not None:
                pointerA = pointerA.next
            # 如果当前指针为空，且未切换过，则切换到另一个链表的头节点
            elif not switchedA:
                pointerA = headB
                switchedA = True
            # 如果当前指针为空，且已切换过，则说明不存在相交节点
            else:
                return None

            # 对pointerB进行相同的操作
            if pointerB is not None:
                pointerB = pointerB.next
            elif not switchedB:
                pointerB = headA
                switchedB = True
            else:
                return None
        
        # 如果两个链表相交，最终两个指针会在相交节点处相遇，否则在链表末尾处相遇（都是None）
        return pointerA
