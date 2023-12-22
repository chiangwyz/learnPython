"""
解题步骤如下：

1. 创建一个哑节点（dummy node），其 next 指向链表的头节点。这样可以方便地处理头节点可能被删除的情况。
2. 使用两个指针 prev 和 curr 来遍历链表。prev 初始化为哑节点，curr 初始化为头节点。
3. 遍历链表，比较 curr 节点和它后面节点的值。如果它们相同，就继续向前移动 curr，直到找到一个不同的值或到达链表末尾。
4. 如果 curr 指针在这个过程中移动了（表示有重复的节点），则更新 prev 的 next 指针，以跳过所有重复的节点。
5. 如果没有重复，prev 移动到 curr。
6. 重复步骤 3-5，直到到达链表末尾。
7. 返回哑节点的下一个节点，即新的链表头。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            # 如果当前节点有重复，则跳过所有重复的节点
            if head.next and head.val == head.next.val:
                # 找到下一个不重复的节点
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                # 没有重复，移动prev指针
                prev = prev.next
            
            head = head.next

        return dummy.next
