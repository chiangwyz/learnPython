"""
为了判断链表中是否存在环，可以使用“快慢指针”方法。
这个方法涉及两个指针，一个移动速度是另一个的两倍。
如果链表中存在环，那么这两个指针最终会在环内相遇；如果不存在环，那么快指针将到达链表的末尾。
"""

from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 初始化快慢指针，初始都指向头节点
        slow = head
        fast = head

        # 遍历链表
        while fast and fast.next:
            slow = slow.next  # 慢指针每次移动一步
            fast = fast.next.next  # 快指针每次移动两步

            # 如果快慢指针相遇，则表示存在环
            if slow == fast:
                return True

        # 如果快指针到达链表末尾（即fast或fast.next为None），则不存在环
        return False


def create_linked_list_with_cycle(array: list[int], pos: int) -> Optional[ListNode]:
    if not array:
        return None

    head = ListNode(array[0])
    current = head
    # 用于存储所有节点的引用
    nodes = [head]

    for element in array[1:]:
        current.next = ListNode(element)
        current = current.next
        nodes.append(current)

    if pos != -1 and pos < len(nodes):
        # 创建环：将最后一个节点的 next 指向第 pos 个节点
        current.next = nodes[pos]

    return head

# test
array = [3, 2, 0, -4, 2]
pos = 1

head = create_linked_list_with_cycle(array, pos)

sol = Solution()
print(sol.hasCycle(head))
