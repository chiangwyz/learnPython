"""
为了判断链表中是否存在环，可以使用“快慢指针”方法。
这个方法涉及两个指针，一个移动速度是另一个的两倍。
如果链表中存在环，那么这两个指针最终会在环内相遇；如果不存在环，那么快指针将到达链表的末尾。

具体实现如下：
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 初始化快慢指针，初始都指向头节点
        slow = fast = head

        # 遍历链表
        while fast and fast.next:
            slow = slow.next         # 慢指针每次移动一步
            fast = fast.next.next    # 快指针每次移动两步

            # 如果快慢指针相遇，则表示存在环
            if slow == fast:
                return True

        # 如果快指针到达链表末尾（即fast或fast.next为None），则不存在环
        return False
