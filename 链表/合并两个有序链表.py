"""
为了合并两个升序链表为一个新的升序链表，我们可以使用迭代的方式，
比较两个链表的当前节点，然后将较小的节点添加到新链表中。具体步骤如下：

1. 创建一个哑节点（dummy node），用于简化边界情况的处理。
2. 创建一个指针 current，初始时指向哑节点。
3. 遍历两个链表，直到至少有一个链表被遍历完毕。
4. 在每次迭代中，比较两个链表当前节点的值，将较小值的节点添加到 current 的 next。
5. 移动 current 指针和较小值节点所在链表的指针。
6. 遍历结束后，将未结束的链表剩余部分拼接到新链表末尾。
7. 返回哑节点的下一个节点，即合并后链表的头节点。
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建哑节点
        dummy = ListNode(0)
        # 当前节点
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 如果其中一个链表已经遍历完，将另一个链表的剩余部分连接到当前链表的末尾
        current.next = list1 if list1 else list2

        # 返回合并后的链表头节点
        return dummy.next


def create_linked_list(arr: list[int]) -> Optional[ListNode]:
    """根据给定的列表创建链表"""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def print_linked_list(head: Optional[ListNode]):
    """打印链表的内容"""
    current = head
    res = []
    while current:
        res.append(current.val)
        current = current.next
    print(res)


# test
l1 = [1, 2, 2, 3, 4, 8, 20, 30, 44, 89]
l2 = [1, 3, 4, 7, 8, 22, 53, 56]

l1_head = create_linked_list(l1)
l2_head = create_linked_list(l2)

solution = Solution()
print_linked_list(solution.mergeTwoLists(l1_head, l2_head))
