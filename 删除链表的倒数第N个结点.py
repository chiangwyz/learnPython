"""
创建哑节点：哑节点是一个辅助节点，它的 next 指针指向链表的头节点。这是为了简化在链表头部进行操作的复杂性，特别是当需要删除头节点时。
使用两个指针：fast（快指针）和 slow（慢指针），这两个指针一开始都指向哑节点。
先移动快指针：将快指针向前移动 n 步。这样，快指针和慢指针之间就会有 n 个节点的间隔。
同时移动快慢指针：同时移动快指针和慢指针，直到快指针指向最后一个节点。此时，慢指针的下一个节点就是我们需要删除的节点。
删除节点：更改慢指针的 next，使其指向下一个节点的下一个节点，从而跳过需要删除的节点。
返回新的头节点：由于哑节点的 next 指向新的头节点，所以返回 dummy.next。
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # 创建一个哑节点，其 next 指向头节点
        fast = slow = dummy  # 初始化快慢指针，都指向哑节点
        
        # 先移动快指针 n 步
        for _ in range(n):
            fast = fast.next

        # 同时移动快慢指针，直到快指针到达最后一个节点
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 跳过慢指针的下一个节点，即删除它
        slow.next = slow.next.next
        
        return dummy.next  # 返回新的头节点
