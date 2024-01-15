"""
这个问题可以通过维护两个链表来解决：一个用于存放所有小于 x 的节点，另一个用于存放所有大于或等于 x 的节点。
在遍历原始链表的过程中，根据节点的值将它们分配到这两个链表中。遍历结束后，将小于 x 的链表与大于或等于 x 的链表连接起来。
这样做可以保证每个节点的初始相对位置不变。

下面是具体地解题步骤：

1. 创建两个新的链表头节点，分别命名为 less_head 和 greater_head，用于存放小于 x 和大于等于 x 的节点。
2. 创建两个指针，less 和 greater，分别指向这两个新链表的当前位置。
3. 遍历原始链表。对于每个节点，根据其值与 x 的比较结果，将它添加到 less 或 greater 链表的末尾。
4. 遍历完成后，将 less 链表的末尾连接到 greater_head 的下一个节点上（即 greater 链表的起始位置）。
5. 返回 less_head 的下一个节点，因为 less_head 是一个空的头节点。
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 创建两个新链表的头节点
        less_head = ListNode(0)
        greater_head = ListNode(0)

        # 初始化两个链表的当前位置指针
        less = less_head
        greater = greater_head

        # 遍历原始链表
        while head:
            # 如果当前节点的值小于x，将其加入less链表
            if head.val < x:
                less.next = head
                less = less.next
            else:
                # 否则，将其加入greater链表
                greater.next = head
                greater = greater.next
            # 移动到下一个节点
            head = head.next

        # 将less链表的末尾连接到greater链表的起始位置
        less.next = greater_head.next
        # 将greater链表的末尾设置为None，避免形成循环链表
        greater.next = None

        # 返回重新排列后的链表的头节点
        return less_head.next


# test
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
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# 示例数据和分割值
arr = [1, 4, 3, 2, 5, 2]
x = 3


# 创建链表并应用分割函数
head = create_linked_list(arr)
solution = Solution()
new_head = solution.partition(head, x)

# 打印结果链表
print_linked_list(new_head)


arr1 = [8, 4, 30, 2, 5, 2, 11, 10, 9, 20]
x1 = 10
head1 = create_linked_list(arr1)
new_head1 = solution.partition(head1, x1)
print_linked_list(new_head1)